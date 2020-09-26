from observer_interface import IObserver
from display_element_interface import IDisplayElement

class HeatIndexDisplay(IObserver, IDisplayElement):

    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperate, humidity, pressure):
        self.heat_index = self._compute_heat_index(temperate, humidity)
        self.display()

    def display(self):
        print(f"Heat Index is: {self.heat_index}")

    def _compute_heat_index(self, temperature, humidity):
        heat_index = (float)((16.923 + (0.185212 * temperature) + (5.37941 * humidity) - (0.100254 * temperature * humidity) 
			+ (0.00941695 * (temperature * temperature)) + (0.00728898 * (humidity * humidity)) 
			+ (0.000345372 * (temperature * temperature * humidity)) - (0.000814971 * (temperature * humidity * humidity)) +
			(0.0000102102 * (temperature * temperature * humidity * humidity)) - (0.000038646 * (temperature * temperature * temperature)) + (0.0000291583 * 
			(humidity * humidity * humidity)) + (0.00000142721 * (temperature * temperature * temperature * humidity)) + 
			(0.000000197483 * (temperature * humidity * humidity * humidity)) - (0.0000000218429 * (temperature* temperature * temperature * humidity * humidity)) +
			0.000000000843296 * (temperature * temperature * humidity * humidity * humidity)) -
			(0.0000000000481975 * (temperature * temperature * temperature * humidity * humidity * humidity)))
        return round(heat_index, 2)
        