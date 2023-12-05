import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups,sprite_type, surface = pygame.Surface((48,48))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface

        if sprite_type =='obstacles':
            self.rect = self.image.get_rect(topleft = (pos[0], pos[1] - 100))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        
        self.hitbox = self.rect.inflate(0,-10)