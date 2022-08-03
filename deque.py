# ID 69444191
class Deque:
    """ Создаем двустороннюю очередь."""

    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 1
        self.tail = 0
        self.size = 0

    def is_empty(self):
        """ Проверка пустоты очереди. """
        return self.size == 0

    def is_full(self):
        """ Проверка переполнения очереди. """
        return self.size == self.max_size

    def push_front(self, value):
        """ Добавить элемент в начало дека. """
        if self.is_full():
            raise AttributeError
        self.head = (self.head - 1) % self.max_size
        self.queue[self.head] = value
        self.size += 1

    def push_back(self, value):
        """ Добавить элемент в конец дека. """
        if self.is_full():
            raise AttributeError
        self.tail = (self.tail + 1) % self.max_size
        self.queue[self.tail] = value
        self.size += 1

    def pop_front(self):
        """ Вывести первый элемент дека и удалить его."""
        if self.is_empty():
            raise AttributeError
        value = self.queue[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return value

    def pop_back(self):
        """ Вывести последний элемент дека и удалить его."""
        if self.is_empty():
            raise AttributeError
        value = self.queue[self.tail]
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return value


def main():
    """ Ввод данных и проверка результата."""
    commands_count = int(input())
    queue_size = Deque(max_size=int(input()))
    COMMANDS = {
        'push_front': queue_size.push_front,
        'push_back': queue_size.push_back,
        'pop_front': queue_size.pop_front,
        'pop_back': queue_size.pop_back,
    }
    for _ in range(commands_count):
        command, *params = input().split()
        try:
            result = COMMANDS[command](*params)
            if result:
                print(result)
        except AttributeError:
            print('error')


if __name__ == '__main__':
    main()
