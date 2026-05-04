fastestroute = 0
fastesttime = 0.0

for route in range(1, 11):
    distance = float(input(f"\nEnter the route {route} distance (miles): "))
    speed = float(input(f"\nEnter route {route} speed (miles/hour): "))

    if distance <= 0:
        print("The distance is invalid. Route will be skipped.")

    elif speed <= 0:
        print("The speed is invalid. Route will be skipped.")

    else:
        timeinminutes = (distance / speed) * 60
        print("Route", route, "time:", round(timeinminutes), "minutes")

        if fastestroute == 0:
            fastestroute = route
            fastesttime = timeinminutes
        elif timeinminutes < fastesttime:
            fastestroute = route
            fastesttime = timeinminutes

    More = input("\n Would you like more routes (yes/no)?: ")

    if More == "no":
        break

if fastestroute == 0:
    print("\nThere are no valid routes entered.")
else:
    print("\nThe route", fastestroute, "is fastest;", round(fastesttime), "minutes")