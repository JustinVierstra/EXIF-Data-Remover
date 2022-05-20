from PIL import Image
import os
import glob

for filename in glob.glob('*.jpeg') + glob.glob('*.png') + glob.glob('*.jpg'):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        name, extension = os.path.splitext(filename)
        
        if name.endswith('image_file_without_exif'):
            break
        elif extension.lower().endswith('.jpeg') or extension.lower().endswith('.png') or extension.lower().endswith('.jpg'):
            print("EXIF data removed from: " + filename)
            image = Image.open(filename)
            # next 3 lines strip exif
            data = list(image.getdata())
            image_without_exif = Image.new(image.mode, image.size)
            image_without_exif.putdata(data)
            #image_without_exif.save(name + '_image_file_without_exif' + extension)
            image_without_exif.save(name + extension)
