import pygame
import random
num = 0
def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    # Game Variables
    walls = makeWalls(250)
    player= Player("green",500,500,30,30,"player")

    # or not playerx + player.W > wall.X,  if not playerx < wall.X + wall.W
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.jump()

        # LOGIC
        player.update(walls)

        # DRAWING
        screen.fill("white")

        for rc in walls:
            rc.draw(screen,player.X,player.Y)
       
        player.draw(screen)
     

        pygame.display.flip()
        dt = clock.tick(60) / 1000


    pygame.quit()



class Wall:
    def __init__(self,color,Xlocation,Ylocation,width,length,type):
        self.color = color
        self.X = Xlocation
        self.Y = Ylocation
        self.W = width
        self.H = length
        self.type = type
   
    def draw(self, screen,playerx,playery):
        viewx = playerx - 500
        viewy = playery -500

        pygame.draw.rect(screen,self.color,[self.X - viewx,self.Y - viewy,self.W,self.H])


class Player:
    def __init__(self,color,Xlocation,Ylocation,width,length,type):
        self.color = color
        self.X = Xlocation
        self.Y = Ylocation
        self.W = width
        self.H = length
        self.dx = 5
        self.dy = 0
        self.gravity = 0.4
        self.launchSpeed = -16
        self.type = type
        self.dir = "right"
   
    def jump(self):
        if self.dy == 0:
            self.dy = self.launchSpeed

    def update(self, walls):
        # Horizontal Movement
        keys = pygame.key.get_pressed()        
        if keys[pygame.K_a]:
            self.X += -self.dx
       
            self.dir = "left"
            self.runCollision(walls)
        elif keys[pygame.K_d]:
            self.X += self.dx
       
            self.dir = "right"
            self.runCollision(walls)
       
        # Vertical Movement
        self.dy += self.gravity
        self.Y += self.dy
        if self.dy > 0:
            self.dir = "down"
        elif self.dy < 0:
            self.dir = "up"
        self.runCollision(walls)
   
    def runCollision(self, walls):
        for wall in walls:
            if (rectCollide(self, wall)):
                if self.dir == "down":
                    # Moving down
                    self.Y = wall.Y - self.H
                    self.dy = 0
                elif self.dir == "up":
                    self.Y = wall.Y + wall.H
                    self.dy = 0
                elif self.dir == "left" :
                    self.X = wall.X + wall.W
                elif self.dir == "right" :
                    self.X = wall.X - self.W
           
    def draw(self, screen):
        viewx = self.X - 500
        viewy = self.Y -500
        pygame.draw.rect(screen,self.color,[self.X - viewx ,self.Y- viewy,self.W,self.H])
   

   
def rectCollide(rect1, rect2) :
 
  return (
    rect1.X < rect2.X + rect2.W and
    rect1.X + rect1.W > rect2.X and
    rect1.Y + rect1.H > rect2.Y and
    rect1.Y < rect2.Y + rect2.H
  )


   

def makeWalls(num_walls):
    temp = []
    i = 0
    while i < num_walls:
        xlocation = random.randint(-1000,1500)
        ylocation = random.randint(-5000,1000)
        width = random.randint(40,60)
        height = random.randint(50,80)
        temp.append(Wall("red",xlocation,ylocation,width,height,"rect"))
        i+=1
    temp.append(Wall("black", 0, 900, 1000, 100, "rect"))
    return temp


# Call main to begin program
main()
