def season_events(number_of_month):
    if number_of_month == 12 or number_of_month <= 2:
        return 'winter.White snow fell outside the window'
    elif number_of_month < 5:
        return 'spring.Birds sang beautiful songs'
    elif number_of_month < 8:
        return 'summer.The sun shone brighter than ever'
    elif number_of_month < 11:
        return 'autumn.The harvest was incredible'
    else:
        return 'You need to enter the real number of the month'
print('Enter number of the month:')
number_of_month = int(input())
print("You were born in",season_events(number_of_month))
