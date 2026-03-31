def num_summing(nums,amount):
    i = 0
    total = 0

    while i != amount:
        total += nums[i]
        i += 1

    return total

def input_list_size():
    count = ''
    while True:
        count = int(input('How many numbers you want to sum up:'))
        if count > 0:
            return count
        else:
            print('Number must be greater than 0.Try again.')
              
       

def create_list(amount):       
     numbers_list = []  
     while len(numbers_list) != amount:
         number = int(input('Enter a number:'))              
         numbers_list.append(number) 
     return numbers_list
           


def main():
    print('Lets sum up your numbers!')

    amount = input_list_size()
    numbers = create_list(amount)
    total = num_summing(numbers , amount)
    
    print('Summary:' , total)

main()

