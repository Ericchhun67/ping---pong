#
# paddle.py
# Eric Chhun
# 09/24/25
# demonstrates the Paddle class, which represents the player’s paddle on screen. 
# It handles the paddle’s position, size, and movement, reacting to key presses 
# (like W/S or arrow keys). The class includes methods to move up and down 
# while preventing the paddle from going outside the game window. It also has a 
# draw method, which renders the paddle as a rectangle so it’s visible on the 
# screen. In Pong, the paddle interacts with the ball through collision 
# detection, so the class needs a way to check and update when the ball 
# bounces off. By keeping the paddle code separate, the game becomes more 
# organized and easier to expand later—for example, you can tweak paddle speed, 
# add AI for single-player mode, or change its appearance without touching 
# other files.


import pygame
success, failure = pygame.init()
print(f"init:{success}, failed: {failure}")


class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.x = x # x position of the paddle
        self.y = y # y position of the paddle
        self.width = width # width of the paddle
        self.height = height # height of the paddle
        self.speed = speed # speed of the paddle
        # create a rectangle for the paddle
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    # a function to move the paddle up and down using the keyboard and handle
    # boundary to prevent the paddle from going out of bounds
    def move_paddle(self, keys, up_key, down_key, screen_height):
        if keys[up_key] and self.rect.top > 0: # if the up key is pressed and 
        # the paddle is not at the top of the screen
            self.rect.y -= self.speed # move the paddle up
            self.y = self.rect.y
            print("moving up")
        if keys[down_key] and self.rect.bottom < screen_height:
            self.rect.y += self.speed
            self.y = self.rect.y
            print("moving down")
        if keys[pygame.K_ESCAPE]:
            print("Exiting game")
            pygame.quit()
            exit()
    
    # A function to draw the paddle on the screen
    def draw_paddle(self, screen):
        pygame.draw.rect(screen, ("white"), self.rect) # draw the paddle as a
        # white rectangle
    


class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y):
        self.x = x # x position of the ball
        self.y = y # y position of the ball
        self.radius = radius # radius of the ball
        self.speed = [speed_x, speed_y] # speed of the ball in x and y direction
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, 
        self.radius * 2, self.radius * 2)
        
    
    # a function to move the ball
    def move_ball(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius
        print(f"ball position: {self.x}, {self.y}")
        
    def hit_paddle(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.speed[0] = -self.speed[0]
            print("Ball hit paddle")
        
    # A function to draw the ball on the screen
    def draw_ball(self, screen):
        pygame.draw.circle(screen, ("red"), (self.x, self.y), self.radius)
        
  
  
# create a second paddle class for the opponent
class OpponentPaddle:
    def __init__(self, x, y, width, height, speed):
        self.x = x # X position of the paddle
        self.y = y # Y position of the paddle
        self.width = width # Width of the paddle
        self.height = height # Height of the paddle
        self.speed = speed # Speed of the paddle
        # Create a rectangle for the paddle
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    
    # A function to move the paddle up and down using the keyboard
    def move_paddle_opponent(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0: 
            self.rect.y -= self.speed
            self.y = self.rect.y
            print("Up arrow key is pressed")
        if keys[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.speed
            self.y = self.rect.y
            print("Down arrow key is pressed")
        
        
        
      
            
        
    # A function to draw the paddle on the screen
    def draw_paddle(self, screen):
        pygame.draw.rect(screen, ("white"), self.rect)