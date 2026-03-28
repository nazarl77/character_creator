def count_vowels(string_array):
    vowels = 'aeiouy'
    result = []
    for word in string_array:
        count = 0
        for letter in word:
            if letter in vowels:
                count +=1
        result.append(count)
    return result
             

def create_array():
    users_list = []
    string = ''
    while string != 'stop':
        string = input('Word:').strip().lower()
        users_list.append(string)
    return users_list


def main():
    print('\nI can count vowels in each word in your list!')
    print('You will be able to input as many words as you want and when you are done just write "stop".')
    
    users_list = create_array()
    count = count_vowels(users_list)
    
    print('Amount of vowels in each word:', count)

main()



    





    