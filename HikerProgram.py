hiker = int(input("How many hikers are going? "))
stay = int(input("How long are you planning to be on your trip? (Days) "))
rain = str(input("Will it rain during your trip? y/n "))
check = 0

food = (hiker * 2) * stay
if (hiker % 2 == 1):
    temp = 1 + hiker
    tent = temp / 2
    tent = int(tent)
    check += 1
elif(hiker % 2 == 0):
    tent = hiker / 2
    check += 1
if (rain=="y" or rain=="yes"):
    rain = "with rain in the forecast"
    rainGear = " and rain gear"
    check += 1
elif (rain=="n" or rain=="no"):
    rain = "with no rain in the forecast"
    rainGear = ""
    check += 1
    
if (check==2):
    print("For your hike of "+str(hiker)+" hikers for "+str(stay)+" days "+rain+", you will need to pack "+str(food)+" pounds of food, "+str(tent)+" tents"+rainGear+".")
else:
    print("Error, please try again.")