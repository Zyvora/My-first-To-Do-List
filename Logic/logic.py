class ToDoList:
    def __init__(self):
        self.__task = []

    def add_task(self, task):
        self.__task.append(task)

    def get_task(self):
        if len(self.__task) == 0:
            print('Нет задач')
        for i, task in enumerate(self.__task, 1):
            print(f'{i}: "{task}"')

    def del_task(self, index):
        try:
            del self.__task[index - 1]
        except IndexError:
            print('задача не найдена')

    def mark_task(self):
        pass

