from PIL import Image
import glob
import os

class Resize:
    def __init__(self,befor_dir,after_dir):
        self.before_dir = befor_dir
        self.after_dir = after_dir
        self.all_paths = self.get_all_paths()

    
    def get_all_paths(self):
        paths = sorted(glob.glob(self.before_dir+"/*"))
        return paths

    def resize(self,path,width,height):
        image = Image.open(path)
        image = image.resize((width,height),Image.LANCZOS)
        return image

    def main(self,width,height):
        for path in self.all_paths:
            path_name = os.path.basename(path)
            image = self.resize(path,width,height)
            image.save(self.after_dir+path_name)

if __name__ == "__main__":
    params = {"before_dir":"/home/fumito/Desktop/workspace/pytorch/cnn/data/test",
              "after_dir":"/home/fumito/Desktop/workspace/pytorch/cnn/resize_data/test/",
              "width":256,"height":256}
    md = Resize(params["before_dir"],params["after_dir"])
    md.main(params["width"],params["height"])
