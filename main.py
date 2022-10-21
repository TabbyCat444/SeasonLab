input_month = input("Please enter month: ")
input_day = int(input("Please enter day(number): "))

if 'March' in input_month and (31 >= input_day >= 20):
    print('Spring')
elif 'June' in input_month and (0 < input_day <= 20):
    print('Spring')
elif 'April' in input_month and (0 < input_day <= 30):
    print('Spring')
elif 'May' in input_month and (0 < input_day <= 31):
    print('Spring')
elif 'June' in input_month and (30 >= input_day >= 21):
    print('Summer')
elif 'September' in input_month and (0 < input_day <= 21):
    print('Summer')
elif 'July' in input_month and (0 < input_day <= 31):
    print('Summer')
elif 'August' in input_month and (0 < input_day <= 31):
    print('Summer')
elif 'September' in input_month and (30 >= input_day >= 22):
    print('Autumn')
elif 'December' in input_month and (0 < input_day <= 20):
    print('Autumn')
elif 'October' in input_month and (0 < input_day <= 31):
    print('Autumn')
elif 'November' in input_month and (0 < input_day <= 30):
    print('Autumn')
elif 'December' in input_month and (31 >= input_day >= 21):
    print('Winter')
elif 'March' in input_month and (0 < input_day <= 19):
    print('Winter')
elif 'January' in input_month and (0 < input_day <= 31):
    print('Winter')
elif 'February' in input_month and (0 < input_day <= 29):
    print('Winter')
else:
    print('Invalid')
