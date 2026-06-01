from todo import add_task, view_tasks, delete_task
from file_manager import load_tasks, save_tasks

tasks = load_tasks()

while True:
    print("\n===== TODO LIST =====")
    print("1. 할 일 추가")
    print("2. 할 일 조회")
    print("3. 할 일 삭제")
    print("4. 종료")

    choice = input("선택: ")

    if choice == "1":
        task = input("할 일을 입력하세요: ")
        add_task(tasks, task)
        save_tasks(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        view_tasks(tasks)
        index = int(input("삭제할 번호 입력: "))
        delete_task(tasks, index)
        save_tasks(tasks)

    elif choice == "4":
        print("프로그램 종료")
        break

    else:
        print("잘못된 입력입니다.")