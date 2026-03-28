def sorting(numbers):
    print('In what order do u want to sort your numbers?')
    print('Enter "asc" for ascending order or "desc" for descending order')

    sorting_order = ''
    while sorting_order != 'asc' and sorting_order != 'desc':
        sorting_order = input('Your choice: "asc" or "desc":\n').strip().lower()

        if sorting_order not in ('asc', 'desc'):
            print('Invalid input, try again')

    
    for u in range(len(numbers) - 1):
        for i in range(len(numbers) - 1):
            if numbers [i] > numbers [i + 1]:
                numbers [i],numbers [i + 1] = numbers [i + 1] , numbers [i]
                
    if sorting_order == 'asc':
        return numbers
    if sorting_order == 'desc':
        return numbers[::-1]
    
 
def create_list():     
    numbers = []
    list_size = input_list_size()
    while len(numbers) < list_size:  
        num = int(input('Enter a whole number:'))
        numbers.append(num)
        
    return numbers

def input_list_size():
    i = ''
    while not i.isdigit():
          i = input('How many numbers you wanna sort?(enter digits):\n')
          if i.isdigit():
             o = int(i)
             if o > 1:
                return o
             else:
                print('It should be at least two numbers for sorting. Try again.')
          else:
              print('It should be a digit.Try again.')
    

            
    

def main():
    print('Let me take your numbers and sort them in ascending or descending order\n')      
    number_list = create_list()
    sort_list = sorting(number_list)
    print('Your sorted list:', sort_list)

main()