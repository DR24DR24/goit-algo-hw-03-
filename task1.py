import argparse
import os
import shutil
import hashlib

cur_dir=os.getcwd()

print(f"cur_dir {cur_dir}")

parser=argparse.ArgumentParser(description="File rearange")
parser.add_argument("source",     type=str,nargs='?', default=cur_dir, help="source dir")
parser.add_argument("destination",type=str,nargs='?', default='..\\dist',  help="source dir")

args=parser.parse_args()

print(args.source)
print(args.destination)

try:
    os.makedirs(args.destination,exist_ok=True)
except PermissionError as e:
    print(e)
except OSError as e:
    print(e)

def get_hash(path):
    """Повертає хеш-значення для файлу."""
    with open(path, 'rb') as file:
        bytes = file.read() 
        readable_hash = hashlib.sha256(bytes).hexdigest();
        return readable_hash

dublicates={}

def copydublicatefile(n:int,filepathname:str,source:str):
    basename=os.path.basename(filepathname)
    name, ext = os.path.splitext(basename)
    name+=f"({n})"
    filepathnamecopy=os.path.join(os.path.dirname(filepathname),name+ext)
    if os.path.isfile(filepathnamecopy):
        copydublicatefile(n+1,filepathname,source)
    else:
        shutil.copy(source,filepathnamecopy)

def copyfile(source):
    try:
        print(source)
        _,ext=os.path.splitext(source)
        filepath= args.destination if ext=="" else os.path.join(args.destination,ext[1:])
        filename= os.path.basename(source)
        os.makedirs(filepath,exist_ok=True)
        filepathname=os.path.join(filepath,filename)
        if os.path.isfile(filepathname):
            if filepathname not in dublicates:
                dublicates[filepathname]=set()
                dublicates[filepathname].add(get_hash(filepathname))
            new_hash=get_hash(source)
            if new_hash in dublicates[filepathname]:
                print(f"dublicates: {source}")
            else:
                print(f"different file with same name: {source}")
                dublicates[filepathname].add(new_hash)
                copydublicatefile(1,filepathname,source)
        else:
            shutil.copy(source,filepathname)
        
    except Exception as e:
        print(e)




def file_rearrange(source):    
    # try:
    #     dir_contents = os.listdir(source)    
    # # except FileNotFoundError as e:
    # #     print(e)
    # except PermissionError as e:
    #     print(e)
    # except OSError as e:
    #     print(e)
    # except Exception as e:
    #     print(e)    

    dir_contents = os.listdir(source) 

    for item in dir_contents:
        filepath=os.path.join(source,item)
        if os.path.isdir(filepath):
            file_rearrange(filepath)
        elif os.path.isfile(filepath):
            copyfile(filepath)
        else:
            print(f"Non recognition item: {filepath}")


file_rearrange(args.source)

# import hashlib
# import os

# def get_hash(path):
#     """Повертає хеш-значення для файлу."""
#     with open(path, 'rb') as file:
#         bytes = file.read() 
#         readable_hash = hashlib.sha256(bytes).hexdigest();
#         return readable_hash

# def find_duplicates(directory):
#     """Шукає дублікати в директорії."""
#     hashes = {}
#     duplicates = []
#     for dirpath, dirnames, filenames in os.walk(directory):
#         for filename in filenames:
#             path = os.path.join(dirpath, filename)
#             file_hash = get_hash(path)
#             if file_hash not in hashes:
#                 hashes[file_hash] = path
#             else:
#                 duplicates.append((path, hashes[file_hash]))
#     return duplicates

# # Пошук дублікатів у заданій директорії
# duplicates = find_duplicates('/path/to/directory')
# for duplicate in duplicates:
#     print(f"Дублікатні файли: {duplicate[0]} та {duplicate[1]}")
