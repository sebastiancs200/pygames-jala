import pygame 
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH

class Spaceship(Sprite):
    X_POS=(SCREEN_WIDTH// 2)-40
    Y_POS=500

    def __init__(self):
        self.image=SPACESHIP
        self.image= pygame.transform.scale(self.image, (40,60))
        self.rect=self.image.get_rect()
        self.rect.x=self.X_POS
        self.rect.y=self.Y_POS

    def update(self,user_imput):
        if user_imput[pygame.K_LEFT]:
            self.move_left()
        elif user_imput[pygame.K_RIGHT]:
            self.move_right()
        elif user_imput[pygame.K_UP]:
            self.move_up()
        elif user_imput[pygame.K_DOWN]:
            self.move_down()
        
    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -=10
        elif self.rect.left == 0:
            self.rect.left += 1050
    
    def move_right(self):
        if self.rect.right< SCREEN_WIDTH:
            self.rect.x +=10
        elif self.rect.right==SCREEN_WIDTH:
            self.rect.left -=1050

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -=10
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y +=10
    
    def draw(self,screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))