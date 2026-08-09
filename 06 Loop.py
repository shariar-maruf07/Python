#for loop,while loop er basic

#infinite loop
# while True:
#     print("Hi boss!")

#1-10 porjonto print korabo while loop dia
i=1
while i<=10:
    print(i)
    i+=1

print("After loop i= ", i)
# loop seshe i er man 11 hye jabe jar karone condition true hbe na, so loop teke ber hye jabe

#break ar continue 
print("for break: ")
i=1
while i<=10:
    if(i%6==0):
        break #break use korle loop teke ber hye jabe
    print(i)
    i+=1

# output: 1 2 3 4 5
print("for continue: ")
i=1
while i<=10:
    if(i%2 == 0): 
        i+=1
        continue #continue means Skip the rest of this iteration and go to the next iteration.
    print(i)
    i+=1

# output: 1 3 5 7 9

#for loop sequential traversal er jnno use kori

string="Maruf bro"

for x in string: #traverse er jnno for _variable_ in _string ta__
    print(x)
    
# in= membership operator (prsensece check korar jnno use kore hoi)

if 'f' in string:
    print("Exists ")
else:
    print("invalid")
    
#range function 
# range(n) mane 0 teke n-1 porjonto jabe
# range(start,stop,step) by default stop value ta take
# example: range(1,6,2) output= 1,3,5

n=int(input("Enter the value n= "))
for i in range(n):
    print(i)
    
