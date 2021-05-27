# Add Celsius class implementation below.
class Celsius:
    def __get__(self,instance,owner):
        return 5 * (instance.fahrenheit-32)/9
    def __set__(self,instance,value):
        instance.fahrenheit=32+9 * value/5

# Add temperature class implementation below.
class Temperature:
    celsius = Celsius()
    def __init__(self,temp):
        self.fahrenheit=temp
          
