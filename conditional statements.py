temperature = int(input("Enter today's temperature in Celsius: "))

if temperature < 20:
    outfit = "jacket"
    print("It is cold today.")
    print("Wear a" , outfit)
else:
        outfit = "t-shirt"
        print("It is warm today")
        print("Wear a", outfit)

is_raining = input("Is it raining today? (yes/no): ")


if is_raining == "yes":
    print("Bring an umbrella")

wind_speed = int(input("Enter the wind speed in km/h:"))

if wind_speed > 30:
    needs_windbreaker = "Yes"
    print("It is calm today.")
    print("No windbraeker needed over your" , outfit)
else:
        needs_windbreaker = "No"
        print("It is calm today.")
        print("No windbreaker needed over your" , outfit)

has_puddles = input("Are there puddles on the ground? (yes/no):")

if has_puddles == "yes":
        shoes = "boots"
        print("The ground is wet")
        print("Wear" , shoes)
else:
            shoes = "sneakers"
            print("The ground is dry")
            print("wear" , shoes)

print("")
print("Weather check complete!")

print("==== WEATHER OUTFIT PICKER ====")
print("Temperature:", temperature)
print("Outfit chosen:", outfit)
print("Raining:", is_raining)
print("Windreaker needed:", needs_windbreaker)
print("Shoes chosen:", shoes)
