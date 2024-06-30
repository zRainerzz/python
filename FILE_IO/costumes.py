import sys
from PIL import Image

images=[]
for arg in sys.argv[1:]:#which leans start at location 1 not zero and take a slice till the end, in other word, give me everything except the first thing.
    image= Image.open(arg)
    images.append(image)
    
images[0].save(
    "costume.gif", save_all=True,append_images=[images[1]], duration=200,loop=0#it means loop*0 times which will be refered to forever
)