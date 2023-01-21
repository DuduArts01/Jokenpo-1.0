import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, x, y, image_x, image_y, width, height, resize_x, resize_y, player1):
        pygame.sprite.Sprite.__init__(self)
        
        self.images_player = []
        
        self.player1 = player1
        
        for i in range(2):
            img = sprite_sheet.subsurface((i * image_x, 0 * image_y), (width, height))
            img = pygame.transform.scale(img, (resize_x, resize_y))
            self.images_player.append(img)

        if player1:
            self.image = self.images_player[0]
        else:
            self.image = self.images_player[1]

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, surface):
        if self.player1:
            self.image = self.images_player[0]
        else:
            self.image = self.images_player[1]
        
        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        pass
