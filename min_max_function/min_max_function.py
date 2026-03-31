def main():
    print('You can get min or max number from your list of numbers.')

    users_array = create_array()

    choice = ''
    while choice != 'min' and choice != 'max':
        choice = input('Type "min" or "max":\n').strip().lower()
    
    if choice == 'min':
        min = minimum_number(users_array)
        print('Your min number from the list is:', min)
        
    elif choice == 'max':
        max = maximum_number(users_array)
        print('Your max number from the list is:' , max)


def create_array():
    number_array = []
    array_size = create_array_size()
    while len(number_array) != array_size:
        number = int(input('Enter  number:'))
        number_array.append(number)
    return number_array

    

def create_array_size():
    array_size = ''
    while not array_size.isdigit():
        array_size = input('How many numbers you want in your list?(enter digit):\n')
        return int(array_size)    

  
def minimum_number(users_array):
    for i in range(len(users_array) - 1):
        if users_array[i] < users_array[i + 1]:
            users_array [i] , users_array [i + 1] = users_array[i + 1] , users_array [i]
    
    return users_array[len(users_array) - 1]


def maximum_number(users_array):
    for i in range(len(users_array) - 1):
        if users_array [i] > users_array [i + 1]:
            users_array [i], users_array [i + 1] = users_array [i + 1], users_array [i]
    return users_array [len(users_array) - 1]

main()





    
