class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""
    
    M_IN_KM = 1000
    LEN_STEP = 0.65   

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        


    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        get_distance_result = (self.action * 
                              Training.LEN_STEP / 
                              Training.M_IN_KM)
        return  get_distance_result


    def get_mean_speed(self, get_distance_result) -> float:
        """Получить среднюю скорость движения."""
        get_mean_speed_result = get_distance_result / self.duration
        return get_mean_speed_result

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""

    coeff_calorie_1 = 18
    coeff_calorie_2 = 20 

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        super().__init__(action,
                         duration,
                         weight)

    def get_spent_calories(self, get_mean_speed_result) -> float:
        """Получить количество затраченных калорий."""
        get_spent_calories_result = ((Running.coeff_calorie_1 * 
                                      get_mean_speed_result - 
                                      Running.coeff_calorie_2) * 
                                      self.weight / 
                                      Training.M_IN_KM * self.duration) 
        return get_spent_calories_result
    
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    coeff_calorie_1 = 0.035
    coeff_calorie_2 = 2
    coeff_calorie_3 = 0.029 

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
    def get_spent_calories(self, get_mean_speed_result) -> float:
        """Получить количество затраченных калорий."""
        get_spent_calories_result = ((SportsWalking.coeff_calorie_1 * 
                                      self.weight + 
                                      (get_mean_speed_result ** 
                                      SportsWalking.coeff_calorie_2 //
                                      self.height) * 
                                      SportsWalking.coeff_calorie_3 * 
                                      self.weight) * 
                                      self.duration)
        return get_spent_calories_result 

class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP = 1.38
    coeff_calorie_1 = 1.1
    coeff_calorie_2 = 2

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
        get_mean_speed_result = (self.length_pool * 
                                 self.count_pool / 
                                 Training.M_IN_KM / 
                                 self.duration)
        return get_mean_speed_result

    def get_spent_calories(self, get_mean_speed_result) -> float:
        """Получить количество затраченных калорий."""
        get_spent_calories_result = ((get_mean_speed_result + 
                                    Swimming.coeff_calorie_1) * 
                                    Swimming.coeff_calorie_2 * 
                                    self.weight)
        return get_spent_calories_result


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

