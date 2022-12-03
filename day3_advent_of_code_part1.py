import string


with open('day3_input.txt', 'r', encoding='UTF-8') as file:
    rucksack = file.read()
    rucksack_list = []
    alpha_priority_list = []
    rucksack_value = []


    for letter in string.ascii_letters:
        alpha_priority_list.append(letter)


    for item in rucksack.splitlines():

        common = set(item[0:int((len(item)/2))]) & set(item[int((len(item)/2)):])
        common = ''.join(common)
        rucksack_list.append(common)


    for letter in rucksack_list:
        if letter == '':
            continue
        else:
            rucksack_value.append((alpha_priority_list.index(letter)+1))

    print(rucksack_list)
    print(sum(rucksack_value))
        
        



    
    



