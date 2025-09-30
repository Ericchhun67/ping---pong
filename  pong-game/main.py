# Entry point (runs the game loop)
 
 
import pygame
import sys
from game.setting import height, width
from game.paddle import Paddle, Ball, OpponentPaddle
from game.button import Button
success, failure = pygame.init()
print(f"init:{success}, failed: {failure}")



try:
    # create a game window and set its full screen
    SCREEN = pygame.display.set_mode((height, width), pygame.RESIZABLE)
    # title and icon for the game window
    pygame.display.set_caption("Pong Game")
    # game icon
except Exception as e:
    print(f"Error opening the game window: {e}")
    exit()
finally:
    print("Pygame window setup attempted.")

# Create a start button
start_button = Button('Start Game', width // 2 - 100, height // 2 - 50, 200, 100, "green", "blue")
exit_button = Button('Exit', width // 2 - 100, height // 2 + 60, 200,100, "green", "red")
resume_button = Button('Resume', width // 2 - 100, height // 2 - 50, 200, 100, "green", "blue")
pause_exit = Button('Pause', width // 2 - 100, height // 2 + 60, 200, 100, "green", "blue")




def main_menu(): # A function to display the main menu
    running = True
    main_menu, gameplay, game_over = "main_menu", "game_play", "game_over"
    state = main_menu
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        SCREEN.fill(("white"))
        
        start_button.draw(SCREEN)
        exit_button.draw(SCREEN)
        
        if start_button.is_clicked():
            break # Exit to the game menu
            
        
        if exit_button.is_clicked():
            pygame.quit()
            sys.exit()
        
        pygame.display.flip()

# a function to display the score on the player's screen and opponent's screen.
# draw a line in the middle of the screen
def draw_score(player_score, opponent_score):
    font = pygame.font.Font(None, 74)
    player_text = font.render(str(player_score), True, (255, 255, 255))
    opponent_score_text = font.render(str(opponent_score), True, (255, 255, 255))
    SCREEN.blit(player_text, (width // 4 - player_text.get_width() // 2, 10))
    SCREEN.blit(opponent_score_text, (3 * width // 4 - opponent_score_text.get_width() // 2, 10))
    pygame.draw.line(SCREEN, (255, 255, 255), (width // 2, 0), (width // 2, height), 5)
    

def count_down_timer():
    font = pygame.font.Font(None, 74)
    # Loop for 3 seconds countdown
    for i in range(3, 0, -1):
        SCREEN.fill((0,0,0)) # Clear the screen
        count_down_text = font.render(str(i), True, (255, 255, 255))
        SCREEN.blit(count_down_text, (width // 2 - count_down_text.get_width() // 2, height // 2 - count_down_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(1000)
        
        
# a function to display the gameover screen
def game_over():
    #  game over screen will only show when one player reaches 10 points
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        SCREEN.fill(("Blue"))
        
        exit_button.draw(SCREEN)
        
        # if exit button is clicked, quit the game
        if exit_button.is_clicked():
            pygame.quit()
            sys.exit()
    


    
    
    
def main():
    run = True # set the game loop to run
    # create a bool main menu variable
    menu_active = True
    # create a bool game variable to show the game screen
    game_active = False
    
    game_is_over = False
    
    
    
    # call the paddle class
    paddle = Paddle(50, height// 2 - 60, 20, 120, 10) # create a paddle object
    # call the Ball class
    ball = Ball(width // 2, height // 2, 15, 7, 7) # Create a ball object
    # call the opponent paddle class
    opponentpaddle = OpponentPaddle(width - 70, height // 2 - 60, 20, 120, 12)
    main_menu()
    count_down_timer() # call the countdown timer function
    player_score = 0
    opponent_score = 0
    
    
    while run: # game loop
        for event in pygame.event.get(): # iterate through all the events
            if event.type == pygame.QUIT: # check if the event is quit
                run = False # if so, set run to false to exit the loop
                pygame.quit() # quit pygame
                exit()
        
            if game_active == False:
                # fill the screen with black color
                SCREEN.fill(("black"))
                # show the game screen if start button is clicked
                if start_button.is_clicked():
                    game_active = True
                    menu_active = False
               
                # get the keys pressed
                keys = pygame.key.get_pressed()
                # move the paddle using w/s keys and draw it on the screen
                paddle.move_paddle(keys, pygame.K_w, pygame.K_s, height)
                paddle.draw_paddle(SCREEN)
                
                
                ball.move_ball() # move the ball
                ball.draw_ball(SCREEN) # draw the ball on the screen
                ball.hit_paddle(paddle)
                
                
                opponentpaddle.move_paddle_opponent()
                opponentpaddle.draw_paddle(SCREEN)
                
                draw_score(player_score, opponent_score)
                
                
            # if the game is over, show the game over screen
            if game_is_over == True:
                game_over()
                
            
            
                
        
        
        pygame.display.update() # update the display window
        pygame.time.Clock().tick(60) # set the frame rate to 60 FPS
if __name__ == "__main__":
    main() # run the main function
    
        
        

        
        
        
        
    

