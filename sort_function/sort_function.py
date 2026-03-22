def sort_asc(nums):
    asc = sorted(nums)
    return asc

def sort_desc(nums):        
    desc = sorted(nums,reverse = True)
    return desc


print('Hellooooooo!!!\nChoose in what order you prefer to sort your 5 numbers:')
print('Enter 1 for ascending order or 2 for descending order.')


order = 0
while order not in (1 , 2):
     order = int(input('Your choise:\n'))
    
     
nums = []

while len(nums) < 5:  
     num = input('Enter a whole number:')
     
     try:
        num = int(num)
        nums.append(num)
     except:
        print('Invalid input.Try again.')

if order == 1:
     l = sort_asc(nums)
     print('Your numbers in ascending order:\n', l)  
elif order == 2:
     q = sort_desc(nums)
     print('Your numbers in descending order:\n', q)


