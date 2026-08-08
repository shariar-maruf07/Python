
#problem 01
print("problem 01")
name=input("Enter your name: ")
age=input("Enter your age: :")

print("Hello "+name+ " your are "+age+" years old")

#problem 02
print("problem 02")

x=int(input("Enter a number X: "))
y=int(input("Enter a number Y: "))

sum=x+y
diff=x-y
prod=x*y
quit=x/y

print("Summation: ",sum, " difference: ",diff ,"product: ",prod, "Quitiont: ",quit)

#problem 03
print("problem 03")

a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=float(input("Enter c :"))

a=float(a)
b=float(b)
avg=(a+b+c)/3
print("Average= ",avg)

#problem 04
print("problem 04")
m=input("Enter m: ")
print("Integer : ",int(m), " Float: ", float(m)," String", m)

#problem 05
print("problem 05")

p = 10 + 3 * 2 ** 2
print("Final Answer: ", p)

#problem 07
print("problem 07")

Celsius=input("Enter Celsius temp: ")

FahrenheitTemp = ((float(Celsius)*(9/5))+32)
print("Fahrenheit Temp: ", FahrenheitTemp)

#problem 08
print("problem 08")

r=float(input("input radius r: "))
area=3.1416*r**r
print("Area is: ",area)

#problem 09
print("problem 09")


d=int(input("Enter d :"))
e=int(input("Enter e :"))
f=float(input("Enter f :"))

d=float(d)
e=float(e)
f=float(f)
per=(d+e+f)/100
print("Percentage= ",per)


#problem 10
print("problem 10")

t=float(input("Enter a number t: "))
integerpart=int(t)
floatpart=t-integerpart

print("Integer part: ",integerpart )
print("Float part: ",floatpart )