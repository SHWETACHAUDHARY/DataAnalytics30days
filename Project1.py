print ("Welcome to my computer quiz")
answer = input("Do you want to play ? Yes or No ")
if answer.lower()!='yes':
    quit()
count =0
answer = input("What does CPU stand for ?")
if answer.lower()=="central processing unit":
    print("Correct !")
    count +=1
else :
    print("Incorrect !")

answer = input("What does RAM stand for ?")
if answer.lower()=="random access memory":
    print("Correct !")
    count +=1
else :
    print("Incorrect !") 
    
answer = input("What does WIFI stand for ?")
if answer.lower()=="wireless fidility":
    print("Correct !")
    count +=1
else :
    print("Incorrect !")
    
print("You have scored "+ str(count)+ " points. ")