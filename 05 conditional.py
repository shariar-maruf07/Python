# if,elif,else

#voter or not testing
age=int(input("Enter Your Age: "))

if (age>=18) :
    print("You can vote")
else :
    print("Invalid voter")
    
#traffic light 

colour=input("Enter colour name: ")

if colour=="green":
    print("Go")
elif colour=="yellow": #elseif er poriborte elif use kora hoi python e
    print("Look")
elif colour=="red":
    print("Stop")
else:
    print("color not matched")


#password checking

id=input("Enter your id: ")
password=input("Enter your password: ")

if (id=="c251094" and password=="1920"):
   print("Login successfull ")
elif(id!="c251094"):
    print("Invalid Id")
else:
    print("wrong password")

# nesting korte caile same code k 
# else:
#     if(id!="c251094"):
#         print("Invalid Id")
#     else:
#         print("Wrong password")


#match case:

color=input("Enter colour(match case) name: ")

match color:
    case "green":
        print("Go")
    case "yellow":
        print("Look")
    case "red":
        print("Stop")
    case _:             #default case er jnno ebhabe likte hoi
        print("Not matched")