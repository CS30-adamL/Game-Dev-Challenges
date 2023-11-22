

import pygame
import math
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


import random

Mouse_Clicked = 0
Mouse_Click_Hit = 0
game_over_msg = ""

objectarray = []
def notdzero():
    try:
        acurracy = Mouse_Click_Hit/Mouse_Clicked
        return acurracy
    except ZeroDivisionError:
        return 0


# msg = f"clicks: {Mouse_Clicked} || Hits: {Mouse_Click_Hit} || acurracy: {Mouse_Click_Hit/Mouse_Clicked}"
msg = f"clicks: {Mouse_Clicked} || Hits: {Mouse_Click_Hit} || acurracy: {notdzero()}"
 
obj_num = 1500

# Making objects
def make_obj():
    for num in range(obj_num):
        num = Obj("circle",random.randint(10,50),0)
        objectarray.append(num)
        num = Obj("rect",random.randint(50,100),random.randint(50,100))
        objectarray.append(num)

class Obj:
    def __init__(self, type, D1,D2):
        self.type = type
        self.xV = random.randint(1,3)
        self.yV = random.randint(1,3)
        self.D1 = D1
        self.D2 = D2
        self.hit = "not_hit"
        self.x = random.randint(0,1000)
        self.y = random.randint(0,1000)
        print(f"Obj Created: Type:{self.type}  VX: {self.xV} VY: {self.yV} D1: {self.D1} D2: {self.D2}\n")

    def movement(self):
        self.x += self.xV
        self.y += self.yV
    def collision(self,size):
        if self.type == "circle":
            if self.x + self.D1 > size[0]:
                var = (self.x + self.D1) - size[0]
                self.x -= var
                self.xV = -1 * self.xV 
            elif self.x - self.D1 < 0:
                var = (self.x - self.D1)
                self.x -= var
                self.xV = -1 * self.xV

            if self.y + self.D1 > size[1]:
                var = (self.y + self.D1) - size[1]
                self.y -= var
                self.yV = -1 * self.yV
            elif self.y - self.D1 < 0:
                var = (self.y - self.D1)
                self.y -= var
                self.yV = -1 * self.yV

        elif self.type == "rect":
            if self.x - (self.D1/2) < 0:
                var = self.x - (self.D1/2)
                self.x -= var
                self.xV = -1 * self.xV
            elif self.x  > size[0]:
                var = self.x - size[0]
                self.x -= var
                self.xV = -1 * self.xV
            if self.y - (self.D2/2) < 0:
                var = self.y - (self.D2/2)
                self.y -= var
                self.yV = -1 * self.yV
            elif self.y > size[1]:
                var = self.y - size[1]
                self.y -= var
                self.yV = -1 * self.yV
                
    def was_hit(self, coordinates):
        if self.type == "circle":
            dx = self.x - coordinates[0]
            dy = self.y - coordinates[1]
            distance = (dx * dx + dy * dy)**0.5
            if distance < self.D1:
                self.hit = "hit"
            else:
                self.hit = "not_hit"
        elif self.type == "rect":
            if self.x - self.D1/2 < coordinates[0] and self.x > coordinates[0] and self.y - self.D2/2 < coordinates[1] and self.y > coordinates[1]:
                self.hit = "Game_over"
            else:
                self.hit = "not_hit"



def game_over(W_or_L):
    global game_over_msg
    if W_or_L == "L":
        for item in objectarray:
            objectarray.remove(item)

        game_over_msg = "YOU LOSE"
    elif W_or_L == "W":
        game_over_msg = "YOU WIN!!"


def actionDetection():

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
            mouse_found(mouse_pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_button = False

def mouse_found(mouse_pos):
    global Mouse_Clicked
    Mouse_Clicked += 1
    for item in objectarray:
        item.was_hit(mouse_pos)
pygame.init()
size = (1000, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

done = False
 
clock = pygame.time.Clock()
make_obj()
# -------- Main Program Loop -----------
while not done:


    # --- Main event loop
    done == actionDetection()  # Flag that we are done so we exit this loop   
    # --- Game logic should go here
    for item in objectarray:
        
        if item.hit == "Game_over":
           game_over("L") 
        elif item.hit == "hit":
            objectarray.pop(objectarray.index(item))
            Mouse_Click_Hit += 1
            if Mouse_Click_Hit == obj_num:
                game_over("W")
        item.movement()
        item.collision(size)
    # --- Screen-clearing code goes here
    screen.fill(WHITE)

    # --- Drawing code should go here
    for item in objectarray:
        if item.type == "circle":
            pygame.draw.circle(screen,GREEN,[item.x,item.y],item.D1,5)
        if item.type == "rect":
            pygame.draw.rect(screen,RED,[item.x - (item.D1/2), item.y - (item.D2/2),(item.D1/2),(item.D2/2)],5)

    msg = f"clicks: {Mouse_Clicked} || Hits: {Mouse_Click_Hit} || acurracy: {notdzero()}"
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(msg,True,BLACK)
    screen.blit(text, [450, 10])

    font = pygame.font.SysFont('Calibri', 100, True, False)
    loss_msg = font.render(game_over_msg,True,BLACK)
    screen.blit(loss_msg, [300, 390])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()


