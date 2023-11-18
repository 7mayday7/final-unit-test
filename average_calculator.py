"""
Модуль, содержащий класс AverageCalculator для вычисления среднего значения списков чисел.
"""
class AverageCalculator:
    """
    Класс для вычисления среднего значения списка чисел и сравнения средних значений двух списков.
    """
    def calculate_average(self, numbers):
        """
        Вычисляет среднее значение списка чисел.

        :param numbers: Список чисел.
        :return: Среднее значение списка.
        """
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

    def compare_averages(self, list1, list2):
        """
        Сравнивает средние значения двух списков и возвращает соответствующее сообщение.

        :param list1: Первый список чисел.
        :param list2: Второй список чисел.
        :return: Сообщение о сравнении средних значений списков.
        """
        avg1 = self.calculate_average(list1)
        avg2 = self.calculate_average(list2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        if avg2 > avg1:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
