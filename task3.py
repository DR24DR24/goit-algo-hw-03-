#import 

hanoi_towers=[[],[],[]]

def init_hanoi_towers(size:int, towers:list):
    towers[0]=[x for x in range(size,0,-1)]

def search_solution(deep:int,towers:list)->bool:
    #print(F"{towers[0]}\n{towers[1]}\n{towers[2]}\n\n")
    if len(towers[0])+len(towers[1])==0:
        print("result")
        print(F"{towers[0]}\n{towers[1]}\n{towers[2]}\n")
        return True 
    if deep<1:
        return False
    for i in range(3):
        for j in range(3):
            if len(towers[j])!=0:
                if len(towers[i])==0:
                    towers[i].append(towers[j].pop())
                    if search_solution(deep-1,towers):
                        towers[j].append(towers[i].pop())
                        print(F"{towers[0]}\n{towers[1]}\n{towers[2]}\n")
                        return True  
                    else:
                        towers[j].append(towers[i].pop())
                         
                elif (towers[i][-1])>(towers[j][-1]):
                    towers[i].append(towers[j].pop())
                    if search_solution(deep-1,towers):
                        towers[j].append(towers[i].pop())
                        print(F"{towers[0]}\n{towers[1]}\n{towers[2]}\n")
                        return True
                    else:
                        towers[j].append(towers[i].pop())
    return False


init_hanoi_towers(4, hanoi_towers)
print(F"{hanoi_towers[0]}\n{hanoi_towers[1]}\n{hanoi_towers[2]}\n\n")
deep=1
while not search_solution(deep,hanoi_towers):
    deep+=1
    print(f"deep {deep}")