from display_element_interface import IDisplayElement
from observer_interface import IObserver

class ForecastDisplay(IObserver, IDisplayElement):

    def __init__(self, weather_data, current_pressure=29.92):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.current_pressure = current_pressure

    def update(self, temperature, humidity, pressure):
        self.last_pressure = self.current_pressure
        self.current_pressure = pressure
        self.display()

    def display(self):
        print("Forecast: ")
        if self.current_pressure > self.last_pressure:
            print("Improving weather on the way!")
        elif self.current_pressure == self.last_pressure:
            print("More of the same.")
        else:
            print("Watch out for cooler, rainy weather")
