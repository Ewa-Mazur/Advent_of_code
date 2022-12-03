import string


with open('day3_input.txt', 'r', encoding='UTF-8') as file:
    rucksack = file.read()

    alpha_priority_list = list(string.ascii_letters)

    line1 = []
    line2 = []
    line3 = []
    i = 0
    common_list = []
    badge = []

    for item in rucksack.splitlines():
        if i ==0:
            line1 = set(item)
            i += 1
            
        elif i ==1:
            line2 = set(item)
            i += 1
            
        elif i == 2: 
            line3 = set(item)

            common = line1 & line2 & line3
            common = ''.join(common)
            badge.append((alpha_priority_list.index(common)+1))

            i = 0
            line1 = []
            line2 = []
            line3 = []

    print(sum(badge))


            
            
        

    
