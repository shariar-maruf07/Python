#function= block of statement that perform a specific task
#function has 2 parts: funciton defination, function call
# def keyword likte hoi erpr functioner name():
#     ekane kaj kam ja hobe likte hbe

def call(): #function ekane defination likha hoise
    print("hello mister !")

call() #ekane call hoise

#sum function

def sum(a,b): #a ar b hoche perameters

    return a+b

print(sum(3,5)) #3,5 hoche arguments


#python e 2 doroner function ase: built-in(print(),input()),user defined

#Lambda Function
#lambda a,b,c: ___expression___

sum= lambda a,b,c: a+b+c

print(sum(2,3,7))
