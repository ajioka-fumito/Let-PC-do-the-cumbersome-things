import shutil
import glob
import os

class Move_files:
    def __init__(self,parameter):
        self.befor_dir = parameter["before_dir"]
        self.after_train_dir = parameter["after_train_dir"]
        self.after_test_dir = parameter["after_test_dir"]
        self.all_paths = self.get_all_paths()

    def get_all_paths(self):
        paths = glob.glob(self.befor_dir+'/*')
        return paths

    def move(self):
        for path in self.all_paths:
            name = os.path.basename(path)
            
            if int(name[0:2])%10==5:
                shutil.copyfile(path,self.after_train_dir+"/"+name)

            elif int(name[0:2])%10==0:
                shutil.copyfile(path,self.after_test_dir+"/"+name)
            else:
                pass






if __name__ == "__main__":
 

    parameter = {"before_dir":"./data/row_data/label",
                 "after_train_dir":"./data/train/label",
                 "after_test_dir":"./data/test/label"}

    fnc = Move_files(parameter)
    fnc.move()