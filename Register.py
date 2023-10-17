register = [ "Maisy", "Catherine", "Aimee", "Shane", "Lily", "Nelly", "Frances", "Aaron", "Ethan"]
found = input("What is the name you want to find in the register? ")
num = 0

for x in register:
    num = num + 1
    print ( str(num) + ": " + x)
    if x==found:
            print(found + "'s Student Number is: " + str(num))
            break
    if x==num:
            print(found + "'s Student Number is: " + str(num))
            break

if x !=found:
    LOOP = 0
    print ("Student could Not be found")
