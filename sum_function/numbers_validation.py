def num_summing(nums,amount):
    i = 0
    total = 0

    while i != amount:
        total += nums[i]
        i += 1

    return total

def howmany():
    num = ''
    while True:
        num = input('How many numbers you want to sum up:')
        
        if num.isdigit():
            number = int(num)
            if number > 0:
                return number
            else:
                print('Number must be greater than 0.Try again.')
        else:
            print('Program accepts only whole numbers.')        
       

def list_create(amount):       
     numbers = []
     while len(numbers) != amount:
         num = input('Enter a number:')
         if not num.isdigit():
            print('Program accepts only numbers.Try again. ')       
         else:
            num = int(num)
            numbers.append(num) 
     return numbers
           


def main():
    print('Lets sum up your numbers!')

    amount = howmany()
    numbers = list_create(amount)
    total = num_summing(numbers , amount)
    
    print('Summary:' , total)

main()

