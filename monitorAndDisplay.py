from sense_hat import SenseHat
import json
import time


class MonitorAndDisplay:

    def __init__(self):
        self.sense_hat = SenseHat()

        with open('config.json') as file:
            self.config_data = json.load(file)

    def display_temp(self,temp):
        if temp < self.config_data["cold_max"]:
            self.sense_hat.show_message(str(temp), text_colour = MonitorAndDisplay.blue)
        elif temp in range(self.config_data["comfortable_min"], self.config_data["comfortable_max"]):
            self.sense_hat.show_message(str(temp), text_colour = MonitorAndDisplay.green)
        else:
            self.sense_hat.show_message(str(temp), text_colour = MonitorAndDisplay.red)

    def get_temp(self):
        return int(round(self.sense_hat.get_temperature()))

    def current_temp(self,interval_to_check):
        old_time = time.time()
        temp = self.get_temp()

        while True:
            if time.time() - old_time > interval_to_check:
                old_time = time.time()
                temp = self.get_temp()
            self.display_temp(temp)


    blue = (0, 0, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)



MonitorAndDisplay().current_temp(10)




 



    
