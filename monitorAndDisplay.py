from sense_hat import SenseHat
import json
import time


class MonitorAndDisplay:

    def __init__(self, sense_hat):
        self.sense_hat = sense_hat

        with open('config.json') as file:
            self.config_data = json.load(file)

    def read_temp(self):
        temp = int(round(self.sense_hat.get_temperature())) 
        while True:
            if temp < self.config_data["cold_max"]:
                self.sense_hat.show_message(str(temp), text_colour = self.blue)
            elif temp in range(self.config_data["comfortable_min"], self.config_data["comfortable_max"]):
                self.sense_hat.show_message(str(temp), text_colour = self.green)
            else:
                self.sense_hat.show_message(str(temp),text_colour = self.red)

    def check_temp(self):
        while True:
            self.read_temp()
            time.sleep(10)



    blue = (0, 0, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)






sense = SenseHat()

sense.clear()

mon = MonitorAndDisplay(sense)

mon.check_temp()


 



    
    
