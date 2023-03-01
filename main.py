from PIL import Image
import glob

for (i, filename) in enumerate(glob.glob("C:/Users/sharath.narayanaswam/Desktop/Datasets_Flowers/Data/*.jpg")):
    print(filename)
    print(i)

    img = Image.open(filename)
    img.save('{}{}{}'.format('C:/Users/sharath.narayanaswam/Desktop/Datasets_Flowers/Data1/', i+1, 'nn.png'))