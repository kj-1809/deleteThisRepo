#find longest word in array


def find_longest_word(ls):
    max_length = 0
    longest_word =""
    for i in ls:
        if(len(i) > max_length):
            max_length = len(i)
            longest_word = i
    return longest_word

ls = ['My' , 'Name' , 'is' , 'Krishna' , 'Jindal' , '(developer)']

print('Given List : ' , ls)
print('Longest Word : ' , find_longest_word(ls))