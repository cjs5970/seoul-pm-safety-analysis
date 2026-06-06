from __future__ import annotations

import re
from pathlib import Path

import pandas as pd


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "original-datasets" / "교통사고 분석 시스템(TAAS)"
OUTPUT_DIR = SCRIPT_DIR
PM_LABEL = "개인형이동수단(PM)"

DISTRICTS = [
    "강남구",
    "강동구",
    "강북구",
    "강서구",
    "관악구",
    "광진구",
    "구로구",
    "금천구",
    "노원구",
    "도봉구",
    "동대문구",
    "동작구",
    "마포구",
    "서대문구",
    "서초구",
    "성동구",
    "성북구",
    "송파구",
    "양천구",
    "영등포구",
    "용산구",
    "은평구",
    "종로구",
    "중구",
    "중랑구",
]


def parse_year_month(value: object) -> pd.Timestamp:
    if pd.isna(value):
        return pd.NaT

    match = re.search(r"(?P<year>\d{4})년\s*(?P<month>\d{1,2})월", str(value))
    if not match:
        return pd.NaT

    return pd.Timestamp(int(match.group("year")), int(match.group("month")), 1)


def extract_district(value: object) -> str | None:
    text = "" if pd.isna(value) else str(value)
    for district in DISTRICTS:
        if district in text:
            return district
    return None


def split_category(series: pd.Series, index: int) -> pd.Series:
    return series.astype(str).str.split(" - ").str[index].replace("nan", pd.NA)


def format_accident_id(value: object) -> str | None:
    if pd.isna(value):
        return None

    try:
        return str(int(float(value)))
    except (TypeError, ValueError):
        text = str(value).strip()
        return text if text else None


def load_pm_raw() -> pd.DataFrame:
    frames = []
    for path in sorted(DATA_DIR.glob("20*.xlsx")):
        df = pd.read_excel(path).dropna(how="all").copy()
        if "구분번호" not in df.columns:
            df["구분번호"] = pd.NA
        df["원본파일"] = path.name
        frames.append(df)

    if not frames:
        raise FileNotFoundError("PM 교통사고 원본 엑셀 파일을 찾을 수 없습니다.")

    return pd.concat(frames, ignore_index=True)


def make_event_level(raw: pd.DataFrame) -> pd.DataFrame:
    df = raw.copy()
    df["발생년월_dt"] = df["발생년월"].apply(parse_year_month)
    df["연월"] = df["발생년월_dt"].dt.strftime("%Y-%m")
    df["연도"] = df["발생년월_dt"].dt.year.astype("Int64")
    df["월"] = df["발생년월_dt"].dt.month.astype("Int64")
    df["자치구"] = df["시군구"].apply(extract_district)

    for column in ["사망자수", "중상자수", "경상자수", "부상신고자수"]:
        df[column] = pd.to_numeric(df[column], errors="coerce").fillna(0).astype(int)

    df["총부상자수"] = df["중상자수"] + df["경상자수"] + df["부상신고자수"]
    df["총사상자수"] = df["사망자수"] + df["총부상자수"]
    df["중상이상자수"] = df["사망자수"] + df["중상자수"]

    df["사고ID"] = df["구분번호"].apply(format_accident_id)
    missing_id = df["사고ID"].isna()
    df.loc[missing_id, "사고ID"] = [
        f"PM-{year}-{idx + 1:05d}"
        for idx, year in zip(df.loc[missing_id].index, df.loc[missing_id, "연도"])
    ]

    df["사고유형_대분류"] = split_category(df["사고유형"], 0)
    df["사고유형_소분류"] = split_category(df["사고유형"], 1)
    df["도로형태_대분류"] = split_category(df["도로형태"], 0)
    df["도로형태_소분류"] = split_category(df["도로형태"], 1)

    df["PM_가해여부"] = df["가해운전자 차종"].eq(PM_LABEL).map({True: "Y", False: "N"})
    df["PM_피해여부"] = df["피해운전자 차종"].eq(PM_LABEL).map({True: "Y", False: "N"})
    df["PM_역할"] = "기타"
    df.loc[df["PM_가해여부"].eq("Y"), "PM_역할"] = "가해"
    df.loc[df["PM_피해여부"].eq("Y"), "PM_역할"] = "피해"
    df.loc[df["PM_가해여부"].eq("Y") & df["PM_피해여부"].eq("Y"), "PM_역할"] = "가해+피해"

    renamed = df.rename(
        columns={
            "가해운전자 차종": "가해운전자_차종",
            "가해운전자 성별": "가해운전자_성별",
            "가해운전자 연령대": "가해운전자_연령대",
            "가해운전자 상해정도": "가해운전자_상해정도",
            "피해운전자 차종": "피해운전자_차종",
            "피해운전자 성별": "피해운전자_성별",
            "피해운전자 연령대": "피해운전자_연령대",
            "피해운전자 상해정도": "피해운전자_상해정도",
        }
    )

    columns = [
        "사고ID",
        "연월",
        "연도",
        "월",
        "자치구",
        "주야",
        "사고내용",
        "사고유형",
        "사고유형_대분류",
        "사고유형_소분류",
        "법규위반",
        "노면상태",
        "기상상태",
        "도로형태",
        "도로형태_대분류",
        "도로형태_소분류",
        "사망자수",
        "중상자수",
        "경상자수",
        "부상신고자수",
        "총부상자수",
        "총사상자수",
        "중상이상자수",
        "PM_가해여부",
        "PM_피해여부",
        "PM_역할",
        "가해운전자_차종",
        "가해운전자_성별",
        "가해운전자_연령대",
        "가해운전자_상해정도",
        "피해운전자_차종",
        "피해운전자_성별",
        "피해운전자_연령대",
        "피해운전자_상해정도",
        "원본파일",
    ]

    return renamed[columns].sort_values(["연월", "자치구", "사고ID"]).reset_index(drop=True)


