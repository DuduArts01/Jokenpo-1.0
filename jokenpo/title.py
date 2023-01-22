import pygame

class Title(pygame.sprite.Sprite):
    def __init__(self, image, x, y, image_x, image_y, width, height, resize_x, resize_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.images_button = []
        
        img = image.subsurface((0 * image_x, 0 * image_y), (width, height))
        img = pygame.transform.scale(img, (resize_x, resize_y))
        
        self.images_button.append(img)



        self.image = self.images_button[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, surface):
        self.image = self.images_button[int(0)]


        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        pass
