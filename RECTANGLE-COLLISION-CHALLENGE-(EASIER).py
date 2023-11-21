

import pygame
import math
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


import random
global Mouse_Click_X,Mouse_Click_Y

Mouse_Clicked = 0
Mouse_Click_Hit = 0
objectarray = []
text = f"clicks: 0 || Hits: 0 || acurracy: 0"


def make_obj():
    for num in range(15):
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
        self.hit = 0
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
                return 1
            else:
                return 0
        elif self.type == "rect":
            if self.x - self.D1/2 < coordinates[0] and self.x > coordinates[0] and self.y - self.D2/2 < coordinates[1] and self.y > coordinates[1]:
                return False
            else:
                return 0


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
            Mouse_Clicked += 1
            text = f"clicks: {Mouse_Clicked} || Hits: {Mouse_Click_Hit} || acurracy: {Mouse_Click_Hit/Mouse_Clicked}"
            print("mouse clicked")
            mouse_found(mouse_pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_button = False

def mouse_found(mouse_pos):
    for item in objectarray:
        if item.was_hit(mouse_pos) == 1:
            item.hit = 1

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1000, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
make_obj()
# -------- Main Program Loop -----------
while not done:


    # --- Main event loop
    done == actionDetection()  # Flag that we are done so we exit this loop   
    # --- Game logic should go here
    for item in objectarray:
        if item.hit == False:
            print("game over")
        elif item.hit == 1:
            objectarray.pop(objectarray.index(item))
            Mouse_Click_Hit += 1
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


    # #pygame.draw.rect(Surface, color, Rect, width=0): return Rect
    # #pygame.draw.rect(screen, RED, [55, 50, 20, 25], 0)
    # # Draw on the screen a green line from (0, 0) to (100, 100)
    # # that is 5 pixels wide.
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # # Draw on the screen several lines from (0,10) to (100,110)
    # # 5 pixels wide using a for loop
    # for y_offset in range(0, 100, 10):
    #     pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5)




    # for i in range(200):
        
    #     radians_x = i / 20
    #     radians_y = i / 6
        
    #     xx = int(75 * math.sin(radians_x)) + 200
    #     yy = int(75 * math.cos(radians_y)) + 200
        
    #     pygame.draw.line(screen, BLACK, [xx,yy], [xx+5,yy], 5)

    # # This draws a triangle using the polygon command
    # pygame.draw.polygon(screen, BLACK, [[100,100], [0,200], [200,200]], 5)
    # # Draw an ellipse, using a rectangle as the outside boundaries
    # pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)  
    # # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
    
     # Render the text. "True" means anti-aliased text.
     # Black is the color. The variable BLACK was defined
     # above as a list of [0, 0, 0]
     # Note: This line creates an image of the letters,
     # but does not put it on the screen yet.
    text = font.render(str(text),True,BLACK)
    
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [450, 10])




    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()



# '''
# from pynput import keyboard
# import time

# repeat_times = 100
# delay_between_press = .01
# time_till_stop = 1
# def on_press(key):
#     print(key)
#     if key == keyboard.Key.space:

#         press_enter(repeat_times, delay_between_press, time_till_stop)



# def press_enter(num_presses, delay, duration):

#     start_time = time.time()

#     end_time = start_time + duration



#     while time.time() < end_time:

#         for _ in range(num_presses):

#             keyboard.Controller().press(keyboard.Key.enter)

#             time.sleep(delay)

#             keyboard.Controller().release(keyboard.Key.enter)



# # Create a listener

# listener = keyboard.Listener(on_press=on_press)

# # Start the listener

# listener.start()

# # Wait for the listener to stop (e.g., by pressing Ctrl+C)

# listener.join()

# '''
# from pynput import keyboard
# import time

# repeat_times = 100
# delay_between_press = .01
# time_till_stop = 1
# def on_press(key):
#     print(key)
#     if key == keyboard.Key.caps_lock:

#         press_enter(repeat_times, delay_between_press, time_till_stop)



# def press_enter(num_presses, delay, duration):

#     start_time = time.time()

#     end_time = start_time + duration



#     while time.time() < end_time:

#         for _ in range(num_presses):

#             keyboard.Controller().press("w")

#             time.sleep(delay)

#             keyboard.Controller().release("w")



# # Create a listener

# listener = keyboard.Listener(on_press=on_press)

# # Start the listener

# listener.start()

# # Wait for the listener to stop (e.g., by pressing Ctrl+C)

# listener.join()
