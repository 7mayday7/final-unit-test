import pytest
from average_calculator import AverageCalculator

def test_calculate_average_empty_list():
    calculator = AverageCalculator()
    assert calculator.calculate_average([]) == 0

def test_calculate_average_positive_numbers():
    calculator = AverageCalculator()
    assert calculator.calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_calculate_average_negative_numbers():
    calculator = AverageCalculator()
    assert calculator.calculate_average([-1, -2, -3, -4, -5]) == -3.0

def test_compare_averages_empty_lists():
    calculator = AverageCalculator()
    assert calculator.compare_averages([], []) == "Средние значения равны"

def test_compare_averages_first_list_greater():
    calculator = AverageCalculator()
    assert calculator.compare_averages([5, 10, 15], [2, 4, 6]) == "Первый список имеет большее среднее значение"

def test_compare_averages_second_list_greater():
    calculator = AverageCalculator()
    assert calculator.compare_averages([2, 4, 6], [5, 10, 15]) == "Второй список имеет большее среднее значение"

def test_compare_averages_lists_with_same_average():
    calculator = AverageCalculator()
    assert calculator.compare_averages([1, 2, 3], [4, 2, 1]) == "Средние значения равны"
