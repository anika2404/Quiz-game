print ("***************************")
print ("Welcome to my computer quiz!")
print ("***************************")
playing=input("Do you want to Play? ")

if playing.lower() != "yes" :
    quit()

print("Okay! Lets play :) ")
score=0

rules='''
 HERE ARE SOME RULES :)

 1 positive point is awarded for correct answer 
               and
1 point is deducted for wrong answer 
'''

print(rules)


answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score+=1
else:
    print("Incorrect!")
    score-=1

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score+=1
else:
    print("Incorrect!")
    score-=1

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score+=1
else:
    print("Incorrect!")
    score-=1

answer = input("what does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("correct!")
    score+=1
else:
    print("Incorrect!")
    score-=1

print("You got " + str(score) + " points in the game!")
print("You got " + str((score/4)*100) + " % ")