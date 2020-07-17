#6201012630096,Assignment2
#----------------------------------------------------------------------
import pygame 
from random import randint
import math
#properties of circle
class circle:
    num_circle = 0
    def __init__(self):
        self.radius = randint(10,20)
        Red = randint(0,255)
        Green = randint(0,255)
        Blue = randint(0,255)
        self.color = (Red,Green,Blue)
        x_and_y = (circle.find_pos(self.radius))
        self.x = x_and_y[0]
        self.y = x_and_y[1]
        circle.num_circle += 1
        self.num_circle = circle.num_circle
        self.speedx = randint(-4,4)
        self.speedy = randint(-4,4)
    def find_pos(r):
        width = 800
        height = 600
        x = randint(r,width-r)
        y = randint(r,height-r)
        if circle.num_circle < 1 :
            return (x,y)
        else :
            count = 0
            while count < (circle.num_circle):
                run = True
                while run : 
                    #check intersection of two circle
                    cen_to_cen = ((x-cyclic[count].x)**2)+((y-cyclic[count].y)**2)
                    dist = (r+cyclic[count].radius)**2 
                    if cen_to_cen < dist :
                        x = randint(r,width-r)
                        y = randint(r,height-r)
                        count = 0
                    else:
                        run = False
                count += 1
            return (x,y)
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y    
    def total_circle(self):
        return circle.num_circle
    #hidden circle
    def remove(self):
        r = self.radius
        self.radius = 0
        self.color = (255,255,255)
        circle.num_circle -= 1
        self.num_circle = circle.num_circle
        pygame.draw.circle( surface, self.color, (self.x,self.y), r )
    def change_to_white(self):
        color = (255,255,255)
        radius = self.radius
        pygame.draw.circle( surface, color, (self.x,self.y), radius )
    def move(self):
        self.x = self.x + self.speedx
        self.y = self.y + self.speedy
    def check_bounce(self,target):
        if (((self.x-target.x)**2)+((self.y-target.y)**2) <= ((self.radius+target.radius)**2)):
            zeta1 = math.atan(self.speedy/(self.speedx+(10**-6)))
            zeta2 = math.atan(target.speedy/(target.speedx+(10**-6)))
            angle_between = math.fabs((zeta1-zeta2)*180/math.pi)
            if (50<=angle_between <= 120 or 240 >=angle_between>= 310):
                if ((self.speedx > 0) and (target.speedx>0)) or ((self.speedx < 0) and (target.speedx<0)) :
                    self.speedy = -self.speedy
                    target.speedy = -target.speedy
                else:
                    self.speedx = -self.speedx
                    target.speedx = -target.speedx
            else :
                    self.speedx = -self.speedx
                    target.speedx = -target.speedx
                    self.speedy = -self.speedy
                    target.speedy = -target.speedy
    def check_bounce_with_frame(self):
        if (((self.x-self.radius)<=0) or ((self.x+self.radius)>=800)):
            self.speedx = -self.speedx
        elif ((self.y-self.radius)<=0 or ((self.y+self.radius)>=600)):
            self.speedy = -self.speedy
def check_all_bounce():
    data_all = cyclic
    for item in range(0,len(data_all)):
        for item2 in range(item+1,len(data_all)) :
            data_all[item].check_bounce(data_all[item2])
#create circle
def create_circle(alist,count):
    some_list = alist
    some_list.append(('circle'+str(count))) #create variable e.g.total = 0,circle1
    print('circle'+str(count))
    some_list[-1] = circle()
    color = some_list[-1]#show index of circle
    color = color.color
    x = some_list[-1].x
    y = some_list[-1].y
    r = some_list[-1].radius
    pygame.draw.circle( surface, color, (x,y), r )
#check object that is biggest
def check_biggest(alist):
    data = []
    for item in range(len(alist)):
        if item == 0:
            data.append(alist[item])
        else :
            if alist[item].radius > data[0].radius:
                data = []
                data.append(alist[item])
            elif alist[item].radius > data[0].radius:
                print(item,alist[item])
                data.append(alist[item])
            else :
                pass
    return data           
cyclic = []
biggest = []
pygame.init()
N = 10
# create a screen of width=600 and height=600
scr_w, scr_h = 800, 600
screen = pygame.display.set_mode( (scr_w, scr_h) )
clock = pygame.time.Clock()
#run continous until user ask to quit
running = True
# create a new surface 
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
for item in range(1,N+1):
    create_circle(cyclic,item)
while running:
    # This limits the while loop to a max of 10 times per second.
    clock.tick( 10 )
    biggest = check_biggest(cyclic)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            print(mouse_x,mouse_y)
            #find item that near the object of circle
            for item in range(len(biggest)):
                distance = (((mouse_x-biggest[item].x)**2) + ((mouse_y-biggest[item].y)**2))
                #Is mouse  in the circle ?
                if distance <= ((biggest[item].radius)**2) :
                    #disconnect the class code in biggest then redraw with white circle and change radius to zero
                    class_code = biggest[item]
                    print(class_code)
                    biggest[item].remove()
                    biggest.remove(class_code)
                    check_biggest(biggest)
                else:
                    pass
    for item in range(len(cyclic)):
        cyclic[item].change_to_white()
        cyclic[item].move()
        pygame.draw.circle( surface, cyclic[item].color, (cyclic[item].x,cyclic[item].y),cyclic[item].radius )
    check_all_bounce()
    #White screen
    for item in range(len(cyclic)):
        cyclic[item].check_bounce_with_frame()
    screen.fill((255,255,255))
    # draw the surface on the screen
    screen.blit(surface, (0,0))
    # update the screen display
    pygame.display.update()

pygame.quit()