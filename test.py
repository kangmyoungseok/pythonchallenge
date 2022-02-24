from PIL import Image

if __name__ == "__main__" :

    with Image.open("wire.png") as img :
        tar = Image.new('RGB',(101,101))
        length = img.width

        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        direction = 0
        x = 100
        y = 99
        cur_x = 0
        cur_y = 0
        index = 0

        while(x+y>0) :
            if(direction%2==0) :
                for i in range(x) :
                    tar.putpixel((cur_x,cur_y),img.getpixel((index,0)))
                    cur_x += dx[direction]
                    index += 1
                x -= 1
            else :
                for i in range(y) :
                    tar.putpixel((cur_x,cur_y),img.getpixel((index,0)))
                    cur_y += dy[direction]
                    index += 1
                y -= 1
            direction = (direction + 1)%4

        tar.save("new_wire.png")
        tar.show()