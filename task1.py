import argparse
import os
import shutil

cur_dir=os.getcwd()

print(f"cur_dir {cur_dir}")

parser=argparse.ArgumentParser(description="File rearange")
parser.add_argument("source",     type=str,nargs='?', default=cur_dir, help="source dir")
parser.add_argument("destination",type=str,nargs='?', default='dist',  help="source dir")

args=parser.parse_args()

print(args.source)
print(args.destination)

try:
    os.makedirs(args.destination,exist_ok=True)
except PermissionError as e:
    print(e)
except OSError as e:
    print(e)

def copyfile(source):
    try:
        print(source)
        _,ext=os.path.splitext(source)
        filepath= args.destination if ext=="" else os.path.join(args.destination,ext[1:])
        filename= os.path.basename(source)
        filepath=os.path.join(filename)
        shutil.copy2(source,filepath)
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
        if os.path.isdir(item):
            file_rearrange(item)
        elif os.path.isfile(item):
            copyfile(item)
        else:
            print(f"Non recognition item: {item}")


file_rearrange(args.source)
