def happyBirthday():
    import datetime
    from datetime import datetime
    today = datetime.today()
    checkMonth = input('What is your birthday month (two digit number 1-12)? ')
    checkDay = input('Which day of the month? (two digits) ')
    stringMonth = today.strftime("%m")
    stringDay = today.strftime("%d")
    print(checkMonth)
    print(today.month)
    print(stringMonth + ' = stringMonth')
    print(checkDay)
    print(today.day)
    print(stringDay + ' = stringDay')

    if (stringMonth == checkMonth) and (stringDay == checkDay):
        print("Happy Birthday!")
    else:
        print("Today is not your birthday")

happyBirthday()
