import csv
from collections import defaultdict

DATA_FILE = 'data.csv'

def load_records(filename=DATA_FILE):
    records = []
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, fieldnames=['날짜','유형', '카테고리', '아이템', '금액'])
            for row in reader:
                records.append(row)
    except FileNotFoundError:
        print(f"기록 없음")
    return records

def display_records(records):
    if not records:
        print("기록 없음")
        return
    
    print("-----------------")
    print(" display records ")
    print("-----------------")
    for r in records:
        print(f"[{r['날짜']}] {r['유형']} - {r['카테고리']} / {r['아이템']} / {r['금액']}원")
    print()

def display_category(records):
    totals = defaultdict(int)
    for r in records:
        if r['type'] == '지출':
            totals[r['category']] += int(r['amount'])

    if not totals:
        print("지출 내역 없음")
        return
    
    print("-----------------")
    print("      total      ")
    print("-----------------")
    total_sum = 0
    for cat, amt in totals.items():
        print(f"{cat}: {amt}원")
        total_sum += amt
    print(">>")
    print(f"총 지출: {total_sum}원\n")
    print()

def display_income(records):
    totals = defaultdict(int)
    for r in records:
        if r['type'] == '수입':
            totals[r['category']] += int(r['amount'])

    if not totals:
        print("수입 내역 없음")
        return
    
    print("------------------")
    print("      income      ")
    print("------------------")
    total_sum = 0
    for cat, amt in totals.items():
        print(f"{cat}: {amt}원")
        total_sum += amt
    print(">>")
    print(f"총 지출: {total_sum}원\n")
    print() 