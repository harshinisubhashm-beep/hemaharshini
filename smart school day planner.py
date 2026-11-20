print("===Smart school day planner ===")
print("Answer 3 quick questions and i will plan yourd day!\n")

day = input("What day is it? (Monday to Sunday):").strip().capitalize()
weather = input("What is the weather? (sunny/rainy/cloudy): ").strip().lower()
homework = input("Is there any homework done? (yes/no): ").strip().lower()

print()
print(f"=== your plan for {day} ===")
print("-" * 35)

if day in ("Saturday", "Sunday"):
    print("Day type     :It's the weekend! Enjoy your day off!")
elif day == "Monday":
        print("Day type   : First day of the week! Time to get back to school.")
elif day == "Friday":
    print("Day type   : Last school day. Return library books today,")
elif day in ("Tuesday","Wednesday","Thursday"):
    print("Day type   : Regular school day. Stay focued!")
else:
    print("Day type   : Day not recognised. Please check the spelling.")        

if weather == "sunny" and homework == "yes":
        print("After school: Head to the park - great weather and homework is done!")

if weather == "rainy" or weather == "cloudy" :
    print("weather tip: Pack your umbrella - it may get wet outside")

if not (homework == "yes"):
 print("Homework   : Not done yet. Finish it before going outside")

if weather == "rainy" and not (homework == "yes"):
        print("Best plan  : Stay in,finish your homework, then watch your favourite shows")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan   : Perfect weekend weather - head outside and have fun!")
else:
    print("Best plan    : Take it one step at a time - you have got this")

    print()
    print("Plan completed! Have a wonderful day!!!")