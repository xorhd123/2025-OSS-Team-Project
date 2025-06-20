import record
import save
import view_stats
import search
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Menu():
    print("--------------------")
    print("  1. 기록 입력")
    print("  2. 기록 출력")
    print("  3. 기록 수정")
    print("  4. 기록 검색")
    print("  5. 프로그램 종료")
    print("--------------------")
    number = int(input("번호를 입력해주세요: "))

    return number

while True:
    number = Menu()
    clear()
    if number==1:
        save.save_data(record.get_record())
    elif number==2:
        view_stats.display_records(view_stats.load_records())
    elif number==3:
        print("3")
    elif number==4:
        break