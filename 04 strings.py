#string operaton

name= "Shariar Maruf"
grade= 'A'

#string length ber krte
print("String length", len(name))

#upper case and lower case
print("uppercase: " ,name.upper()) #upper case e convert korbe
print("lowercase: " ,grade.lower()) #lower case e convert korbe

#find
print("Find 'iar': ", name.find("iar")) #index print krbe jekan teke pabe ar na paile -1 print krbe
print("Find 'x': ", name.find("x")) 

#replace
print("Replace 'Maruf' with 'Habib': ", name.replace("Maruf", "Habib"))
print("Replace 'Sh' with 'Saha': ", name.replace("Sh","Saha"))

#check for presence
print("Check 'aru' is in name: ", "aru" in name) #True or False return korbe
print("Check 'khan' is in name: ", "khan" in name)

print("Now the main string: ", name)

#concatenate
word1="i love"
word2="you"
print(word1+" "+word2)

#prottek charecter k print korabo
for x in word2:
    print(x)
    
#slicing
print(name[2:8]) #substring print koraite hole ___string___[starting index(def=0):ending index(def=str length)]

#string formating
a=5
b=10
print(f"the sum of {a} and {b} is {a+b}") #ebhabe f dia string er modde likha jabe alada krte hbe na

#string er khetre amra string e joto kisoi na kori seta main string ke change korbe na tobe seta ekta noton string banabe. karon string immutable.

