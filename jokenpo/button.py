import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, x, y, image_x, image_y, width, height, resize_x, resize_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.images_button = []
        for i in range(2): 
            img = sprite_sheet.subsurface((i * image_x, 0 * image_y), (width, height))
            img = pygame.transform.scale(img, (resize_x, resize_y))
            self.images_button.append(img)

        self.image = self.images_button[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.clicked = False
        self.action = False

    def draw(self, surface):
        self.action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.clicked == True and pygame.mouse.get_pressed()[0] == 0: 
            self.image = self.images_button[int(0)]
            self.action = False
            self.clicked = False

        elif self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.action = True
                self.clicked = True
                self.image = self.images_button[int(1)]
        
                       
        
        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        pass
