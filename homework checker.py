math_time = int(input("Enter the time you spend on your Math homework (in minutes): "))
if math_time < 30:
    maximum_time = "60 minutes"
    print("You spent less than 30 minutes on Math")
    print("Try spending upto", maximum_time)
else:
    print("You spent more than 30 minutes on your Math homework")
    print("Good job! Keep up the good work")

science_time = int(input("Enter the time you spend on your Science homework (in minutes): "))
if science_time < 25:
    maximum_time = "45 minutes"
    print("You spent less than 25 minutes on Science")
    print("Try spending atleast", maximum_time)
else:
    print("You spent more than 25 minutes on your Science homework")
    print("Good job! Keep up the good work")

english_time = int(input("Enter the time you spend on your English homework (in minutes): "))
if english_time < 20:
    maximum_time = "30 minutes"
    print("You spent less than 20 minutes on English")
    print("Try spending atleast", maximum_time)
else:
    print("You spent more than 20 minutes on your English homework")
    print("Good job! Keep up the good work")

social_time = int(input("Enter the time you spend on your Social Studies homework (in minutes): "))
if social_time < 20:
    maximum_time = "30 minutes"
    print("You spent less than 20 minutes on Social Studies")
    print("Try spending atleast", maximum_time)
else:
    print("You spent more than 20 minutes on your Social Studies homework")
    print("Good job! Keep up the good work")

print("")
print("Your daily homework time management check is completed")

print("==== DAILY HOMEWORK TIME CHECK ====")
print("Math homework time:", math_time)
print("Science homework time:", science_time)
print("English homework time:", english_time)
print("Social Studies homework time:", social_time)
