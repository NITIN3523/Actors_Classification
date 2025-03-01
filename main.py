import os
from PIL import Image

images_dir = "downloads"
images_dir_actors = os.listdir(images_dir)

j = 1
for images_dir_actor in images_dir_actors:
    images = os.listdir(os.path.join(images_dir,images_dir_actor))
    print(images_dir_actor)
    for i,image in enumerate(images):
        img_path = os.path.join(images_dir,images_dir_actor,image)
        img = Image.open(img_path)
        img = img.resize((600,600))
        os.remove(img_path)
        print(img_path)
        img.save(os.path.join(images_dir,images_dir_actor,f"{images_dir_actor}_{j}.jpg"))
        j += 1
