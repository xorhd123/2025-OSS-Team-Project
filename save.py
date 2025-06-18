import csv
import os


def save_data(data, filename='data.csv'):
    """
    입력받은 데이터를 CSV 파일로 저장
    filename (str): 저장할 파일 이름 (기본값: data.csv)
    """
    file_exists = os.path.isfile(filename)

    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # 파일이 존재하지 않으면 헤더 추가
        if not file_exists:
            writer.writerow(['날짜', '유형', '카테고리', '아이템', '금액'])  # 필요에 따라 수정 가능

        writer.writerow(data)

