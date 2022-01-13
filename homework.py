from dataclasses import dataclass
from typing import List


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        """Метод возвращает строку сообщения"""
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


class Training():
    """Базовый класс тренировки."""

    M_IN_KM: float = 1000
    LEN_STEP: float = 0.65
    MIN_IN_HOUR: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration_h = duration
        self.weight_kg = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration_h

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                           self.duration_h,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""

    COEF_CALORIE_1: int = 18
    COEF_CALORIE_2: int = 20

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        super().__init__(action,
                         duration,
                         weight)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.COEF_CALORIE_1
                * self.get_mean_speed()
                - self.COEF_CALORIE_2)
                * self.weight_kg
                / Training.M_IN_KM
                * self.duration_h
                * self.MIN_IN_HOUR)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    COEF_CALORIE_1: float = 0.035
    COEF_CALORIE_2: int = 2
    COEF_CALORIE_3: float = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        self.height = height
        super().__init__(action,
                         duration,
                         weight)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.COEF_CALORIE_1
                * self.weight_kg
                + (self.get_distance() ** self.COEF_CALORIE_2 // self.height)
                * self.COEF_CALORIE_3
                * self.weight_kg)
                * self.duration_h
                * self.MIN_IN_HOUR)


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38
    COEF_CALORIE_1: float = 1.1
    COEF_CALORIE_2: int = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int
                 ) -> None:
        self.length_pool = length_pool
        self.count_pool = count_pool
        super().__init__(action,
                         duration,
                         weight)

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (self.length_pool
                * self.count_pool
                / Training.M_IN_KM
                / self.duration_h)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.get_mean_speed()
                + self.COEF_CALORIE_1)
                * self.COEF_CALORIE_2
                * self.weight_kg)


def read_package(workout_type: str, data: List[int]) -> Training:
    """Прочитать данные полученные от датчиков."""
    from_code_to_type = {'SWM': Swimming,
                         'RUN': Running,
                         'WLK': SportsWalking}
    if workout_type in from_code_to_type:
        return from_code_to_type[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция. Финальный вывод данных в консоль"""
    info = training.show_training_info()
    print(info.get_message())


"""Имитация получения данных от блока датчиков фитнес-трекера"""
if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
