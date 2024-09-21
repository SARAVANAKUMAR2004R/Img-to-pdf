from PIL import Image
import os
initial_location="D:\\images"
destination="E:\\img_out.pdf"
z=[]
for i in os.listdir(initial_location):
    if i.endswith((".jpeg","jpg","png")):
        img_path=os.path.join(initial_location,i)
        img=Image.open(img_path)
        img1=img.convert("RGB")
        z.append(img1)
if len(z)!=0:
    z[0].save(destination,save_all=True,append_images=z[1:])