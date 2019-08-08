import os.path as path
import shutil
import glob

def create_segmentation_dataset(voc_dir,dataset_dir):
    iamges_dir = voc_dir+"JPEGImages/"
    labels_dir = voc_dir+"SegmentationClass/"
    image_paths = sorted(glob.glob(iamges_dir+"*"))
    label_paths = sorted(glob.glob(labels_dir+"*"))
    print(len(image_paths),len(label_paths))
    i = 0
    for j in range(len(label_paths)):
        name_label = path.splitext(path.basename(label_paths[j]))[0]
        while 1:
            name_image = path.splitext(path.basename(image_paths[i]))[0]
            if name_image == name_label:
                shutil.copy(iamges_dir+"{}{}".format(name_image,".jpg"),dataset_dir+"images/{}{}".format(name_image,".jpg"))
                shutil.copy(labels_dir+"{}{}".format(name_label,".png"),dataset_dir+"labels/{}{}".format(name_label,".png"))
                i += 1
                break
            else:
                i += 1
if __name__ == "__main__":
    create_segmentation_dataset("/home/fumito/Pictures/VOCdevkit/VOC2012/","/home/fumito/Pictures/data/")
    