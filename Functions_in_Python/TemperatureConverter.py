print("Temperature Converter")
print("1.Fahrenhiet to Celcius")
print("2.Celcius to Fahrenhiet")
choice=int(input("Please choose a option "))
if choice==1:
    temp=int(input("Please enter the temperature in degree Fahrenheit Scale: "))
    celcius=(temp-32)*5/9
    print("Temperature in celcius is ",celcius)
else:
    temp=int(input("Please enter the temperature in degree Celcius Scale: "))
    Fahren=temp*9/5+32
    print("Temperature in celcius is ",Fahren)

