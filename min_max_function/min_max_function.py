def minimum(nums):
    return min(nums)


def maximum(nums):
    return max(nums)

print('You can get min or max number from your list of numbers.')

choice = ''
while choice != 'min' and choice != 'max':
    choice = input('Type "min" or "max":\n').strip().lower()
   
list = []
while len(list) < 5:
    num = input('Enter a whole number:' )
    try:
        num = int(num)
        list.append(num)
    except:
        print('Invalid input, try again.')

if choice == 'min':
    l = minimum(list)
    print('Your mininim number from the list is', l)

elif choice == 'max':
    q = maximum(list)
    print('Your max number from the list is', q)

    
