# ID 69341929

def data_input():
    """
    Данные ввода.
    В первой строке дано целое число k
    В четырёх следующих строках задан вид тренажёра – по 4 символа
    в каждой строке.
    """
    k = int(input()) * 2
    matrix = list(''.join([input() for _ in range(4)]))
    return k, matrix

def speed_dial():
    """
    Перебираем матрицу, с помощью счетчика считаем баллы. 
    """
    k, matrix = data_input()
    result = 0

    for index in set(matrix):
        result += 1 if matrix.count(index) <= k and index != '.' else 0
    print(result)

if __name__ == '__main__':
    speed_dial()
