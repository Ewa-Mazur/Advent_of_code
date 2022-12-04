with open('day4_input.txt','r', encoding='UTF-8') as file:
    input_data = file.read()
    elf_pair = []
    counter = 0


    for line in input_data.splitlines():
        elf_pair.append(line.split(','))

        

    for sector in elf_pair:

        elf_1_min = int(sector[0].split('-')[0])
        elf_1_max = int(sector[0].split('-')[1])

        elf_2_min = int(sector[1].split('-')[0])
        elf_2_max = int(sector[1].split('-')[1])

        if elf_1_min in range(elf_2_min,(elf_2_max+1)) and elf_1_max in range(elf_2_min,(elf_2_max+1)):
            counter += 1
            
        elif elf_2_min in range(elf_1_min,(elf_1_max+1)) and elf_2_max in range(elf_1_min,(elf_1_max+1)):
            counter += 1
            
        else:
            continue


    print(counter)



