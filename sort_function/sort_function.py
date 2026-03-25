def sort_asc(nums):
    for u in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i],nums[i + 1] = nums[i + 1] , nums[i]

    return nums

def sort_desc(nums):
    for u in range(len(nums)):
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
             nums[i],nums[i + 1] = nums[i + 1],nums[i]
    return nums



def order():
    print('In what order do u want to sort your numbers?')
    print('Enter "1" for ascending order or "2" for descending order')
    order = ''
    while order not in ('1', '2'):
        order = input('Your choice: "1" or "2":\n').strip()

        if order not in ('1', '2'):
            print('Invalid input, try again')

    return int(order)


    
def l_creation():     
    nums = []
    o = howmany()
    while len(nums) < o:  
        num = input('Enter a whole number:')
     
        try:
            num = int(num)
            nums.append(num)
        except:
            print('Invalid input.Try again.')
    return nums




def howmany():
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
   
    ord = order()
    noms = l_creation()
    if ord == 1:
       l = sort_asc(noms)
       print('Your numbers in ascending order:\n', l)  
    elif ord == 2:
       q = sort_desc(noms)
       print('Your numbers in descending order:\n', q)

main()