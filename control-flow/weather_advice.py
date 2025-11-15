weather = input("Enter today's weather (sunny, rainy, cold): ")

if weather == "sunny":
    print("Wear light clothes and drink water.")
elif weather == "rainy":
    print("Carry an umbrella!")
elif weather == "cold":
    print("Wear a jacket.")
else:
    print("Weather type not recognized.")
