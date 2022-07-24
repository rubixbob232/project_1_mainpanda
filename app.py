print("Welcome to My Computer Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
answer = input("What country has the best air force in the world? ")
if answer == "United States of America":
    print("Correct!")
    score += 1
else:
     print("Incorrect! It's where you live goofy."  )

answer = input("What small island is south of Turkey? ")
if answer == "Cyprus":
    print("Correct!")
    score += 1
else:
    print("Incorrect! It was Cyprus. ")

answer = input("What country is Mount Everest located in? ")
if answer == "Nepal":
    print("Correct!")
    score += 1
else:
     print("Incorrect! It was Nepal. ")

answer = input("What island use to be apart of China and still have conflict today? ")
if answer == "Taiwan":
         print("Correct! ")
         score += 1
else:
         print("Incorrect! It was Taiwan. ")

answer = input("Which snow owns snowy? ")
if answer == "dbnsnow":
    print("Correct!")
    score += 1
else:
     print("Incorrect! It was dbnsnow.")

answer = input("What fast food has more customers? Burger King or Mcdonalds? ")
if answer == "Mcdonalds":
    print("Correct!")
    score += 1
else:
    print("Incorrect! It was Mcdonalds.")


answer = input("What do we classify people who complain? ")
if answer == "Karens":
    print("Correct!")
    score += 1
else:
    print("Incorrect! It was Karens. ")

answer = input("Who is the best Football Fusion player of all time? ")
if answer == "MainPanda700":
    print("Correct!")
    score += 1
else:
    print("Incorrect! It's MainPanda700! ")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 8) * 100) + "%.")

