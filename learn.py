import numpy as np

# Функция для ввода данных попарного сравнения критериев
def input_comparison_matrix(num_criteria):
    comparison_matrix = np.zeros((num_criteria, num_criteria))
    
    for i in range(num_criteria):
        for j in range(i+1, num_criteria):
            comparison_value = float(input(f"Введите отношение важности критерия {i+1} к критерию {j+1}: "))
            reciprocal_value = 1 / comparison_value
            comparison_matrix[i][j] = comparison_value
            comparison_matrix[j][i] = reciprocal_value
    
    return comparison_matrix

# Функция для вычисления весовых коэффициентов
def calculate_weights(comparison_matrix):
    num_criteria = len(comparison_matrix)
    weights = np.prod(comparison_matrix, axis=1) ** (1 / num_criteria)
    weights /= np.sum(weights)
    return weights

if __name__ == "__main__":
    num_criteria = int(input("Введите количество критериев: "))
    comparison_matrix = input_comparison_matrix(num_criteria)
    weights = calculate_weights(comparison_matrix)
    
    # Вывод весовых коэффициентов
    for i, weight in enumerate(weights):
        print(f"Вес критерия {i+1}: {weight:.2f}")