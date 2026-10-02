def calculate_weight(mass, gravity):
    return mass * gravity


EARTH_GRAVITY = 9.8
MOON_GRAVITY = 1.62

try:
    mass = float(input("Enter mass of object in kg: "))

    earth_weight = calculate_weight(mass, EARTH_GRAVITY)
    moon_weight = calculate_weight(mass, MOON_GRAVITY)

    print("\nResults:")
    print("Weight on Earth:", earth_weight, "N")
    print("Weight on Moon:", moon_weight, "N")

except ValueError:
    print("Invalid input! Please enter a valid number.")