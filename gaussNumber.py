#gussing the number
#rnadom => (a,b) 
# loop => condition => guss_count => feedback => guss_count => feeback
import random
import sys

try:
    low = int(input("Enter the low number:\n "))
    high = int(input("Enter the high number:\n "))
except:
    print("Please enter a valid number")
    sys.exit()   # توقف برنامه
    
r = random.randint(low,high)

guss_count = 5

while guss_count > 0:
    try:
        new_guss_str = input(f'remain guss count: {guss_count} => Enter your guss:\n ')
        new_guss = int(new_guss_str)
        
        if new_guss == r:
            print("Congratulations! You gussed the number.")
            break
        elif new_guss < r:
            print("Your guss is too low.")
        else:
            print("Your guss is too high.")
        guss_count -= 1
    except:
        print("Please enter a valid number")
if guss_count == 0:
    print(f"Sorry, you have used all your gusses. The number was {r}.")



   


