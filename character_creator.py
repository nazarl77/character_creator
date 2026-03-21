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
    height = int(input('Overall character height (10 - 20) : '))
    hair = input('Character for the hair: ')
    eye = input('Character for the eyes: ')
    arm = input('Character for the arms: ')
    shoe = input('4-character string for the shoes:')
    
    print()
    print_head(hair,eye)
    print_body(height, arm)
    print_legs(height, shoe)

boundary = '---------------------------------------------'
print(boundary + '\n')

main()

print(boundary)
