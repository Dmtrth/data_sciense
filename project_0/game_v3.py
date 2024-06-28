import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Игра угадай число
    Компьютер сам загадывает и сам угадывает число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # начальное количество попыток
    low = 0 # начальная нижняя граница поиска
    high = 101 # начальная верхняя граница чисел
    predict_number = (low + high)//2   # задаем начальное значение предсказания
    while number != predict_number:   # цикл с предсказыванием
        count += 1 #  увеличиваем счетчик
        if predict_number > number:    # проверяем условие 1
            high = predict_number    # изменяем верхнюю границу
        elif predict_number < number:    # проверяем условие 2
            low = predict_number      # изменяем нижнюю границу
        predict_number = (low + high)//2   # делаем новое предсказание

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score



if __name__ == "__main__":
    # RUN
    print('Run benchmarking for game_core_v3: ', end='')
    score_game(game_core_v3)
