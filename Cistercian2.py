from PIL import Image, ImageOps
import math

f=open("text.txt","r")
text=f.read()

textasc=""
for n in text:
    textasc += str(ord(n))
print(textasc)
size=int((len(textasc)))
numsize=math.ceil(size/4)
if numsize>10:
    width=10
    hight=math.ceil(numsize/10)
else:
    width=numsize
    hight=1

print(hight)


print(math.sqrt(int(numsize)))
backsize=(65*width,65*hight)
print(size,numsize,backsize)

background =Image.new("L",backsize, color=255)


# Read image 
im0 = Image.open('0.png')
im1 = Image.open('1.png')
im2 = Image.open('2.png')
im3 = Image.open('3.png')
im4 = Image.open('4.png')
im5 = Image.open('5.png')
im6 = Image.open('6.png')
im7 = Image.open('7.png')
im8 = Image.open('8.png')
im9 = Image.open('9.png')
array= [im0,im1,im2,im3,im4,im5,im6,im7,im8,im9]
xpos=0
ypos=0
print(textasc)
for n in range (0, size,4):
    
    im0 = Image.open('0.png')
    number=0
    img=im0
    aux=im0

    number=textasc[n:n+4]
    
    number= str(number)[::-1]
    for i in range (len(number)):      
        aux=array[int(number[i])] 
        if i==1:
            aux=ImageOps.mirror(aux)
            
        if i==2:
            aux=ImageOps.flip(aux)
            
        if i==3:
            aux =aux.rotate(180)
        img.paste(aux, (0, 0), aux)
        
    background.paste(img,(xpos, ypos),img)
    xpos+=65
    if xpos==650:
        xpos=0
        ypos+=65
# Output Images 
img.save('result.png', quality=95)

background.save('back.png', quality=95)
background.show()

f.close()
