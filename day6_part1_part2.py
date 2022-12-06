with open('day6_input.txt','r',encoding='UTF-8') as file:
    code = file.read()
    code_list = []
    N = 4 #number of individual characters


    for i in code:
        code_list.append(i)



    for i in range(0,len(code_list)):
        #N-element fragment of code_list changed to set
        l = set(code_list[i:(i+N)])       

        if len(l) == N: #means lack of duplicates in set (individual chars)
            print(l)
            print(i+N) #answer
            break
