import random
from datetime import date, datetime


### Baby Prep Assignment ###

# Constants
OUNCES_PER_POUND = 16
DEFAULT_MOOD = "content"


# Functions
def introduce_baby(baby_name, age, current_weight):
    funny_things = [
        "wearing my socks as hats",
        "trying to eat my toes",
        "having a dance party with my toys",
    ]
    print()
    print(f"Hi! My name is {baby_name}. I am {age} years old.")
    print(f"I weigh {current_weight} ounces.")
    print(f"I like {random.choice(funny_things)}!")


def eat(current_weight, eat_count):
    current_weight += 11
    eat_count += 1
    print(f"{baby_name} is eating.")

    if eat_count % 3 == 0:
        current_weight = poop(current_weight)

    return current_weight, eat_count


def drink(current_weight, drink_count):
    current_weight += 8
    drink_count += 1
    print(f"{baby_name} is drinking.")

    if drink_count % 3 == 0:
        current_weight = pee(current_weight)

    return current_weight, drink_count


def poop(current_weight):
    current_weight -= 5
    print(f"{baby_name} pooped.")

    return current_weight


def pee(current_weight):
    current_weight -= 4
    print(f"{baby_name} peed.")
    return current_weight


def cry():
    print(f"{baby_name} is crying.")

    return "Sad"


def sleep():
    print(f"{baby_name} is sleeping.")

    return "Content"


def display_status(baby_name, current_weight, mood, eat_count, drink_count):
    weight_lb = current_weight / OUNCES_PER_POUND

    print()
    print("--- BABY STATUS ---")
    print("Name:", baby_name)
    print("Weight in ounces:", current_weight)
    print(f"Weight in pounds: {weight_lb:.2f}")
    print("Mood:", mood)
    print("Feedings:", eat_count)
    print("Drinks:", drink_count)


# Inputs
print()
baby_name = input("Enter the baby's name: ")
birth_day = input("Enter the baby's birthday (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_day, "%Y-%m-%d").date()
starting_weight = int(input("Enter the baby's weight in ounces: "))
height_in = float(input("Enter the baby's height in inches: "))

# Calculate the baby's age in completed years
today = date.today()
age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1


# Starting Values
current_weight = starting_weight
mood = DEFAULT_MOOD
eat_count = 0
drink_count = 0


# Introduce the Baby
introduce_baby(baby_name, age, current_weight)


# Care Loop
while True:
    print("\n--- CARE MENU ---")
    print("Eat")
    print("Drink")
    print("Sleep")
    print("Cry")
    print("Status")
    print("Home\n")

    action = input("Choose an action: ").lower()

    if action == "eat":
        current_weight, eat_count = eat(current_weight, eat_count)
        mood = "Happy"

    elif action == "drink":
        current_weight, drink_count = drink(current_weight, drink_count)
        mood = "Content"

    elif action == "sleep":
        mood = sleep()

    elif action == "cry":
        mood = cry()

    elif action == "status":
        display_status(baby_name, current_weight, mood, eat_count, drink_count)

    elif action == "home":
        break

    else:
        print("Unknown action - try again.")


# Final Outputs
weight_lb = current_weight / OUNCES_PER_POUND
print()
print("--- FINAL BABY STATUS ---")
print("Name:", baby_name)
print("Birthday:", birth_day)
print("Height in inches:", height_in)
print("Starting weight in ounces:", starting_weight)
print("Current weight in ounces:", current_weight)
print(f"Current weight in pounds: {weight_lb:.2f}")
print("Mood:", mood)
print("Feedings:", eat_count)
print("Drinks:", drink_count)
print()