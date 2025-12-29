
zeroCelcius = 273.5  # zero degree Celcius in Kelvin

def convert_celcius_to_kelvin(temperatureC):
    return temperatureC + zeroCelcius

def convert_kelvin_to_celcius(temperatureK):
    return temperatureK - zeroCelcius

if __name__ == '__main__':
    print (convert_celcius_to_kelvin(15.7))
    print (convert_kelvin_to_celcius(302.9))
