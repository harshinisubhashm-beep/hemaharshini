name = input("Enter your real name,student;")
house = input("Enter your house name: ")

no_of_cabinet_members = 3
number_of_achievements = 5
no_of_students = 30
is_active = True

print("Name:", name, "-> type:", type(name))
print("House:", house, "-> type:", type(house))
print("No. of Cabinet Members:", no_of_cabinet_members, "-> type:", type(no_of_cabinet_members))
print("No. of Achievements:", number_of_achievements, "-> type:", type(number_of_achievements))
print("No. of Students:", no_of_students, "-> type:", type(no_of_students))
print("Is Active:", is_active, "-> type:", type(is_active))

number_of_cabinet_members_text = str(no_of_cabinet_members)
number_of_achievements_text = str(number_of_achievements)
number_of_students_text = str(no_of_students)
is_active_text = str(is_active)
print("No. of Cabinet Members as text:", number_of_cabinet_members_text, " -> type:",
type(number_of_cabinet_members_text))
print("No. of Achievements as text:", number_of_achievements_text, " -> type:",
type(number_of_achievements_text))
print("No. of Students as text:", number_of_students_text, " -> type:",
type(number_of_students_text))
print("Is Active as text:", is_active_text, " -> type:",
type(is_active_text))

first_three = house[0:3]
last_letter = house[-1:]
print("First 3 letters of house:", first_three)
print("Last letter of house:", last_letter)
print("YOUR SCHOOL CODE NAME:", first_three + last_letter)

reversed_house = house[::-1]
print("Reversed House Name:", reversed_house)

badge_line_1 = "STUDENT" + house.upper()
badge_line_2 = "CABINET MEMBERS: " + number_of_cabinet_members_text + " | ACHIEVEMENTS: " + number_of_achievements_text
badge_line_3 = "STUDENTS: " + number_of_students_text + " | ACTIVE: " + is_active_text
badge_line_4 = "REVERSED HOUSE NAME: " + reversed_house.upper()

print("")
print("==== SCHOOL BADGE ====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("********************************")