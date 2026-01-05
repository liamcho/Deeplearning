import os
import pandas as pd
from glob import glob
from datetime import datetime
import shutil
from collections import defaultdict


# CSV 로드
csv_path = "ADSP-PHC__ADNI_T1_1.0_5_08_2025.csv"
df = pd.read_csv(csv_path)


# 열 이름 확인
print(df.columns)


# 사용자에게 직접 지정하게 하거나 아래 열 이름을 실제 열 이름으로 수정
# 환자 ID 열
id_col = "Subject"  # 예: 'Subject' 또는 'RID'
# 날짜 열
date_col = "Acq Date"  # 예: 'SCANDATE', 형식은 'YYYY-MM-DD'


# (환자ID, 날짜) 튜플 만들기
df[date_col] = pd.to_datetime(df[date_col]).dt.date
valid_pairs = set(zip(df[id_col].astype(str), df[date_col].astype(str)))


# MRI 경로
base_dir = "Cohort_2_MRI/ADNI"


# 유지할 MRI 폴더 목록
kept_folders = []

for patient_folder in os.listdir(base_dir):
    patient_path = os.path.join(base_dir, patient_folder)
    if not os.path.isdir(patient_path):
        continue
    
    for subfolder in os.listdir(patient_path):
        full_path = os.path.join(patient_path, subfolder)
        if not os.path.isdir(full_path):
            continue
        
        for scan_folder in os.listdir(full_path):
            scan_path = os.path.join(full_path, scan_folder)
            if not os.path.isdir(scan_path):
                continue
            
            # 날짜 추출 시 앞부분 10자리 (예: '2006-04-18')
            try:
                scan_date = scan_folder[:10]
                scan_date = datetime.strptime(scan_date, "%Y-%m-%d").date()
            except:
                continue
            
            key = (patient_folder, str(scan_date))
            
            if key in valid_pairs:
                kept_folders.append(scan_path)
            else:
                # 삭제
                print(f"Deleting unmatched folder: {scan_path}")
                shutil.rmtree(scan_path, ignore_errors=True)



# 결과 저장용 딕셔너리
patient_image_count = defaultdict(int)


# 기준 디렉토리
base_dir = "Cohort_2_MRI/ADNI"


# 순회하며 환자별 이미지 수 세기
for patient_id in os.listdir(base_dir):
    patient_path = os.path.join(base_dir, patient_id)
    if not os.path.isdir(patient_path):
        continue

    for root, dirs, files in os.walk(patient_path):
        for file in files:
            if file.endswith(".dcm") or "raw" in file or file.endswith(".nii"):
                patient_image_count[patient_id] += 1


# 출력
for patient_id, count in sorted(patient_image_count.items()):
    print(f"{patient_id}: {count} images")


print(f"남아 있는 환자 수: {len(patient_image_count)}\n")