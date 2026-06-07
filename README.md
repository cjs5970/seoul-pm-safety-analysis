# 서울시 공유 자전거 및 PM 안전 규제 영향 분석
### **[2026-1학기] 고급프로그래밍설계 01분반 10조 Term Project**
[Google Drive Link(참고용)](https://drive.google.com/drive/folders/1SD4E_i3LVfp4WcNHgni37XIGH7OtbBKA)

## 프로젝트 주제
**서울시 내 안전 규제 도입이 공유 자전거(따릉이) 및 개인형 이동장치(PM) 이용량과 교통사고 발생 추이에 미치는 영향 분석**

## 프로젝트 목적
최근 몇 년간 서울시의 PM 및 공유 자전거 관련 법규(안전모 착용 의무화, 불법 주정차 견인 제도 등)가 강화되었습니다. 본 프로젝트는 이러한 규제들이 실제 시민들의 모빌리티 이용 패턴과 사고율 감소에 실효성이 있었는지 데이터에 기반하여 통계적으로 검증하는 것을 목적으로 합니다. 

## 디렉터리 구조
```text
📦 seoul-pm-safety-analysis
┣ 📂 data
┃ ┣ 📂 data-preprocessing   # original-datasets -> 데이터 전처리 수행 과정(ipynb/py) 및 결과 데이터셋
┃ ┗ 📂 original-datasets    # 교통사고 분석 시스템(TAAS), 서울시 공공데이터 등에서 수집한 원본 데이터셋 
┣ 📂 analysis
┃ ┣ 📂 서영웅_분석_결과   # EDA, 데이터 시각화 및 통계 분석 결과(ipynb) (서영웅)
┃ ┗ 📂 최준성_분석_결과   # EDA, 데이터 시각화 및 통계 분석 결과(ipynb) (최준성)
┗ 📜 README.md
```

## 팀원 구성 및 주요 역할

본 프로젝트는 2인 1조로 진행되었으며, 데이터 전처리(TAAS/서울시 공공데이터)와 통계 검증, 그리고 시각화를 통한 사고 추이 분석으로 심도 있는 탐색적 데이터 분석(EDA)을 수행했습니다.

| 이름 | 주요 담당 업무 | GitHub |
|:---:|:---|:---:|
| **최준성** | **[데이터 수집 및 전처리]**<br>- 서울시 열린데이터광장 공공데이터 5종 수집 및 데이터 정제<br>- 문자열 및 날짜형(datetime) 데이터 병합 시 발생하는 타입 오류 등 원본 데이터 정제, 통합<br><br>**[데이터 분석 및 시각화]**<br>- 가설 1: PM 안전 규제 전후 교통사고 건수 및 치명률 시각화 (Bootstrapping 활용)<br>- 가설 1+: GeoPandas를 활용한 자치구별 공간 시각화 병합 분석 / 가설 1 추가 분석<br>- 가설 2: 코로나19 확진자 수와 PM 사고 건수 간의 상관관계(통제 변수) 분석<br>- 가설 3: PM 규제 강화에 따른 공유 자전거(따릉이) 풍선효과(대체 효과) 상관분석<br><br>**[프로젝트 리딩 및 문서화]**<br>- 구글 드라이브 기반 팀 워크스페이스 구축 및 산출물 통합 관리<br>- 프로젝트 과제제안서, 최종 보고서 및 발표용 PPT 초안 기획 및 작성 | [@cjs5970-Dev](https://github.com/cjs5970) |
| **서영웅** | **[데이터 전처리]**<br>- TAAS 교통사고 원자료를 기반으로 서울시 PM 교통사고 데이터 정제<br>- PM 사고 단위 데이터, 자치구별 월별 사고 데이터, 연도별 사고 데이터 생성<br><br>**[추가 분석 및 시각화]**<br>- 전체 교통사고 대비 PM 사고 비율 분석<br>- 자치구별 사고 위험도 보정 분석<br>- 규제 직전/직후 단기 사고 변화 분석<br>- 사고유형 및 법규위반별 심화 분석<br>- 따릉이 대체효과를 자치구 단위로 추가 검증<br><br>**[통계적 검정 및 결과 해석]**<br>- 규제 전후 단기 사고 변화에 대한 T-test 수행<br>- 규제 전후 법규위반 유형 분포 변화에 대한 카이제곱 검정 수행<br>- 따릉이 이용량과 PM 사고/견인 변수 간 피어슨 상관분석 수행<br>- 추가 분석 결과의 통계적 유의성 해석 및 보고서 작성 내용 정리 | [@SeoHero-Dev](https://github.com/SeoHero-Dev) |


## 기술 스택 및 개발 환경

### 1. Language
* **Python 3.x**

### 2. Data Analysis & Statistics
* **Pandas / NumPy:** 5종 이상의 공공데이터 결측치/이상치 정제, 날짜형(datetime) 데이터 병합 및 대용량 데이터 전처리
* **SciPy (`scipy.stats`):** 피어슨 상관분석, 카이제곱 검정, ANOVA, Bootstrapping 등을 활용한 통계적 유의성 검증

### 3. Data Visualization
* **Matplotlib / Seaborn:** 연도별/월별 교통사고 발생률 및 따릉이 이용량 추이 등 핵심 탐색적 데이터 분석(EDA) 시각화
* **GeoPandas:** 서울시 자치구별 공간 데이터(geojson) 병합 및 지도 기반 교통사고 시각화 분석

### 4. Development Environment
* **IDE & Platform:** Visual Studio Code (Jupyter Notebook Extension), Google Colab
* **OS & Setting:** Windows 11 / `Malgun Gothic`(맑은 고딕) 폰트 기반 시각화 한글 깨짐 방지 세팅
* **Collaboration & Version Control:** Git, GitHub, Google Workspace (Drive, Docs)


## 결과물 유의사항

- 본 GitHub 저장소는 원본 및 전처리 결과 데이터셋, 전처리 및 분석 주피터 노트북 파일들이 위치해 있으며 주요 결과물 업로드 및 설명(MD)을 작성하기 위한 공간입니다. 프로젝트 진행은 [Google Drive](https://drive.google.com/drive/folders/1SD4E_i3LVfp4WcNHgni37XIGH7OtbBKA)를 이용하여 산출물을 통합 관리하였습니다.
- 데이터 분석(analysis) 과정에 사용한 데이터셋(`.csv`)들은 모두 `data/data-preprocessing/` 디렉터리에 위치해 있습니다.
- **현 GitHub 저장소의 디렉터리 구조를 그대로 유지한 채 clone - 실행(ipynb, py)하여 코드의 정상 동작 여부를 확인할 수 있습니다.**

----
----
# 부록
## 사용한 데이터 Link
- [교통사고 분석 시스템(TAAS)](https://taas.koroad.or.kr/web/shp/mik/main.do?menuId=WEB_KMP)


- [서울 열린데이터 광장 - 서울시 공공자전거 따릉이 대여소 정보](https://data.seoul.go.kr/dataList/OA-13252/F/1/datasetView.do)


- [서울 열린데이터 광장 - 서울시 자치구별 코로나 확진자, 사망자 현황](https://data.seoul.go.kr/dataList/OA-20470/F/1/datasetView.do)


- [서울 열린데이터 광장 - 서울시 전동킥보드 견인 현황](https://data.seoul.go.kr/dataList/OA-21304/S/1/datasetView.do)


- [서울 열린데이터 광장 - 월별 따릉이 이용정보](https://data.seoul.go.kr/dataList/OA-15248/F/1/datasetView.do)


- [서울 열린데이터 광장 - 서울시 전동킥보드 주차구역 현황](https://data.seoul.go.kr/dataList/OA-21710/S/1/datasetView.do)
  - [공공데이터포털](https://www.data.go.kr/index.do) - 서울시 예산이 아닌 자치구에서 자치구 예산으로 직접 설치한 주차구역을 포함하기 위해, 공공데이터포털에 등록된 서울시 내 11개 자치구의 전동킥보드 주차구역 데이터를 개별 수집하여 병합하였습니다.


- [공공데이터포털 - 질병관리청_사회적 거리두기 시행연혁](https://www.data.go.kr/data/15106451/fileData.do)


- [Github - hangjeongdong_서울특별시.geojson (aqoon886)](https://github.com/raqoon886/Local_HangJeongDong/blob/master/hangjeongdong_%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C.geojson)


----
## 레퍼런스 Link
## 1. 데이터 조작 및 전처리 (Data Manipulation)

### Pandas (Python Data Analysis Library)
데이터프레임 병합, 시계열 데이터 처리(YoY 증감량 계산), 그룹화 집계 및 전반적인 데이터 전처리의 핵심 도구로 활용되었습니다.
* **공식 레퍼런스:** [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
* **주요 함수:**
  * `pandas.merge`: [Data 상관 병합 및 Inner Join 처리](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)
  * `pandas.crosstab`: [범주형 데이터 간의 교차표(Contingency Table) 생성](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html)
  * `pandas.to_datetime`: [문자열 종속 날짜 데이터를 시계열 Datetime 객체로 변환](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)
  * `pandas.DataFrame.diff`: [시계열 계절성 통제를 위한 12개월 주기(YoY) 증감량 산출](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.diff.html)

### NumPy (Numerical Python)
조건부 데이터 분기 알고리즘 처리 및 파생 변수 생성의 고속 연산 처리에 활용되었습니다.
* **공식 레퍼런스:** [https://numpy.org/doc/stable/](https://numpy.org/doc/stable/)
* **주요 함수:**
  * `numpy.where`: [규제 전후 벡터 분기 및 법규위반 항목 카테고리화 처리](https://numpy.org/doc/stable/reference/generated/numpy.where.html)

---

## 2. 통계 검정 및 가설 확인 (Statistical Analysis)

### SciPy (Scientific Python - `scipy.stats`)
단순 시각적 지표 분석을 넘어, 수집된 표본 데이터의 차이와 연관성이 통계학적으로 유의미한지($p$-value) 수학적으로 검증하는 통계 용도로 활용되었습니다.
* **공식 레퍼런스:** [https://docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)
* **주요 함수:**
  * `scipy.stats.ttest_rel`: [대응표본 T-검정 (규제 전후 동월 사고 건수 비교)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html)
  * `scipy.stats.ttest_ind`: [독립표본 T-검정 (견인 규제 전후 따릉이 이용 증감량 비교)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
  * `scipy.stats.f_oneway`: [일원배치 분산분석 (거리두기 3개 그룹 간 평균 차이 검증)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html)
  * `scipy.stats.pearsonr`: [피어슨 상관계수 산출 (확진자/견인건수와 PM/따릉이 증감량 간 선형 관계 검증)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html)
  * `scipy.stats.chi2_contingency`: [카이제곱 검정 (PM 탑승자 상해 정도 분석 및 자치구별 교차 검증)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)
  * `scipy.stats.fisher_exact`: [피셔의 정확 검정 (소표본 자치구 데이터의 통계적 검정력 한계 증명)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fisher_exact.html)

---

## 3. 데이터 시각화 (Data Visualization)

### Matplotlib
그래프의 전반적인 레이아웃 프레임 구조 설계, 이중 축 설정, 임계 기준선 등 시각적 객체의 세부적인 통제 기능을 수행했습니다.
* **공식 레퍼런스:** [https://matplotlib.org/stable/api/index.html](https://matplotlib.org/stable/api/index.html)
* **주요 함수:**
  * `matplotlib.pyplot.subplots`: [다중 축 인스턴스 레이아웃 배열 구성](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)
  * `matplotlib.pyplot.twinx`: [서로 다른 단위를 가진 시계열 추이 비교용 이중 Y축(Dual Axis) 구성](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.twinx.html)
  * `matplotlib.axes.Axes.invert_yaxis`: [수평 막대 그래프의 하향식 가독성을 위한 Y축 정렬 방향 반전](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_yaxis.html)
  * `matplotlib.pyplot.axhline`: [YoY 증감량의 성장/감소 분기점인 0점 임계선(Zero Line) 배치](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhline.html)

### Seaborn
데이터의 내포된 분포 확률 밀도, 선형 회귀 추세, 그룹별 밀집 구조를 세련된 통계 그래픽스 형태로 변환하는 역할을 담당했습니다.
* **공식 레퍼런스:** [https://seaborn.pydata.org/api.html](https://seaborn.pydata.org/api.html)
* **주요 함수:**
  * `seaborn.regplot`: [산점도와 선형 회귀 평면 추세선의 결합 시각화](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot)
  * `seaborn.violinplot`: [사분위수 위치 정보와 커널 밀도 추정(KDE) 곡선의 동시 결합 분포 시각화](https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot)
  * `seaborn.stripplot`: [범주별 실제 관측 데이터 포인트의 지터(Jitter) 기반 개별 분포 매핑](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn-stripplot)
  * `seaborn.barplot`: [집계된 범주형 통계 수치의 크기 비교](https://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn-barplot)

---

## 4. 공간 데이터 분석 및 지도 시각화 (Geospatial Analysis)

### GeoPandas
서울시 행정동 GeoJSON 지리정보 데이터를 자치구 단위 공간 폴리곤 데이터로 통합 연산하고, 이를 단계구분도(Choropleth Map) 형태로 표출하는 핵심 연산 공간 모델로 활용되었습니다.
* **공식 레퍼런스:** [https://geopandas.org/en/stable/docs.html](https://geopandas.org/en/stable/docs.html)
* **주요 함수:**
  * `geopandas.read_file`: [공간 인프라 파일 정보(GeoJSON) 로드](https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html)
  * `geopandas.GeoDataFrame.dissolve`: [하위 행정구역 속성 폴리곤 객체를 상위 자치구 단위 공간 레이어로 병합 통합](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.dissolve.html)
  * `geopandas.GeoDataFrame.plot`: [지리 좌표계 기반 데이터 맵 렌더링 및 통계적 컬러맵(`cmap`) 매핑](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.plot.html)
