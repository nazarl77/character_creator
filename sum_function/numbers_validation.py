def num_validation(nums):
    return sum(nums)

print('Lets sum up your 5 numbers!\n')

numbers = []
while len(numbers) != 5:
    num = input('Enter a number:')
    if not num.isdigit():
        print('Program accepts only numbers.Try again. ')
        
    else:
        num = int(num)
        numbers.append(num) 
        
   
sum = num_validation(numbers)
print('Summary:' , sum)



