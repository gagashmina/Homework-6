def validate_input(value):
    # Проверяем, что введенное значение является числом
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_pairwise_comparisons(num_criteria):
    comparisons = []
    for i in range(num_criteria):
        for j in range(i+1, num_criteria):
            while True:
                comparison = input(f"Введите отношение между критерием {i+1} и {j+1} (от 1 до 9): ")
                if validate_input(comparison) and 1 <= float(comparison) <= 9:
                    comparisons.append(float(comparison))
                    break
                else:
                    print("Неправильный ввод. Введите число от 1 до 9.")
    return comparisons

def prod(values):
    result = 1
    for value in values:
        result *= value
    return result

def calculate_weights(comparisons):
    num_criteria = int((2 + (8 * len(comparisons) + 1) ** 0.5) ** 0.5 - 1)
    matrix = [[1] * num_criteria for _ in range(num_criteria)]
    idx = 0
    for i in range(num_criteria):
        for j in range(i+1, num_criteria):
            matrix[i][j] = comparisons[idx]
            matrix[j][i] = 1/comparisons[idx]
            idx += 1
    weights = []
    for column in zip(*matrix):
        column_sum = sum(column)
        column_weights = [value / column_sum for value in column]
        weights.append(prod(column_weights) ** (1 / num_criteria))
    sum_weights = sum(weights)
    norm_weights = [weight / sum_weights for weight in weights]
    return norm_weights

def main():
    # Получаем количество критериев
    while True:
        num_criteria = input("Введите количество критериев: ")
        if validate_input(num_criteria) and int(num_criteria) > 1:
            num_criteria = int(num_criteria)
            break
        else:
            print("Неправильный ввод. Количество критериев должно быть целым числом больше 1.")

        # Получаем сравнения попарно
    comparisons = get_pairwise_comparisons(num_criteria)

    # Вычисляем веса критериев
    weights = calculate_weights(comparisons)

    # Выводим результат
    print(f"Веса критериев: {', '.join([str(weight) for weight in weights])}")

if __name__ == "__main__":
    main()
