import csv
from collections import defaultdict
import os

DATA_FILE = 'data.csv'

def save_records(records, filename=DATA_FILE):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for r in records:
            writer.writerow([
                r['date'],
                r['category'],
                r['item'],
                r['amount'],
                r['type']
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
        print(f"{idx}: [{r['date']}] {r['type']} - {r['category']} / r['item'] / r['amount']원")
    print("--------------------")

    try:
        i = int(input("수정할 번호를 입력하세요: ").strip())
        record = records[i-1]
    except (ValueError, IndexError):
        print("잘못된 번호입니다")
        return
    
    fields = ['date', 'category', 'item', 'amount', 'type']
    print("수정할 부분을 선택하세요:",",".join(fields))
    field = input("수정부분: ").strip()
    if field not in fields:
        print("잘못 입력하셨습니다.")
        return
    
    new_write = input(f"새 {field} 값 입력 (현재: {record[field]}): ").strip()
    if field == 'amount' and not new_write.isdigit():
        print("숫자만 입력 가능")
        return
    if field == 'type' and new_write not in ('지출', '수입'):
        print("type은 '지출' 또는 '수입'만 입력 가능합니다")
        return
    
    record[field] = new_write
    save_records(records)