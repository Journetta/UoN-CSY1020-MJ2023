register = ["Maisy", "Aimee", "Catherine", "Shane", "Lily", "Nelly", "Frances", "Aaron", "Ethan"]
found = input("What is the name you want to find in the register? ")
num = 1

for x in register:
        print ( str(num) + ": " + x)
        num = num+1
        if x==found:
                 break