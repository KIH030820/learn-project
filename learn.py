def add_task(tasks, task):
    tasks.append(task)
    print("할 일이 추가되었습니다.")
    //할 일 추가//

def view_tasks(tasks):
    if not tasks:
        print("등록된 할 일이 없습니다.")
        return

    print("\n[할 일 목록]")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    //할 일 목록 출력//

def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"'{removed}' 삭제 완료")
    else:
        print("잘못된 번호입니다.")
