import random
import math

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

# pass_len=random.randint(8,13) #without User input

password_length = int(input("Enter Password Length: "))

# length of password by 50-30-20 formula
alpha_length = password_length//2
num_length = math.ceil(password_length*30/100)
special_length = password_length-(alpha_length+num_length)

password = []

#generate password function
def generate_password(length,array,isAlpha = False):
    for i in range(length):
        index = random.randint(0, len(array)-1)
        character = array[index]

        if isAlpha:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        
        password.append(character)

# alpha password
generate_password(alpha_length, alpha, True)

# numeric password
generate_password(num_length, num)

# special Character password
generate_password(special_length, special)

# suffle the generated password list
random.shuffle(password)

# convert List To string
gen_password = ""

for i in password:
    gen_password = gen_password + str(i)
print(gen_password)
