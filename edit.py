import csv
from collections import defaultdict
import os

DATA_FILE = 'data.csv'


def load_records(filename=DATA_FILE):
    records = []
    if not os.path.exists(filename):
        return records

    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, fieldnames=['날짜','유형','카테고리','아이템','금액'])
        for row in reader:
            records.append(row)
    return records

def save_records(records, filename=DATA_FILE):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for r in records:
            writer.writerow([
                r['날짜'],
                r['유형'],
                r['카테고리'],
                r['아이템'],
                r['금액']
            ])
    print(f"수정 내용 저장 완료")

def rewrite_record(records):
    if not records:
        print("수정 가능한 항목 없음")
        return
    
    print("--------------------")
    print("   수정 가능한 항목   ")
    print("--------------------")
    for idx, r in enumerate(records, start=1):
        print(f"{idx}: [{r['날짜']}] {r['유형']} - {r['카테고리']} / {r['아이템']} / {r['금액']}원")
    print("--------------------")

    while True:
        try:
            i = int(input("수정할 번호를 입력하세요: ").strip())
            if 1 <= i <= len(records):
                record = records[i-1]
                break
            else:
                print(f"잘돗된 번호입니다. 다시 입력해주세요.")
        except ValueError:
            print("숫자를 입력해주세요")
        
    fields = ['날짜', '유형', '카테고리', '아이템', '금액']
    while True:
        print("수정할 부분을 선택하세요:")
        for f in fields:
            print(f" -{f} (현재: {record[f]})")
        field = input("수정부분: ").strip()
        if field not in fields:
            print("잘못 입력하셨습니다. 다시 선택해주세요.")
            continue
        
        if field == '카테고리':
            categories = {
                "1": "식비",
                "2": "교통",
                "3": "쇼핑",
                "4": "문화",
                "5": "건강",
                "6": "교육",
                "7": "생활",
                "8": "저축",
                "9": "기타"
            }

            print("\n카테고리를 선택하세요:")
            for num, name in categories.items():
                print(f"[{num}] {name}")

            while True:
                choice = input("카테고리 번호 입력: ").strip()
                if choice in categories:
                    new_write = categories[choice]
                    break
                else:
                    print("올바른 번호를 입력해주세요 (1~9).")
        break
        
    while True:
        if field == '카테고리':
            break
        new_write = input(f"새 {field} 값 입력 (현재: {record[field]}): ").strip()
        if field == '금액':
            if not new_write.isdigit():
                print("숫자만 입력 가능합니다.")
                continue
        if field == '유형':
            if new_write not in ('지출', '수입'):
                print("type은 '지출' 또는 '수입'만 입력 가능합니다")
                continue
        break
    
    record[field] = new_write
    save_records(records)