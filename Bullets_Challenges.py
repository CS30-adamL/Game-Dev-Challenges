import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
objectarray = []
bulletarray = []
obj_num = 30
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
        print(f"player Created: X:{self.x} R:{self.r}")

    def collision(self,size):
            if self.x + self.r > size[0]:
                var = (self.x + self.r) - size[0]
                self.x -= var
            elif self.x - self.r < 0:
                var = (self.x - self.r)
                self.x -= var
    def shoot(self):
        print("shot")
        bullet = Bullet(5,self.x,self.y)
        bulletarray.append(bullet)

    def movement(self,a,d):
        if a == True and d == False:
                self.xV = -5
        elif a == False and d == True:
                self.xV = 5
        elif a== False and d == False:
            self.xV = 0
        self.x += self.xV



class Bullet:
    def __init__(self, r,x,y):
        self.xV = 0
        self.yV = -5
        self.r = r
        self.hit = False
        self.miss = False
        self.x = x
        self.y = y

    def offScreen(self):
        if self.y < 0:
            self.miss = True
    
    def bullet_hit(self,item):
            did_it_hit = item.was_shot(self.x,self.y,self.r)
            if did_it_hit == True:
                self.hit = True
            return did_it_hit
    def movement(self):
        self.y += self.yV
    
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
        self.hit = "not_hit"
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

            if self.y + self.r > size[1]/2:
                var = (self.y + self.r) - size[1]/2
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
                self.hit = "dead"
                return True
            else:
                self.hit = "alive"
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
            player.shoot()
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
    player.movement(a_pressed,d_pressed)
    player.collision(size)

    for item in objectarray:
        item.collision(size)
        item.movement()
        
    for bullet in bulletarray:
        if bullet.miss == True:
                bulletarray.pop(bulletarray.index(bullet))
        if bullet.hit == True:
                bulletarray.pop(bulletarray.index(bullet))
        bullet.movement()   
        bullet.offScreen()         
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
