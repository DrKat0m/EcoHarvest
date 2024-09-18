from Climate2 import *
import random
import numpy as np
from humidity import *
from Predict import *
from sort_by_price import *
from CropRotation import *
from LLM_REC import*


def Ph_of_soil():
    return random.choice(np.arange(4.5, 8.5, 0.007)) 

def main(lat, lang):
    temperature, precipitation = collect_weather(lat, lang)
    Ph =  Ph_of_soil()
    humidity = get_humidity(lat, lang)
    commodities = predict_crop(temperature, humidity, Ph, precipitation)
    print(commodities)
    prices = control(lat, lang, commodities)
    print(prices)
    keys = list(prices.keys())
    values = list(prices.values())
    sorted_value_index = np.argsort(values)
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
    print(sorted_dict)

    output_json = {}
    output_json["rotationTxt"] = main_rotation(list(sorted_dict.keys()))
    print(output_json["rotationTxt"])
    add_data = main_howto(sorted_dict)
    print(add_data)
    output_json["cropSpecific"] = add_data

    return output_json

if __name__ == '__main__':
    (main(33.44193097647909, -112.07110698105588))