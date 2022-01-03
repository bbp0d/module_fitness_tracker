class InfoMessage:
    """Информационное сообщение о тренировке."""

    ROUND_NUM = 3

    def __init__(self, 
                 training_type: str,
                 duration: int,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = round(distance, self.ROUND_NUM)
        self.speed = round(speed, self.ROUND_NUM)
        self.calories = round(calories, self.ROUND_NUM)

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type};'
                f'Длительность: {self.duration} ч.;'
                f'Дистанция: {self.distance} км.;'
                f'Ср. скорость: {self.speed} км/ч;'
                f'Потрачено ккал: {self.calories}. ')


class Training:
    """Базовый класс тренировки."""
    
    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65   

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
                               self.LEN_STEP / 
                               self.M_IN_KM)
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

    COEFF_CALORIE_1: int = 18
    COEFF_CALORIE_2: int = 20
    MINUTES_IN_HOUR: int = 60 

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
        get_spent_calories_result = ((self.COEFF_CALORIE_1 * 
                                      get_mean_speed_result - 
                                      self.COEFF_CALORIE_2) * 
                                      self.weight / 
                                      Training.M_IN_KM * 
                                      self.duration * 
                                      self.MINUTES_IN_HOUR)
        return get_spent_calories_result
    
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    COEFF_CALORIE_1: float = 0.035
    COEFF_CALORIE_2: int = 2
    COEFF_CALORIE_3: float = 0.029
    MINUTES_IN_HOUR: int = 60  

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
        get_spent_calories_result = ((self.COEFF_CALORIE_1 * 
                                      self.weight + 
                                      (get_mean_speed_result ** 
                                      self.COEFF_CALORIE_2 //
                                      self.height) * 
                                      self.COEFF_CALORIE_3 * 
                                      self.weight) * 
                                      self.duration *
                                      self.MINUTES_IN_HOUR)
        return get_spent_calories_result 

class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP = 1.38
    COEFF_CALORIE_1 = 1.1
    COEFF_CALORIE_2 = 2

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
                                    self.COEFF_CALORIE_1) * 
                                    self.COEFF_CALORIE_2 * 
                                    self.weight)
        return get_spent_calories_result


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_dict = {'SWM': Swimming,
                     'RUN': Running,
                     'WLK': SportsWalking}

    for key, value in training_dict.items():
        if workout_type == key:
            return value(*data)
      

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

