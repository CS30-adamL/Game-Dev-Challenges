import pygame
import random
import math
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
objectarray = []
bulletarray = []
obj_num = 50
size = (1000, 800)
done = False
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
w_pressed = False
a_pressed = False
s_pressed = False
d_pressed = False
# Making objects
def make_obj():
    
    for num in range(obj_num):
        num = Obj(random.randint(10,30))
        objectarray.append(num)

class Player:
    def __init__(self, r):
        self.xV = 0
        self.r = r
        self.x = 400
        self.y = size[1] - 50
        self.dir = "Up"
        print(f"player Created: X:{self.x} R:{self.r}")

    def collision(self,size):
            if self.x + self.r > size[0]:
                var = (self.x + self.r) - size[0]
                self.x -= var
            elif self.x - self.r < 0:
                var = (self.x - self.r)
                self.x -= var
    def shoot(self,mouse_pos):
        print("shot")
        bullet = Bullet(5,self.x,self.y,mouse_pos)
        bulletarray.append(bullet)

    def movement(self,a,d,w,s):
        if w or a or s or d == True: 
            if a == True and d == False :
                self.xV = -5
                self.yV = 0
                self.dir = "Left"
            elif a == False and d == True:
                self.xV = 5
                self.dir = "Right"
            else:
                self.xV = 0
            if w == True and s == False:
                self.yV = -5
                self.dir = "Up"
            elif w == False and s == True:
                self.yV = 5
                self.dir = "Down"
            else:
                self.yV = 0
        else:
            self.xV = 0
            self.yV = 0



class Bullet:
    def __init__(self, r,x,y,dir):
        self.dir = dir
        self.xV = 5
        self.yV = 5
        self.r = r
        self.hit = False
        self.miss = False
        self.x = x
        self.y = y
    
    def offScreen(self,size):
        if self.y < 0 or self.y > size[1] or self.x < 0 or self.x > size[0]:
            self.miss = True


    
    def bullet_hit(self,item):
            did_it_hit = item.was_shot(self.x,self.y,self.r)
            if did_it_hit == True:
                self.hit = True
            return did_it_hit
    
    def movement(self):
        dx = self.x - self.dir[0]
        dy = self.y - self.dir[1]
        distance = (dx * dx + dy * dy)**0.5
        # angle = math.acos(dx/distance)
        # if distance > self.r:
        
        if dx > 0:
            self.x += self.xV * (dx/dy)
        elif dx < 0:
            self.x -= self.xV * (dx/dy)
        if dy < 0:
            self.y -= self.yV * (dy/dx)
        elif dy > 0:
            self.y += self.yV * (dy/dx)

    
# Making objects
def make_obj():
    for num in range(obj_num):
        num = Obj(random.randint(10,50))
        objectarray.append(num)
class Obj:
    def __init__(self, r):
        self.xV = random.randint(1,3)
        self.yV = random.randint(1,3)
        self.r = r
        self.x = random.randint(0,1000)
        self.y = random.randint(0,1000)
        print(f"Obj Created:   VX: {self.xV} VY: {self.yV} r: {self.r} \n")

    def movement(self):
        self.x += self.xV
        self.y += self.yV
    def collision(self,size):
            if self.x + self.r > size[0]:
                var = (self.x + self.r) - size[0]
                self.x -= var
                self.xV = -1 * self.xV 
            elif self.x - self.r < 0:
                var = (self.x - self.r)
                self.x -= var
                self.xV = -1 * self.xV

            if self.y + self.r > size[1]:
                var = (self.y + self.r) - size[1]
                self.y -= var
                self.yV = -1 * self.yV
            elif self.y - self.r < 0:
                var = (self.y - self.r)
                self.y -= var
                self.yV = -1 * self.yV      

    def was_shot(self, playerx,playery,player_r):
            dx = self.x - playerx
            dy = self.y - playery
            distance = (dx * dx + dy * dy)**0.5
            if distance - player_r < self.r:
                return True
            else:
                return False
       
def actionDetection():
    global w_pressed,a_pressed,s_pressed,d_pressed
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            print("User asked to quit.")
            pygame.quit()
            return True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos() 
            print(mouse_pos)
            mouse_button = True
            print("mouse clicked")
            player.shoot(mouse_pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_button = False
        elif event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "w":
                w_pressed = True
            if pygame.key.name(event.key) == "a":
                a_pressed = True
            if pygame.key.name(event.key) == "s":
                s_pressed = True
            if pygame.key.name(event.key) == "d":
                d_pressed = True
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
            print("User let go of a key.")
        


player = Player(20)
make_obj()
# -------- Main Program Loop -----------
while not done:

    # --- Main event loop
    done == actionDetection() 
    # --- Game logic should go here
    mouse_pos = pygame.mouse.get_pos() 
    player.movement(a_pressed,d_pressed,w_pressed,s_pressed)
    player.collision(size)
    player.x += player.xV
    player.y += player.yV
    for item in objectarray:
        item.collision(size)
        item.movement()
        
    for bullet in bulletarray:
        if bullet.miss == True:
                bulletarray.pop(bulletarray.index(bullet))
        if bullet.hit == True:
                bulletarray.pop(bulletarray.index(bullet))
        bullet.movement()   
        bullet.offScreen(size)         
        for item in objectarray:
            hit = bullet.bullet_hit(item)
            if hit == True:
                objectarray.pop(objectarray.index(item))
    if len(objectarray) == 0:
        print("WIN!")
        make_obj()
    # --- Screen-clearing code goes here
    screen.fill(WHITE)
    # --- Drawing code should go here
    pygame.draw.circle(screen,BLACK,[player.x,player.y],player.r,0)
    for item in objectarray:
       pygame.draw.circle(screen,GREEN,[item.x,item.y],item.r,0)
    for bullet in bulletarray:
        pygame.draw.circle(screen,RED,[bullet.x,bullet.y],bullet.r,0)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()


#  for item in objectarray:
#         for bullet in bulletarray:
#             if bullet.miss == True:
#                 bulletarray.pop(bulletarray.index(bullet))
#             if bullet.hit == True:
#                 bulletarray.pop(bulletarray.index(bullet))
#             bullet.movement()                
#             bullet.bullet_hit(item)
#         if item.hit == "dead":
#             dead_food = objectarray.pop(objectarray.index(item))
#         item.collision(size)