def make_monthly_panel(events: pd.DataFrame) -> pd.DataFrame:
    month_index = pd.date_range("2019-01-01", "2024-12-01", freq="MS")
    panel = pd.MultiIndex.from_product(
        [month_index, DISTRICTS], names=["발생년월_dt", "자치구"]
    ).to_frame(index=False)
    panel["연월"] = panel["발생년월_dt"].dt.strftime("%Y-%m")
    panel["연도"] = panel["발생년월_dt"].dt.year.astype(int)
    panel["월"] = panel["발생년월_dt"].dt.month.astype(int)

    work = events.copy()
    work["발생년월_dt"] = pd.to_datetime(work["연월"] + "-01", errors="coerce")
    work["PM_가해사고"] = work["PM_가해여부"].eq("Y")
    work["PM_피해사고"] = work["PM_피해여부"].eq("Y")
    work["야간사고"] = work["주야"].eq("야간")

    monthly = (
        work.groupby(["발생년월_dt", "자치구"], dropna=False)
        .agg(
            PM_사고건수=("사고ID", "count"),
            사망자수=("사망자수", "sum"),
            중상자수=("중상자수", "sum"),
            경상자수=("경상자수", "sum"),
            부상신고자수=("부상신고자수", "sum"),
            총부상자수=("총부상자수", "sum"),
            총사상자수=("총사상자수", "sum"),
            중상이상자수=("중상이상자수", "sum"),
            PM_가해사고건수=("PM_가해사고", "sum"),
            PM_피해사고건수=("PM_피해사고", "sum"),
            야간사고건수=("야간사고", "sum"),
        )
        .reset_index()
    )

    result = panel.merge(monthly, on=["발생년월_dt", "자치구"], how="left")
    count_columns = [
        "PM_사고건수",
        "사망자수",
        "중상자수",
        "경상자수",
        "부상신고자수",
        "총부상자수",
        "총사상자수",
        "중상이상자수",
        "PM_가해사고건수",
        "PM_피해사고건수",
        "야간사고건수",
    ]
    result[count_columns] = result[count_columns].fillna(0).astype(int)

    columns = ["연월", "자치구", "연도", "월"] + count_columns
    return result[columns].sort_values(["연월", "자치구"]).reset_index(drop=True)


def make_annual_panel(monthly: pd.DataFrame) -> pd.DataFrame:
    count_columns = [
        "PM_사고건수",
        "사망자수",
        "중상자수",
        "경상자수",
        "부상신고자수",
        "총부상자수",
        "총사상자수",
        "중상이상자수",
        "PM_가해사고건수",
        "PM_피해사고건수",
        "야간사고건수",
    ]
    annual = monthly.groupby(["연도", "자치구"], as_index=False)[count_columns].sum()
    columns = ["연도", "자치구"] + count_columns
    return annual[columns].sort_values(["연도", "자치구"]).reset_index(drop=True)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    raw = load_pm_raw()
    events = make_event_level(raw)
    monthly = make_monthly_panel(events)
    annual = make_annual_panel(monthly)

    events.to_csv(OUTPUT_DIR / "서울시_PM_교통사고_사고단위.csv", index=False, encoding="utf-8-sig")
    monthly.to_csv(OUTPUT_DIR / "서울시_자치구별_월별_PM교통사고.csv", index=False, encoding="utf-8-sig")
    annual.to_csv(OUTPUT_DIR / "서울시_자치구별_연도별_PM교통사고.csv", index=False, encoding="utf-8-sig")

    print(f"output dir: {OUTPUT_DIR.resolve()}")
    print(f"event rows: {len(events):,}")
    print(f"monthly rows: {len(monthly):,}")
    print(f"annual rows: {len(annual):,}")


if __name__ == "__main__":
    main()
