import pandas as pd
import numpy as np

# wine 데이터 로드
wine_data = pd.read_csv('wine.csv')

# 데이터 기본 정보 확인
print("=== Wine 데이터 기본 정보 ===")
print(f"데이터 크기: {wine_data.shape}")
print(f"클래스 변수 값: {wine_data['class'].unique()}")
print(f"클래스별 샘플 수:\n{wine_data['class'].value_counts().sort_index()}")
print()

# class 변수 그룹별로 alcohol 평균 계산
ㅇㅇ
print("=== Class별 Alcohol 평균 ===")
print(alcohol_by_class)
print()

# 더 자세한 통계 정보
print("=== Class별 Alcohol 상세 통계 ===")
detailed_stats = wine_data.groupby('class')['alcohol'].describe()
print(detailed_stats)
print()

# 시각화를 위한 추가 분석
print("=== Class별 Alcohol 분포 요약 ===")
for class_val in sorted(wine_data['class'].unique()):
    class_data = wine_data[wine_data['class'] == class_val]['alcohol']
    print(f"Class {class_val}:")
    print(f"  평균: {class_data.mean():.3f}")
    print(f"  중앙값: {class_data.median():.3f}")
    print(f"  표준편차: {class_data.std():.3f}")
    print(f"  최소값: {class_data.min():.3f}")
    print(f"  최대값: {class_data.max():.3f}")
    print(f"  샘플 수: {len(class_data)}")
    print()

# 전체 데이터의 alcohol 평균과 비교
overall_mean = wine_data['alcohol'].mean()
print(f"전체 데이터 alcohol 평균: {overall_mean:.3f}")
print()

# class별 alcohol 평균과 전체 평균 비교
print("=== Class별 vs 전체 평균 비교 ===")
for class_val in sorted(wine_data['class'].unique()):
    class_mean = wine_data[wine_data['class'] == class_val]['alcohol'].mean()
    diff = class_mean - overall_mean
    print(f"Class {class_val}: {class_mean:.3f} (전체 평균 대비 {diff:+.3f})")
