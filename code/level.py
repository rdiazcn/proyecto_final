import pygame
import levels
from tile import Tile
from entities import Entity



class Level:
    def __init__(self,level):
        #Get the display surface
        self.display_surface= pygame.display.get_surface()

        self.level = level

        self.visible_sprites = YSortCameraGroup(level)
        self.obstacle_sprites = pygame.sprite.Group()
        self.entity_sprites = pygame.sprite.Group()
        self.create_map()


    def create_map(self):

        if self.level == 'level 1':
            layouts,graphics = levels.level1()
            self.player= levels.level1_layout(self.visible_sprites,self.entity_sprites,self.obstacle_sprites,layouts,graphics,Tile,Entity)

        if self.level == 'level 2':
            layouts,graphics = levels.level2()
            self.player= levels.level2_layout(self.visible_sprites,self.entity_sprites,self.obstacle_sprites,layouts,graphics,Tile,Entity)

        elif self.level == 'level 3':
            layouts,graphics = levels.level3()
            self.player= levels.level3_layout(self.visible_sprites,self.entity_sprites,self.obstacle_sprites,layouts,graphics,Tile,Entity)

        elif self.level == 'level 4':
            layouts,graphics = levels.level4()
            self.player= levels.level4_layout(self.visible_sprites,self.entity_sprites,self.obstacle_sprites,layouts,graphics,Tile,Entity)



    def run(self):  
        # update and draw the game
       self.visible_sprites.custom_draw(self.player)
       self.visible_sprites.update()
    

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self,level):
        #general setup
        super().__init__()

        # Offset rendering
        self.display_surface= pygame.display.get_surface()
        self.half_width = self.display_surface.get_size ()[0]//2
        self.half_height = self.display_surface.get_size ()[1]//2
        self.offset = pygame.math.Vector2(100,200)
        self.level = level

        # creating the floor
        if self.level == 'level 1':
            self.floor_surf = pygame.image.load('../../graphics/map/Floor1.png')
            self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
        elif self.level == 'level 2':
            self.floor_surf = pygame.image.load('../../graphics/map/Floor2.png')
            self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
        elif self.level == 'level 3':
            self.floor_surf = pygame.image.load('../../graphics/map/Floor3.png')
            self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
        elif self.level == 'level 4':
            self.floor_surf = pygame.image.load('../../graphics/map/Floor4.png')
            self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self,player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height


        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)


        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)



        
