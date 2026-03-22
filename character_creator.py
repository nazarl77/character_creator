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
    

    height = 0
    while height <= 5 or height >= 10:
         height = int(input('Overall character height (5 - 10):'))
         
    hair = ''
    eye = ''
    arm = ''
    shoe = ''

    while len(hair) != 1 or len(eye) != 1 or len(arm) != 1 or len(shoe) != 4:
         hair = input('Enter one character for the hair: ')
         eye = input('Enter one character for the eye: ')
         arm = input('Enter one character for the arms: ')
         shoe = input('Enter four character string for the shoes:')
         print('Invalid quantity of characters , try again. ')
      
    print()
    print_head(hair,eye)
    print_body(height, arm)
    print_legs(height, shoe)

boundary = '---------------------------------------------'
print(boundary + '\n')

main()

print(boundary)
