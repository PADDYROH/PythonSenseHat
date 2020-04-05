from sense_hat import SenseHat
import json
import os
import time


class MonitorAndDisplay:

    def __init__(self):
        self.sense_hat = SenseHat()

        # here we check if the json file is in a correct format exception is thrown otherwise
        self.config_data = self.check_json('config.json')

    def display_temp(self,temp):
        if temp < self.config_data["cold_max"]:
            self.sense_hat.show_message(str(temp), text_colour = MonitorAndDisplay.blue)
        elif temp in range(self.config_data["comfortable_min"], self.config_data["comfortable_max"]):
            self.sense_hat.show_message(str(temp), text_colour = MonitorAndDisplay.green)
        elif temp > self.config_data["hot_min"]:
            self.sense_hat.show_message(str(temp), text_colour = MonitorAndDisplay.red)

    def check_json (self,json_file):

        incorrect_file = False
        cold_max = "cold_max"
        comfortable_min = "comfortable_min"
        comfortable_max = "comfortable_max"
        hot_min = "hot_min"

        with open(json_file) as file:
            config_data = json.load(file)

        #check if the json file is not empty
        if os.stat(json_file).st_size == 0:
            incorrect_file = True

        # check if we can obtain the valid figures 
        if cold_max not in config_data:
            incorrect_file = True
        if comfortable_min not in config_data:
            incorrect_file = True
        if comfortable_max  not in config_data:
            incorrect_file = True
        if  hot_min not in config_data:
            incorrect_file = True  

        if incorrect_file:
            raise Exception('json file is incorrect')

        else:
            return config_data


    def get_temp(self):
        cpu_temp = self.get_cpu_temp()
        temp_hum = self.sense_hat.get_temperature_from_humidity()
        temp_press = self.sense_hat.get_temperature_from_pressure()

        #get a median temperature 
        temp = (temp_hum + temp_press) / 2
        #remove cpu temp for better room temperature reading
        calibrated_temp = temp - ((cpu_temp - temp) / 1.5)

        return int(round(calibrated_temp))

    def current_temp(self,interval_to_check):
        self.display_temp(self.get_temp())

        old_time = time.time()
        temp = self.get_temp()

        while True:
            #if the current time is greater then the interval to check (10 seconds)
            if time.time() - old_time > interval_to_check:
                old_time = time.time()
                self.display_temp(self.get_temp())


    # Get CPU temperature.
    def get_cpu_temp(self):
        res = os.popen("vcgencmd measure_temp").readline()
        return float(res.replace("temp=","").replace("'C\n",""))


    blue = (0, 0, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)



MonitorAndDisplay().current_temp(10)
