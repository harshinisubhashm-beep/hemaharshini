print("==============================================================")
print("                   Welcome to ride builder                    ")
print("==============================================================")
print()

print("Step 1: Pick your vechile")
print(" 1 - Bike")
print(" 2 - car")
print()

choice = int(input("Enter 1 or 2:"))
print()

if choice == 1:
    print("Step 2: Pick your bike type")
    print(" 1 - Scooty")
    print(" 2 - Mountain Bike")
    print()

    bike_type = int(input("Enter 1 or 2:"))
    print()

    if bike_type == 1:
      print("You picked  : Scooty")
      print("You picked  : 80 km/hr")
      print("Best for    : City roads")
    else:
      print("You picked  : Mountain bike")
      print("Top speed   : 90 km/hr")
      print("Best for    : Mountain riding")

elif choice == 2:

     print("Step 2: Pick your car type")
     print(" 1 - seden")
     print(" 2 - suv")
     print()

     car_type = int(input("Enter 1 or 2:"))
     print()

     if car_type -- 1:
         print("You picked  : Seden")
         print("Seets       : 5 passengers")
         print("Best for     : Family trips")

     car_type = int(input("Enter 1 or 2:"))
     print()

     if car_type == 1:
           print("You picked  : Seden")
           print("Seats       : 5 seats")
           print("Best for    : Family trip")
     else:
           print("You picked  : SUV")
           print("Seats       : 7 Passengers")
           print("Best for    : off-road adventures")

else:
    print(("That was not a valid choice"))
    print("please enter 1 for bike or 2 for car")

print()
print("=======================")
print("  your custom ride is ready")
print("  Enjoy your ride")
print("===============")       