

import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Making objects
def make_obj():
    
    for num in range(obj_num):
        num = Obj("food",random.randint(10,30),0)
        objectarray.append(num)

class Player:
    def __init__(self, type, r,D2):
        self.type = type
        self.r = r
        self.D2 = D2
        self.hit = "alive"
        self.x = size[0]/2
        self.y = size[1]/2
        print(f"player Created: X:{self.x} Y:{self.y} R:{self.r}")


    def collision(self,size):
        if self.type == "player":
            if self.x + self.r > size[0]:
                var = (self.x + self.r) - size[0]
                self.x -= var
            elif self.x - self.r < 0:
                var = (self.x - self.r)
                self.x -= var
            if self.y + self.r > size[1]:
                var = (self.y + self.r) - size[1]
                self.y -= var
            elif self.y - self.r < 0:
                var = (self.y - self.r)
                self.y -= var
      
class Obj:
    def __init__(self,type, r,D2):
        self.r = r
        self.type = type
        self.D2 = D2
        self.eaten = "alive"
        self.x = random.randint(0,1000)
        self.y = random.randint(0,1000)

    def collision(self,size):
            if self.x + self.r > size[0]:
                var = (self.x + self.r) - size[0]
                self.x -= var
            elif self.x - self.r < 0:
                var = (self.x - self.r)
                self.x -= var
            if self.y + self.r > size[1]:
                var = (self.y + self.r) - size[1]
                self.y -= var
            elif self.y - self.r < 0:
                var = (self.y - self.r)
                self.y -= var

    def was_eaten(self, playerx,playery,player_r):
            dx = self.x - playerx
            dy = self.y - playery
            distance = (dx * dx + dy * dy)**0.5
            if distance - player_r < self.r:
                self.eaten = "dead"
            else:
                self.eaten = "alive"
       
def actionDetection():
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            print("User asked to quit.")
            pygame.quit()
            return True
        
def mouse_found(playercharacter):
    for item in objectarray:
        item.was_eaten(playercharacter.x,playercharacter.y,playercharacter.r)

pygame.init()
objectarray = []
obj_num = 30
size = (1000, 800)
playercharacter = Player("player",20,0)
done = False
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()
make_obj()
# -------- Main Program Loop -----------
while not done:

    # --- Main event loop
    done == actionDetection() 
    # --- Game logic should go here
    mouse_pos = pygame.mouse.get_pos() 
    playercharacter.x = mouse_pos[0]
    playercharacter.y = mouse_pos[1]
    if len(objectarray) < 25:
        objectarray.append(Obj("food",random.randint(10,30),0))

    mouse_found(playercharacter)
    playercharacter.collision(size)
    for item in objectarray:
        if item.eaten == "dead":
            dead_food = objectarray.pop(objectarray.index(item))
            playercharacter.r += dead_food.r / 12
        item.collision(size)
    # --- Screen-clearing code goes here
    screen.fill(WHITE)
    # --- Drawing code should go here
    for item in objectarray:
        if item.type == "food":
            pygame.draw.circle(screen,GREEN,[item.x,item.y],item.r,0)
    pygame.draw.circle(screen,BLACK,[playercharacter.x,playercharacter.y],playercharacter.r,0)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()


