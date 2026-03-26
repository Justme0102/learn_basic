user_correct = "brayan"
password_correct = "123123"
attempts = 0
max_attempst = 3 

while attempts < max_attempst:
    user = input("enter your user: ")
    password = input ("enter your password: ")
    
    if user == user_correct and password == password_correct:
        print (f"hello {user_correct} all good ")
        break
    else:
        attempts += 1 
        print (f"incorrect try againt attemtps left:{max_attempst - attempts}")
      
if attempts == max_attempst:
    print("too many attempts")
print("end of program")
