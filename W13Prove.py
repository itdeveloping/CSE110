""""
File: ShoppingCart.py
Author: Oscar Rodriguez

Purpose: create a program that stores a list of products in a shopping cart along with their prices.
"""
# Begin of code

class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[0m'
# function to convert Celsius To Fahrenheit
def CelsiusToFahrenheit(Temp):
    Fahrenheit=(Temp*9/5)+32
    return Fahrenheit

# function to get Windchill
def GetWindChill(Temp, WindSpeed):
    WindChill=35.74+0.6215*Temp-35.75*WindSpeed**0.16+0.4275*Temp*WindSpeed**0.16
    return WindChill

#Welcome message
print (f"{bcolors.WARNING}-------------------------------------------")
print (f"{bcolors.OKCYAN}Welcome to the Wind Chill Calculations v1.0! {bcolors.OKBLUE}by Oscar Rodriguez SoftDev")

#Ask the user for information
Temp=float(input(f"\n{bcolors.OKGREEN}What is the temperature?: ")) # Temperature
Degrees=""
while Degrees!="f" and Degrees!="c":
    Degrees=input(f"{bcolors.WARNING}Fahrenheit or Celsius (F/C)?: ").lower() # Fahrenheit or Celsius

if Degrees=="c":
    Temp=CelsiusToFahrenheit(Temp) # use function to convert Celsius to Fahrenheit
    Degrees="F"

for WindSpeed in range(5,65,5):
    WindChill=GetWindChill(Temp,WindSpeed) # use function to get Windchill
    print (f"{bcolors.OKCYAN}At temperature {Temp:.1f}{Degrees.upper()}, and wind speed {WindSpeed} mph, the windchill is: {WindChill:.2f}{Degrees.upper()}")

#Display a final message
print (f"\n{bcolors.WHITE}Thank you for using our system. Goodbye!")
print ("-----------------------------------------")
#end of code