import csv
# 파일 불러오기
# import view_stats

def search_result():
    records = load_records() #view_stats.load_records()

    if not records:
        print("기록이 없습니다.")
        return

    print("\n검색 기준을 선택하세요")
    print("1. 날짜로 검색")
    print("2. 유형으로 검색")
    print("3. 카테고리로 검색")
    choice = input("번호 입력: ").strip()

    keyword = input("검색어를 입력하세요: ").strip()

    found = False
    print("\n===== 검색 결과 =====")

    for r in records:
        # 날짜 검색
        if choice == '1' and keyword in r['날짜']:
            print(f"[{r['날짜']}] {r['유형']} - {r['카테고리']} / {r['아이템']} / {r['금액']}원")
            found = True
        #유형 검색
        if choice == '1' and keyword in r['유형']:
            print(f"[{r['날짜']}] {r['유형']} - {r['카테고리']} / {r['아이템']} / {r['금액']}원")
            found = True
        # 카테고리 검색
        elif choice == '3' and keyword in r['카테고리']:
            print(f"[{r['날짜']}] {r['유형']} - {r['카테고리']} / {r['아이템']} / {r['금액']}원")
            found = True

    if not found:
        print(f"'{keyword}'에 해당하는 기록이 없습니다.")

    print("=======================")
    input("\n아무 키나 누르면 종료합니다.")

# 테스트용 실행
if __name__ == '__main__':
    search_result()