import csv
# 파일 불러오기
import view_stats

def search_result():
    records = view_stats.load_records() #view_stats.load_records()

    if not records:
        print("기록이 없습니다.")
        return

    print("\n검색 기준을 선택하세요")
    print("1. 날짜로 검색")
    print("2. 유형으로 검색")
    print("3. 카테고리로 검색")
    choice = int(input("번호 입력: "))

    if(choice == 1 or choice == 2):
        keyword = input("검색어를 입력하세요: ").strip()

    if(choice == 3):
        categories = {
        1: "식비",
        2: "교통",
        3: "쇼핑",
        4: "문화",
        5: "건강",
        6: "교육",
        7: "생활",
        8: "저축",
        9: "기타",
        10: "급여",
        11: "용돈",
        12: "금융소득",
        13: "공적 지원금",
        14: "환급",
        15: "중고물품 판매"
    }

        i=0

        print("\n카테고리를 선택하세요:")
        for num, name in categories.items():
                if i==9:
                    print()
                    print("=====수입 카테고리=====")
                print(f"[{num}] {name}")
                i+=1

        while True:
            category_choice = int(input("카테고리 번호 입력: "))
            if category_choice in categories:
                keyword = categories[category_choice].strip()
                break
            print("올바른 번호를 입력해주세요 (1~15).")


    found = False
    print("\n===== 검색 결과 =====")

    for r in records:
        # 날짜 검색
        if choice == 1 and keyword in r['날짜']:
            print(f"[{r['날짜']}] {r['유형']} - {r['카테고리']} / {r['아이템']} / {r['금액']}원")
            found = True
        #유형 검색
        if choice == 2 and keyword in r['유형']:
            print(f"[{r['날짜']}] {r['유형']} - {r['카테고리']} / {r['아이템']} / {r['금액']}원")
            found = True
        # 카테고리 검색
        if choice == 3 and keyword in r['카테고리']:
            print(f"[{r['날짜']}] {r['유형']} - {r['카테고리']} / {r['아이템']} / {r['금액']}원")
            found = True

    if not found:
        print(f"'{keyword}'에 해당하는 기록이 없습니다.")

    print("=======================")
    input("\n아무 키를 입력시 종료합니다.")

# 테스트용 실행
if __name__ == '__main__':
    search_result()