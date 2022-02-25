
import random
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
'U','V','W','X','Y','Z', 'a','b', 'c', 'd',	'e'	,'f','g','h',
'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']	
number = ['0', '1', '2', '3', '4', '5,' '6', '7', '8','9' ]
symbol = ['!', '@' ,'#', '$' ,'%', '^', '&' ,'*','(', ')', '+', '-' ]
print("Welcome to the Password generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbol = int(input("How many symbols would you like ?\n"))
nr_number = int(input("How many numbers would you like ?\n"))
#simpl level
# password = ""
# for char in range (1,nr_letters+1):
#  password +=  random.choice(letters)
   
# for char in range (1,nr_symbol+1):
#  password +=  random.choice(symbol)
    
# for char in range (1,nr_number+1):
#  password +=  random.choice(number)

# print(password)

#hard logic

password_list = []
for char in range (1,nr_letters+1):
 password_list.append(random.choice(letters))
   
for char in range (1,nr_symbol+1):
 password_list +=  random.choice(symbol)
    
for char in range (1,nr_number+1):
 password_list +=  random.choice(number)

# print(password_list)
random.shuffle(password_list)
# print(password_list) 

password = ""
for char in password_list:
 password += char

print(f"your password is :{password}")
