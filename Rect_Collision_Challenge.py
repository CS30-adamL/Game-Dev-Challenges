

import pygame
import math
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# make true for the easier version
tp = False



import random

w_pressed = False
a_pressed = False
s_pressed = False
d_pressed = False
space_pressed = False
objectarray = []

obj_num = 30

# Making objects
def make_obj(x,y,w,h):
        num = Obj(x,y,w,h)
        objectarray.append(num)

class Player:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.xV = 5
        self.yV = 5
        self.hitting = False
    
    def movement(self,w,a,s,d):
        # print(w,a,s,d,self.xV,self.yV)
        if w or a or s or d == True: 
            if a == True and d == False :
                self.xV = -5
            elif a == False and d == True:
                self.xV = 5
            else:
                self.xV = 0
            if w == True and s == False:
                self.yV = -5
            elif w == False and s == True:
                self.yV = 5
            else:
                self.yV = 0
        else:
            self.xV = 0
            self.yV = 0
    
    def collision_Wall(self,size):
            if self.x - (self.w) < 0:
                var = self.x - (self.w)
                self.x -= var
            elif self.x  > size[0]:
                var = self.x - size[0]
                self.x -= var
            if self.y - (self.h) < 0:
                var = self.y - (self.h)
                self.y -= var
            elif self.y > size[1]:
                var = self.y - size[1]
                self.y -= var
    
    def collision_Player(self,wall,tp):
        if self.x + (self.w) > wall.x and self.x < wall.x + wall.w and self.y + (self.h) > wall.y and self.y < wall.y + wall.h and tp == True:
            tp_mode()
       
        if self.x + (self.w) > wall.x and self.x < wall.x + wall.w and self.y + (self.h) > wall.y and self.y < wall.y + wall.h and tp == False:
            collision = {'top': False, 'bottom': False,'right': False,'left': False}
            if self.y + self.h > wall.y and self.y < wall.y:
                collision['top'] = True
            elif self.y < wall.y + wall.h and self.y + self.h/2 > wall.y + wall.h:
                collision['bottom'] = True
            if self.x + self.w > wall.x and self.x < wall.x - self.w/1.5:
                collision['left'] = True
            elif self.x < wall.x + wall.w and self.x + self.w/2  > wall.x + wall.w :
                collision['right'] = True
            

            if self.xV > 0 and collision['left']:
                self.xV = 0
                var = self.x + (self.w) - wall.x
                self.x -= var               
            elif self.xV < 0 and collision['right']:
                self.xV = 0
                var = self.x - (wall.x + wall.w)
                self.x -= var 
            if self.yV < 0 and collision['bottom']:
                var = self.y - (wall.y + wall.h)
                self.y -= var
                self.yV = 0
            elif self.yV > 0 and collision['top']:
                var = self.y + self.h - wall.y
                self.y -= var
                self.yV = 0
            print(collision)
        
class Obj:
    def __init__(self,x,y,w,h):
        self.x = x 
        self.y = y
        self.w = w
        self.h = h
        self.hitting = False
        print(f"Obj Created: x:{self.x} y: {self.y} w: {self.w} h: {self.h}\n")


    def collision_Wall(self,size):
            if self.x - (self.w) < 0:
                var = self.x - (self.w)
                self.x -= var
            elif self.x  > size[0]:
                var = self.x - size[0]
                self.x -= var
            if self.y - (self.h) < 0:
                var = self.y - (self.h)
                self.y -= var
            elif self.y > size[1]:
                var = self.y - size[1]
                self.y -= var
    

def tp_mode():
    player.x = 0
    player.y = 0

def actionDetection():
    global w_pressed,a_pressed,s_pressed,d_pressed,space_pressed
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            print("User asked to quit.")
            pygame.quit()
            return True
        elif event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "w":
                w_pressed = True
            if pygame.key.name(event.key) == "a":
                a_pressed = True
            if pygame.key.name(event.key) == "s":
                s_pressed = True
            if pygame.key.name(event.key) == "d":
                d_pressed = True
            if pygame.key.name(event.key) == "space":
                space_pressed = True
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            if pygame.key.name(event.key) == "w":
                w_pressed = False
            if pygame.key.name(event.key) == "a":
                a_pressed = False
            if pygame.key.name(event.key) == "s":
                s_pressed = False
            if pygame.key.name(event.key) == "d":
                d_pressed = False
            if pygame.key.name(event.key) == "space":
                space_pressed = False
            print("User let go of a key.")

pygame.init()
size = (1000, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
player = Player(0,0,20,20)
# make_obj(100,00,50,1000)
# make_obj(900,00,50,1000)
make_obj(0,750,1000,100)
# make_obj(0,200,1000,50)
make_obj(500,400,200,200)
for i in range(0,10):
    make_obj(random.randint(50,750),random.randint(50,750),random.randint(10,100),random.randint(10,100))
done = False


clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:


    # --- Main event loop
    done == actionDetection()  # Flag that we are done so we exit this loop   
    # --- Game logic should go here
    # print(player.x,player.xV,player.y,player.yV)
    player.movement(w_pressed,a_pressed,s_pressed,d_pressed)
    player.x += player.xV
    player.y += player.yV

    for item in objectarray:
        # item.collision_Wall(size)
        player.collision_Player(item,tp)
        player.collision_Wall(size)
        
    # --- Screen-clearing code goes here
    screen.fill(WHITE)

    # --- Drawing code should go here
    for item in objectarray:
            pygame.draw.rect(screen,RED,[item.x, item.y,(item.w),(item.h)],0)
    pygame.draw.rect(screen,BLACK,[player.x,player.y,player.w,player.h],0)
   
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()



