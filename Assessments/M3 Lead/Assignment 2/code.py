import random

# Temperature in Farenheit
def getTemperature():
    temperature = round(random.uniform(20.00,100.00))
    return temperature

# Humidity in range (0.00 to 100.00)
def getHumidity():
    humidity = round(random.uniform(0.00,100.00))
    return humidity
    
currTemperature = getTemperature()

currHumidity = getHumidity()

# Humidity
if(currHumidity > 65):
    print("High Humidity")
    print("Buzzer on")
elif(currHumidity == 65):
    print("Humidity gonna reach maximum")
else:
    print("Humidity is good")
    
# Temperatrue 
if(currTemperature > 86):
    print("High temperature")
    print("Buzzer on")
elif(currTemperature == 86):
    print("Temperature gonna reach maximum")
else:
    print("Temperature is good")