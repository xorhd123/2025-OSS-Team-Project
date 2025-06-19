from datetime import datetime

#수입 지출 함수
def get_transaction_type():
    while True:
        t_type = input("수입 또는 지출을 입력하세요 (수입/지출): ").strip()
        if t_type in ['수입', '지출']:
            return t_type
        print("잘못 입력했습니다. '수입' 또는 '지출' 중에 선택해주세요.")

#금액 입력 함수
def get_amount():
    while True:
        amount = input("금액을 입력하세요 (숫: ").strip()
        if amount.isdigit():
            return amount
        print("숫자만 입력해주세요.")

#항목명 입력
def get_item():
    return input("항목명을 입력하세요 (예: 점심, 월급 등): ").strip()

#카테고리 선택 함수
def select_category():
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
            return categories[choice]
        print("올바른 번호를 입력해주세요 (1~9).")

#수입 항목명 입력
def get_income_item():
    return input("수입 항목명을 입력하세요 (예: 월급, 장학금 등): ").strip()

#현재 시간
def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")