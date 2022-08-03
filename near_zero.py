# ID 69336449

def data_input():
    """
    В первой строке дана длина улицы —– n. 
    В следующей строке записаны n целых неотрицательных чисел — номера домов
    и обозначения пустых участков на карте.
    """
    street = input()
    houses = input().split()
    return street, houses


def near_zero():
    """Создаем список и заполняем нулями."""
    street, houses = data_input()
    distance = [0]*len(houses)
    zeros = [index for index, house in enumerate(houses) if house == '0']

    """Цикл до первого нуля."""
    for i in range(zeros[0]):
        distance[i] = zeros[0] - i

    """Цикл для пар нулевых."""
    for k in range(1, len(zeros)):
        for i in range(zeros[k-1] + 1, zeros[k]):
            distance[i] = min(i - zeros[k-1], zeros[k] - i)

    """Цикл после последнего нуля."""
    for i in range(zeros[-1] + 1, len(houses)):
        distance[i] = i - zeros[-1]
    print(*distance)


if __name__ == "__main__":
    near_zero()
