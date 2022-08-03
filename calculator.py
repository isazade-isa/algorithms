# ID 69444286
class Stack:
    """Создание стэка."""

    def __init__(self):
        """Создание пустого массива."""
        self.__data = []

    def is_not_empty(self):
        """Проверка пустоты массива."""
        return len(self.__data) != 0

    def push(self, elem):
        """Добавление элемента на вершину стэка."""
        self.__data.append(elem)

    def pop(self):
        """Возвращает элемент с вершины стэка и удаляет его."""
        if self.is_not_empty():
            return self.__data.pop()


def calc(data):
    """Ввод данных и вычисления."""
    OPERATORS = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: y-x,
        '*': lambda x, y: x*y,
        '/': lambda x, y: y//x
    }
    operands = Stack()
    for value in data.split():
        if value in OPERATORS:
            operands.push(OPERATORS[value](operands.pop(), operands.pop()))
        else:
            operands.push(int(value))
    return operands.pop()


print(calc(input()))
