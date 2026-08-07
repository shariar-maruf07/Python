#type casting in python

name= input("Enter your name:")
print(type(name))
age= input("Enter your age:")
print("before type casting", type(age))

#initially age is string type, but we can convert it into integer type using int() function

age= int(age) #amra age ke integer type e convert korechi, jate amra age er upor mathematicaloperation korte pari.
print("after type casting ", type(age))
print("5 bochor por age: ", age+5)

age= float(age) #float e convert kora holo
print(age)

#same amra bool() ar str() eo covert krte prbo

#type conversion krtesi ekn (jeta python nij teke kore)

print(2+3.4) #implicit type conversion
print(2+int(3.4)) #explicit type conversion

