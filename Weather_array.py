import numpy as np
days = np.arange(1,31)
temp = np.random.uniform(20, 40, 30)
humidity = np.random.uniform(30,90,30)
rainfall = np.random.uniform(0, 20, 30)
weather_data = np.column_stack((days, temp, humidity, rainfall))
print("Weather Data: \n", weather_data)
print("Average Temp :",np.mean(weather_data[:, 1]))
print("Max Temp :", np.max(weather_data[:, 1]))
print("Min Temp :", np.min(weather_data[:, 1]))
print("Average Humidity :", np.mean(weather_data[:, 2]))
print("Average Rainfall :", np.mean(weather_data[:, 3]))
hot_days = weather_data[weather_data[:, 1] > 35, 0]
print("Hot Temp :",hot_days)
rainy_days = weather_data[weather_data[:, 3] > 10, 0]
print("Rainy Data :", rainy_days)