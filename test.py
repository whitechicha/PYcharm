todos=open('todos','a')
print("Первая строка",file=todos)
print("Вторая строка",file=todos)
todos.close()

task = open('todos.txt')
for str in task:
    print(str,end='')
    task.close()

    with open("todos.txt") as task:
        for str in task:
            print(str, end="")
            print("тут файл уже закрыт")
