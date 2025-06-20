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
            writer.writerow(['날짜', '카테고리', '아이템', '금액', '유형'])  # 필요에 따라 수정 가능

        writer.writerow(data)

# 테스트용 예시 실행
if __name__ == "__main__":
    test_data = ['2025.06.18', '지출', '식비', '점심', 12000]
    save_data(test_data)
    print("✅ 테스트 저장 완료")