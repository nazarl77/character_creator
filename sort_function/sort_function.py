def sorting(numbers,sorting_order):
    print('In what order do u want to sort your numbers?')
    print('Enter "1" for ascending order or "2" for descending order')

    sorting_order = ''
    while sorting_order != 'asc' and sorting_order != 'desc':
        sorting_order = input('Your choice: "asc" or "desc":\n').strip().lower()

        if sorting_order not in ('asc', 'desc'):
            print('Invalid input, try again')

    if sorting_order == 'asc':
      for u in range(len(numbers) - 1):
        for i in range(len(numbers) - 1):
            if numbers [i] > numbers [i + 1]:
                numbers [i],numbers [i + 1] = numbers [i + 1] , numbers [i]



    return numbers

def input_order():
    
    order = ''
    while order != 'asc' and order != 'desc':
        order = input('Your choice: "asc" or "desc":\n').strip().lower()

        if order not in ('asc', 'desc'):
            print('Invalid input, try again')

    return order


    
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
   
    
    numbers = create_list()
    l = sorting(numbers,)
    print('Your numbers in ascending order:\n', l)  
    q = sorting(numbers,)
    print('Your numbers in descending order:\n', q)

main()