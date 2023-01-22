import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, x, y, image_x, image_y, width, height, resize_x, resize_y, player, fps):
        pygame.sprite.Sprite.__init__(self)

        self.images_player = []

        for i in range(5):
            img = sprite_sheet.subsurface((i * image_x, 0 * image_y), (width, height))
            img = pygame.transform.scale(img, (resize_x, resize_y))
            self.images_player.append(img)

        self.image = self.images_player[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


        self.clock = pygame.time.Clock()

        self.fps = fps
        self.player = player
        self.count = 0
        self.index = 0
        self.action = False

    def draw(self, surface):
        self.clock.tick(self.fps)

        if 1 < self.index < 2:
            self.index = 0

        if self.count < 4:
            self.image = self.images_player[int(self.index)]
        else:
            if self.player == 1:
                self.image = self.images_player[2]
                self.action = True
            elif self.player == 2:
                self.image = self.images_player[3]
                self.action = True
            elif self.player == 3:
                self.image = self.images_player[4]
                self.action = True
        
        self.count += 0.25
        self.index += 0.25



        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        pass
