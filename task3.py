import time
from functools import lru_cache

hanoi_towers=[[],[],[]]

old_case={}


def init_hanoi_towers(size:int, towers:list):
    towers[0]=[x for x in range(size,0,-1)]

#@lru_cache(maxsize=None)
def search_solution(deep:int,towers:list)->bool:
    #print(F"{towers[0]}\n{towers[1]}\n{towers[2]}\n\n")

    key=(tuple(towers[0]),tuple(towers[1]),tuple(towers[2]))
    if key in old_case and deep<old_case[key]:
            return False
    else:
        old_case[key]=deep    
    

    if len(towers[0])+len(towers[1])==0:
        print("result")
        print(F"{towers[0]}\n{towers[1]}\n{towers[2]}\n")
        return True 

    if deep<1:
        return False
    


    for i in range(3):
        for j in range(3):
            if (i!=j) and len(towers[j])!=0 and (len(towers[i])==0 or (towers[i][-1])>(towers[j][-1])):
                towers[i].append(towers[j].pop())
                if search_solution(deep-1,towers):
                    towers[j].append(towers[i].pop())
                    print(F"{towers[0]}\n{towers[1]}\n{towers[2]}\n")
                    return True  
                else:
                    towers[j].append(towers[i].pop())
    return False


init_hanoi_towers(7, hanoi_towers)
print(F"{hanoi_towers[0]}\n{hanoi_towers[1]}\n{hanoi_towers[2]}\n\n")
deep=1
start_time=time.time()
while not search_solution(deep,hanoi_towers):
    deep+=1
    old_case.clear()
    print(f"deep {deep}")
print(f"duration: {time.time()-start_time}")


# k=0

# def hanoi(n, source, target, auxiliary, towers):
#     global k
#     if n > 0:

#         # Переміщення n-1 дисків з source на auxiliary
#         hanoi(n-1, source, auxiliary, target, towers)
        
#         # Переміщення найбільшого диска з source на target
#         disk = towers[source].pop()
#         towers[target].append(disk)
#         print(f"Перемістити диск з {source} на {target}: {disk}")
#         print(f"Проміжний стан: {towers}")
#         k+=1
#         print(k)
#         # Переміщення n-1 дисків з auxiliary на target
#         hanoi(n-1, auxiliary, target, source, towers)

# def main():
#     n = int(input("Введіть кількість дисків: "))
    
#     # Початковий стан стрижнів
#     towers = {
#         'A': list(range(n, 0, -1)),
#         'B': [],
#         'C': []
#     }
    
#     print(f"Початковий стан: {towers}")
    
#     # Виконання алгоритму Ханойських веж
#     hanoi(n, 'A', 'C', 'B', towers)
    
#     print(f"Кінцевий стан: {towers}")

# if __name__ == "__main__":
    main()
