from PIL import Image, ImageOps




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

while True:
    im0 = Image.open('0.png')
    number=0
    img=im0
    aux=im0
    number=int((input("enter a number ")))
     
        
    while True:
        
        if number > 9999:        
            number=int(input("enter a number lower than 9999 "))   
        elif number <0:
            number=int(input("enter a number higher than 0 ")) 
        else:
            break
    
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
    # Output Images 
    img.save('result.png', quality=95)
    img.show()
