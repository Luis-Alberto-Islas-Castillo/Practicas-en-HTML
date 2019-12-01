def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter you firs name: ')
first_name_initial = get_initial(first_name)

print('your initial is: ' + first_name_initial)
