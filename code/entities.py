import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self,pos,groups, obstacle_sprites,img):
        super().__init__(groups)
        self.image = img
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect
        
        self.direction = pygame.math.Vector2() 
        self.speed = 5
        
        self.obstacle_sprites = obstacle_sprites

    def collision(self,direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x >  0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x <  0:
                        self.hitbox.left = sprite.hitbox.right
            


        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y >  0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y <  0:
                        self.hitbox.top = sprite.hitbox.bottom
