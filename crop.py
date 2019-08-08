from PIL import Image
import glob
from tqdm import tqdm
import os

class Crop:
    def __init__(self,parameter):
        self.parameter = parameter
        self.image_paths,self.label_paths,self.dataset_size = self.get_paths()
        self.width,self.height = self.get_image_property()
    
    def get_paths(self):
        """
        return : dir image paths , dir label paths, dataset size
        In segmentation dataset, the leaves of image and label is equal
        """
        image_paths = glob.glob(self.parameter["image_dir"]+"/*")
        label_paths = glob.glob(self.parameter["label_dir"]+"/*")
        return image_paths,label_paths,len(image_paths)
    
    def get_image_property(self):
        """
        In my dataset,images have same shape
        """
        image = Image.open(self.image_paths[0])
        return image.size
    
    def crop(self,image_path,save_dir):
        """
        image: an image for crop
        name : [image's file name, iamge's extension]
        width_leaves : maximum number of sheets that be can cut horizontally
        height_leaves: maximum number of sheets that be can cut vertically
        """
        image = Image.open(image_path)
        name = os.path.splitext(os.path.basename(image_path))
        width_leaves = self.width//self.parameter["crop_size"]
        height_leaves = self.height//self.parameter["crop_size"]

        for height in range(height_leaves):
            for width in range(width_leaves):
                # 正方形に切り出すので以下のような変数設定になる。
                # 割ることのできる最大数？？を考えた。
                x = self.parameter["crop_size"]*width
                y = self.parameter["crop_size"]*height
                x1,y1,x2,y2 = x,y,x+self.parameter["crop_size"],y+self.parameter["crop_size"]
                crop = image.crop((x1,y1,x2,y2))
                #save crop image
                crop.save(save_dir+"/{}-{:02d}-{:02d}{}".format(name[0],height+1,width+1,name[1]))
    
    def main(self):
        for i in tqdm(range(self.dataset_size)):
            self.crop(self.image_paths[i],self.parameter["image_save_dir"])
            self.crop(self.label_paths[i],self.parameter["label_save_dir"])
        
if __name__ == "__main__":
    parameter = {"image_dir":"/home/fumito/Pictures/adachi_lab_data/DP_data/row_data/data/image",
                 "label_dir":"/home/fumito/Pictures/adachi_lab_data/DP_data/row_data/data/label",
                 "image_save_dir":"/home/fumito/Pictures/adachi_lab_data/DP_data/data_crop_475/image",
                 "label_save_dir":"/home/fumito/Pictures/adachi_lab_data/DP_data/data_crop_475/label",
                 "crop_size":475}
    crop = Crop(parameter)
    crop.main()