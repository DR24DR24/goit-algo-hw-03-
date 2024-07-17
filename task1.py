import argparse
import os
import shutil
import hashlib



class FilesRearrange:
    def __init__(self,source,destination):
        self.dublicates={}
        self.source=source
        self.destination=destination

    def get_hash(self,path):
        """Повертає хеш-значення для файлу."""
        with open(path, 'rb') as file:
            bytes = file.read() 
            readable_hash = hashlib.sha256(bytes).hexdigest()
            return readable_hash

    def copydublicatefile(self,n:int,filepathname:str,source:str):
        """file is copied
        adding a number in brackets to the file name."""
        basename=os.path.basename(filepathname)
        name, ext = os.path.splitext(basename)
        name+=f"({n})"
        filepathnamecopy=os.path.join(os.path.dirname(filepathname),name+ext)
        if os.path.isfile(filepathnamecopy):
            self.copydublicatefile(n+1,filepathname,source)
        else:
            shutil.copy(source,filepathnamecopy)

    def CopyFile(self,source):
        """tries to copy a file 
        and checks whether a file with the same name exists in the destination directory.
        Checks the new file is the same as in the destination folder or different.
        if the file is the same, then copying does not occur.
        if the file is different, then the file is copied
        File comparison occurs by calculating the hash function. 
        The Hash function is stored in a dictionary. 
        the key in the dictionary is the name of the file in the destination directory.
        The value in the dictionary is a set of hash functions 
        for all files with this name that have previously been processed"""
        try:
            print(source)
            _,ext=os.path.splitext(source)
            filepath= self.destination if ext=="" \
                                            else os.path.join(self.destination,ext[1:])
            filename= os.path.basename(source)
            os.makedirs(filepath,exist_ok=True)
            filepathname=os.path.join(filepath,filename)
            if os.path.isfile(filepathname):
                if filepathname not in self.dublicates:
                    self.dublicates[filepathname]=set()
                    self.dublicates[filepathname].add(self.get_hash(filepathname))
                new_hash=self.get_hash(source)
                if new_hash in self.dublicates[filepathname]:
                    print(f"dublicates: {source}")
                else:
                    print(f"different file with same name: {source}")
                    self.dublicates[filepathname].add(new_hash)
                    self.copydublicatefile(1,filepathname,source)
            else:
                shutil.copy(source,filepathname)
            
        except FileNotFoundError as e:
            print(e)
        except PermissionError as e:
            print(e)
        except OSError as e:
            print(e)
        except Exception as e:
            print(e) 



    def FileRearrange(self,source):   
        """iterates through all files in the input directory 
        when encountering a subdirectory calls itself recursively 
        If a file is encountered calls the file copy function""" 
        try:
            dir_contents = os.listdir(source) 
            try:
                for item in dir_contents:
                    filepath=os.path.join(source,item)
                    if os.path.isdir(filepath):
                        self.FileRearrange(filepath)
                    elif os.path.isfile(filepath):
                        self.CopyFile(filepath)
                    else:
                        print(f"Non recognition item: {filepath}")       
            except FileNotFoundError as e:
                    print(e)
            except PermissionError as e:
                print(e)
            except OSError as e:
                print(e)
            except Exception as e:
                print(e)          

        except PermissionError as e:
            print(e)
        except OSError as e:
            print(e)
        except Exception as e:
            print(e)    



    def FilesRearrange(self):
        """ creates an output directory and runs the main processing logic"""    
        try:
            os.makedirs(self.destination,exist_ok=True)
            self.FileRearrange(self.source)
        except PermissionError as e:
            print(e)
        except OSError as e:
            print(e)
        except Exception as e:
            print(e)  


if __name__=="__main__":


    cur_dir=os.getcwd()

    print(f"cur_dir {cur_dir}")

    parser=argparse.ArgumentParser(description="File rearange")
    parser.add_argument("source",     type=str,nargs='?', default=cur_dir, help="source dir")
    parser.add_argument("destination",type=str,nargs='?', default='..\\dist',  help="source dir")

    args=parser.parse_args()

    print(args.source)
    print(args.destination)

    FA=FilesRearrange(args.source,args.destination)

    FA.FilesRearrange()


