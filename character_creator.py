def print_head(hair,eye):
    print(hair * 12)
    print(hair + '|        |' + hair)
    print(hair + '|  ' + eye + '  ' + eye + '  |' + hair)
    print(' |   /\\   | ')
    print(' |        | ')
    print(' \\  "--"  / ')
    print('   ------   ')



def print_body(height, arm):
    print('     XX     ')
    print('#' + (4 * arm) + 'XX' + (4 * arm) + '#')
    print('    XXXX\n' * height , end = '')

def reverse_shoe(shoe):
    return shoe[::-1]


def print_legs(height , shoe):
    print('    ====    ')
    print('   ||  ||\n' * height , end = '')
    print(' ' + shoe + '  ' + reverse_shoe(shoe))

def main():
    print('Welcome to the custom character creator tool!')
    
    while True:
         height = int(input('Overall character height (5 - 10):'))
         if height < 5 or height > 10:
            print('Try again!')
         else:
             break
        
    while True:
         hair = input('1 - Character for the hair: ')
         eye = input('1 - Character for the eyes: ')
         arm = input('1 - Character for the arms: ')
         shoe = input('4 - character string for the shoes:')
         if len(hair) != 1 or len(eye) != 1 or len(arm) != 1 or len(shoe) != 4:
             print('Invalid quantity of characters , try again. ')
         else:
             break
      
    print()
    print_head(hair,eye)
    print_body(height, arm)
    print_legs(height, shoe)

boundary = '---------------------------------------------'
print(boundary + '\n')

main()

print(boundary)
