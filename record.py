def get_transaction_type():
    while True:
        t_type = input("수입 또는 지출을 입력하세요 (수입/지출): ").strip()
        if t_type in ['수입', '지출']:
            return t_type
        print("잘못 입력했습니다. '수입' 또는 '지출' 중에 선택해주세요.")