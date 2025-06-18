import csv
from collections import defaultdict

DATA_FILE = 'data.csv'

def load_records(filename=DATA_FILE):
    records = []
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, fieldnames=['data','category','item','amount','type'])
            for row in reader:
                records.append(row)
    except FileExistsError:
        print(f"기록 없음")
    return records

def display_records(records):
    if not records:
        print("기록 없음")
        return
    
    print("-----------------")
    print("     records     ")
    print("-----------------")
    for r in records:
        print(f"[{r['date']}] {r['type']} - {r['category']} / {r['item']} / {r['amount']}원")
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
    for cat, total in totals.items():
        print(f"{cat}: {total}원")
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
    for cat, total in totals.items():
        print(f"{cat}: {total}원")
    print() 


def main():
    records = load_records()
    display_records(records)
    display_category(records)
    display_income(records)

if __name__ == '__main__':
    main()