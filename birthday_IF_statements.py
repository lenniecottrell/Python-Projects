import datetime

today = datetime.date.today()
checkDate = datetime.datetime(2020, 6, 30)
allisonBday = datetime.datetime(2020, 5, 9)

print(today)
print(checkDate)
print(allisonBday)

if today.month == checkDate.month and today.day == checkDate.day:
    print("Happy birthday!")
elif today.month == allisonBday.month and today.day == allisonBday.day:
    print("It's Allison's birthday!")
else:
    print("It's not your or Allison's birthday")
    if today.month > 6:
        print("You have to wait until next year")
    elif today.month == 5 and today.day >= 10:
        print("Your birthday is next!!")
    else:
        print("Allison's birthday is next!!")
