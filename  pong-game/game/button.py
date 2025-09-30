# button class
    # start game button
    # quit game button
    # hover effect for buttons
    

import pygame
success, failure = pygame.init()
print(f"success:{success}, failed: {failure}")




class Button:
    def __init__(self, text, x, y, width, height, color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont("Arial", 30)

    def draw(self, screen):
        # draw button text 
        pygame.draw.rect(screen, self.color if not self.is_hovered() else self.hover_color, self.rect)
        # set the game text font to black color
        text_surface = self.font.render(self.text, True, "black")
        text_rect = text_surface.get_rect(center=self.rect.center)
        # add text to the screen
        screen.blit(text_surface, text_rect)

    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

    def is_clicked(self):
        return self.is_hovered() and pygame.mouse.get_pressed()[0]
        
        
        
        
    