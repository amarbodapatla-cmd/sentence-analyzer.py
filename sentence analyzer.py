def is_integer():
    while True:
        user_input = input('Enter a value')
        if  user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            print('Enter a exact num ',user_input)
            number = abs(int(user_input))
            return number
        else:
            print('invalid input, please enter a valid input')
number = is_integer()
print('you enter valid num',number)
name = input('enter a sentence ')

count=0
c_count=0
space_count=0

for i in range(min(number,len(name))):
    r= name[i]
    print(r)
    if r.lower() in 'aeiou' :
        count+=1
    elif r == " ":
        space_count+=1
    else:
        c_count+=1
word = name.split()       
longest_word =max(word, key=len)        
print(f'vowels:{count},consonant:{c_count},space:{space_count}')
print(f"total letter:{len(name)}")
print(longest_word)       


    
#
