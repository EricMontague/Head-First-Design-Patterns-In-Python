from display_element_interface import IDisplayElement
from observer_interface import IObserver


class StatisticsDisplay(IObserver, IDisplayElement):
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.num_readings = 0
        self.temperature_sum = 0
        self.max_temperature = float("-inf")
        self.min_temperature = float("inf")

    def update(self, temperature, humidity, pressure):
        self.temperature_sum += temperature
        self.num_readings += 1
        self.max_temperature = max(self.max_temperature, temperature)
        self.min_temperature = min(self.min_temperature, temperature)
        self.display()

    def display(self):
        print(
            f"""
        Avg/Max/Min temperatures: 
        {self.temperature_sum / self.num_readings} / {self.max_temperature} / {self.min_temperature}
            """
        )

