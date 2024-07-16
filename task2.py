import argparse
import os

cur_dir=os.getcwd()

print(f"cur_dir {cur_dir}")

parser=argparse.ArgumentParser(description="File rearange")
parser.add_argument("source",     type=str,nargs='?', default=cur_dir, help="source dir")
parser.add_argument("destination",type=str,nargs='?', default='dist',  help="source dir")

args=parser.parse_args()

print(args.source)
print(args.destination)

os.makedirs(args.destination)
