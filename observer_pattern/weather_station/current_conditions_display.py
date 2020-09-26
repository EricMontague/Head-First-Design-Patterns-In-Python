from display_element_interface import IDisplayElement
from observer_interface import IObserver


class CurrentConditionsDisplay(IObserver, IDisplayElement):

    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature} F degrees and humidity {self.humidity}")