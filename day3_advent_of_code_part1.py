import string


with open('day3_input.txt', 'r', encoding='UTF-8') as file:
    rucksack = file.read()
    rucksack_list = []
    rucksack_value = []

    alpha_priority_list = list(string.ascii_letters)


    for item in rucksack.splitlines():

        common = set(item[0:int((len(item)/2))]) & set(item[int((len(item)/2)):])
        common = ''.join(common)
        rucksack_value.append((alpha_priority_list.index(common)+1))


    
    print(sum(rucksack_value))
        
        



    
    



