from datetime import datetime
#수입 지출 함수
def get_transaction_type():
    while True:
        t_type = input("수입 또는 지출을 입력하세요 (수입/지출): ").strip()
        if t_type in ['수입', '지출']:
            return t_type
        print("잘못 입력했습니다. '수입' 또는 '지출' 중에 선택해주세요.")
#금액 입력
def get_amount():
    while True:
        amount = input("금액을 입력하세요 (숫: ").strip()
        if amount.isdigit():
            return amount
        print("숫자만 입력해주세요.")