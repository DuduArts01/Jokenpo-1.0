import pygame


class Loading(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, x, y, image_x, image_y, width, height, resize_x, resize_y, count_image, clock, loading):
        pygame.sprite.Sprite.__init__(self)

        self.images_load = []

        for i in range(count_image):
            img = sprite_sheet.subsurface((i * image_x, image_y), (width, height))
            img = pygame.transform.scale(img, (resize_x, resize_y))
            self.images_load.append(img)

        self.index = 0
        
        self.count_image = count_image - 1
        self.loading = loading



        self.image = self.images_load[self.index]

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.exit_loading = True

        self.clock = pygame.time.Clock()
        self.fps = clock

        self.time = 7
        self.count = 0

    def draw(self, surface):
        self.clock.tick(self.fps)


        if(int(self.count == self.time)) and (self.loading == True):
            self.exit_loading = False
            

        if(int(self.index) == self.count_image):
            self.index = 0

        self.index += 0.25
        self.count += 0.25

        self.image = self.images_load[int(self.index)]




        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        pass
