from Logic import ToDoList


def main():
    todo = ToDoList()
    while True:
        try:
            print('\n--- СПИСОК ЗАДАЧ ---\n'
                  '1: Добавить задачу\n'
                  '2: Посмотреть задачу\n'
                  '3: Удалить задачу\n')
            action = int(input('Введите номер операции: '))
            if action == 1:
                todo.add_task(input('Введите задачу: '))
            if action == 2:
                todo.get_task()
            if action == 3:
                todo.del_task(int(input('Введите номер задачи: ')))
        except IndexError:
            print('Неверная операция!')


if __name__ == '__main__':
    main()