def reverse_array(any_list):  
    reversed_list = []
    for i in range(len(any_list) - 1 , -1 , -1):
       reversed_list.append(any_list[i])
    return reversed_list



def create_array(amount):
    i = 0
    my_array = []
    while i != amount:
        value = input('Enter a value:')
        my_array.append(value)
        i += 1

    return my_array

def create_array_size():
    print('How many values you want in your array?')
    amount = '' 
    while not amount.isdigit():
        amount = input('Enter a number of elements:')
    return int(amount)

def main():
    print('Let me reverse your array. ')
    
    amount = create_array_size()
    array = create_array(amount)
    reverse_function = reverse_array(array)

    print('Your reversed array:', reverse_function)

main()