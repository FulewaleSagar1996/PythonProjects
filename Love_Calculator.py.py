print("Helllo world")
print("Welcome to the love calculator ")
name1 = input("what is your name? \n")
name2 = input("what is your their name? \n")
combined_stringlower = name1 + name2
combined_string = combined_stringlower.lower()
t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e") 

true = t+r+u+e

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e") 

love = l+o+v+e

lovescore = int(str(true) + str(love))

if (lovescore<10) or (lovescore>90):
  print(f"your score is {lovescore},you go together like coke and mentos")
elif(lovescore>=40)and(lovescore<=50):
  print(f"your score is {lovescore},you are alright toghether")
else:
  print(f"your score is {lovescore}")
  