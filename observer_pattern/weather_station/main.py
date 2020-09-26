from weather_data import WeatherData
from current_conditions_display import CurrentConditionsDisplay
from heat_index_display import HeatIndexDisplay
from forecast_display import ForecastDisplay
from statistics_display import StatisticsDisplay

def main():
    # subject
    weather_data = WeatherData()

    # observers
    current_display = CurrentConditionsDisplay(weather_data)
    heat_index_display = HeatIndexDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)
    stats_display = StatisticsDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)


if __name__ == "__main__":
    main()