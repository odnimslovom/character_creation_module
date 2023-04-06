from math import sqrt

message: str = (
    'Добро пожаловать в самую лучшую программу для вычисления '
    'квадратного корня из заданного числа')

print(message)


def calculate_square_root(number) -> float:
    """Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number) -> None:
    """Печатает результат вычисления квадратного корня"""
    root: float = 0.0
    if your_number <= 0:
        return root
    root = calculate_square_root(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа.'
          f'Это будет: {root}')
    return root


print(message)
calc(25.5)
