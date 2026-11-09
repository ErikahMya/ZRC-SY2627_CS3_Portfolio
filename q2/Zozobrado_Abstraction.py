from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_ready(self, pH, Temperature):
        pass

class PHsensor(Sensor):
    def get_ready(self, pH,):
        print(f"[pH sensor] Reading: {pH} (neutral)")

class TempSensor(Sensor):
    def get_ready(self,Temperature):
        print(f"[Temperature sensor] Reading: {Temperature}")

pH_sensor = PHsensor()
temp_sensor = TempSensor()

print ("--- Lab Inventory System ---")

pH_sensor.get_ready("7.2 pH")
temp_sensor.get_ready('24.5°C') 

print ("-----------------------------")