import pygame
from csv import reader
from os import walk
from player import Player


def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for img in img_files:
            full_path = path + '/' + img
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list

def level1 ():        
    layouts = {
        'boundary': import_csv_layout('../../graphics/maps/map1/map1_Bounds.csv'),
        'obstacles': import_csv_layout('../../graphics/maps/map1/map1_Obstacles.csv'),
        'entities': import_csv_layout('../../graphics/maps/map1/map1_Entities.csv'),
    }
    graphics = {
        'campsite_props' : import_folder('../../graphics/assets/Map 1 Singles/campsite props'),
        'characters' : import_folder('../../graphics/assets/Map 1 Singles/characters'),
        'fence' : import_folder('../../graphics/assets/Map 1 Singles/fence'),
        'tent' : import_folder('../../graphics/assets/Map 1 Singles/tent'),
        'tree' : import_folder('../../graphics/assets/Map 1 Singles/tree'),
    }

    return layouts,graphics

def level1_layout(visible_sprites,entity_sprites, obstacle_sprites,layouts,graphics,Tile,Entity):
    for style,layout in layouts.items():
        for row_index,row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col != '-1':
                    x = col_index * 48
                    y = row_index * 48
                    if style == 'boundary':
                        Tile ((x,y),[obstacle_sprites],'invisible')
                    if style == 'obstacles':
                        if col == '30':
                            Tile ((x,y),[visible_sprites,obstacle_sprites],'obstacles',graphics['fence'][0])
                        if col == '34':
                            Tile((x,y),[visible_sprites,obstacle_sprites],'obstacles',graphics['tree'][0])
                        if col == '22':
                            Tile((x,y),[visible_sprites,obstacle_sprites],'obstacles',graphics['campsite_props'][0])
                        if col == '31':
                            Tile((x,y),[visible_sprites,obstacle_sprites],'obstacles',graphics['tent'][0])
                        if col== '33':
                            Tile((x,y),[visible_sprites,obstacle_sprites],'obstacles',graphics['tent'][1])
                        if col == '32':
                            Tile((x,y),[visible_sprites,obstacle_sprites],'obstacles',graphics['tent'][2])
               
                    if style == 'entities':
                        if col == '23':
                            player = Player((x,y+30),[visible_sprites],entity_sprites,obstacle_sprites, graphics['characters'][0])
                        if col == '27':
                            Entity ((x,y),[entity_sprites,visible_sprites],obstacle_sprites, graphics['characters'][1])
                        if col == '28':
                            Entity ((x,y),[entity_sprites,visible_sprites],obstacle_sprites, graphics['characters'][2])
                        if col == '26':
                            Entity ((x,y),[entity_sprites,visible_sprites],obstacle_sprites, graphics['characters'][3])  
                        if col == '24':
                            Entity ((x,y),[entity_sprites,visible_sprites],obstacle_sprites, graphics['characters'][4])
                        if col == '25':
                            Entity ((x,y),[entity_sprites,visible_sprites],obstacle_sprites, graphics['characters'][5]) 
                        if col == '29':
                            Entity ((x,y),[entity_sprites,visible_sprites],obstacle_sprites, graphics['characters'][6])
                       
                    
    return player

def level2 ():        
    layouts = {
        'bounds': import_csv_layout('../../graphics/maps/map2/map2_Bounds.csv'),
        'objects': import_csv_layout('../../graphics/maps/map2/map2_Objects.csv'),
        'entities': import_csv_layout('../../graphics/maps/map2/map2_Entities.csv')
    }
    graphics = {
        'playground' : import_folder('../../graphics/assets/Map 2 Singles/Playground'),
        'green' : import_folder('../../graphics/assets/Map 2 Singles/Green'),
        'characters': import_folder('../../graphics/assets/Map 2 Singles/Characters')
    }

    return layouts,graphics

def level2_layout(visible_sprites,entity_sprites, obstacle_sprites,layouts,graphics,Tile,Entity):
    for style,layout in layouts.items():
        for row_index,row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col != '-1':
                    x = col_index * 48  
                    y = row_index * 48
                    if style == 'bounds':
                        Tile ((x,y),[obstacle_sprites],'invisible')

                    if style == 'objects':
                        if col == '0':
                            Tile((x,y),[visible_sprites, obstacle_sprites],'obstacles', graphics['playground'][0])
                        if col == '1':
                            Tile((x,y),[visible_sprites, obstacle_sprites],'obstacles', graphics['playground'][1])
                        if col == '2':
                            Tile((x,y),[visible_sprites, obstacle_sprites],'obstacles', graphics['playground'][2])
                        if col == '3':
                            Tile((x,y),[visible_sprites, obstacle_sprites],'obstacles', graphics['playground'][3])
                        if col == '4':
                            Tile((x,y),[visible_sprites, obstacle_sprites],'obstacles', graphics['playground'][4])
                        if col == '5':
                            Tile((x,y),[visible_sprites, obstacle_sprites],'obstacles', graphics['playground'][5])
                        if col == '6':
                            Tile((x,y),[visible_sprites, obstacle_sprites],'obstacles', graphics['playground'][6])
                        if col == '7':
                            Tile ((x,y),[visible_sprites,obstacle_sprites],'obstacles',graphics['green'][0])
                        if col == '8':
                            Tile ((x,y),[visible_sprites,obstacle_sprites],'obstacles',graphics['green'][1])

                    if style == 'entities':
                        if col == '0':
                            player = Player((x,y),[visible_sprites],entity_sprites,obstacle_sprites, graphics['characters'][0])
                        if col == '1':
                            Entity ((x,y),[entity_sprites,visible_sprites],obstacle_sprites, graphics['characters'][1])
                        if col == '2':
                            Entity ((x,y),[entity_sprites,visible_sprites],obstacle_sprites, graphics['characters'][2])
                        if col == '3':
                            Entity ((x,y),[entity_sprites,visible_sprites],obstacle_sprites, graphics['characters'][3])
                        if col == '4':
                            Entity ((x,y),[entity_sprites,visible_sprites],obstacle_sprites, graphics['characters'][4])
                        if col == '6':
                            Entity ((x,y),[entity_sprites,visible_sprites],obstacle_sprites, graphics['characters'][6])

    return player

def level3():
    layouts = {
        'bounds': import_csv_layout('../../graphics/maps/map3/map3_Bounds.csv'),
        'entities': import_csv_layout('../../graphics/maps/map3/map3_Entities.csv')
    }
    graphics = {
        'characters': import_folder('../../graphics/assets/Map 3 Singles/Characters')
    }

    return layouts,graphics

def level3_layout(visible_sprites,entity_sprites, obstacle_sprites,layouts,graphics,Tile,Entity):
    for style,layout in layouts.items():
        for row_index,row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col != '-1':
                    x = col_index * 48  
                    y = row_index * 48
                    if style == 'bounds':
                        Tile ((x,y),[obstacle_sprites],'invisible')

                    if style == 'entities':
                        if col == '0':
                            player = Player((x,y),[visible_sprites],entity_sprites,obstacle_sprites, graphics['characters'][0])
                        if col == '6':
                            Entity ((x,y),[entity_sprites,visible_sprites],obstacle_sprites, graphics['characters'][6]) 
                       
                    
    return player

def level4():
    layouts = {
        'bounds': import_csv_layout('../../graphics/maps/map4/map4_Bounds.csv'),
        'entities': import_csv_layout('../../graphics/maps/map4/map4_Entities.csv')
    }
    graphics = {
        'characters': import_folder('../../graphics/assets/Map 4 Singles/Characters')
    }

    return layouts,graphics

def level4_layout(visible_sprites,entity_sprites, obstacle_sprites,layouts,graphics,Tile,Entity):
    for style,layout in layouts.items():
        for row_index,row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col != '-1':
                    x = col_index * 48  
                    y = row_index * 48
                    if style == 'bounds':
                        Tile ((x,y),[obstacle_sprites],'invisible')

                    if style == 'entities':
                        if col == '0':
                            player = Player((x,y),[visible_sprites],entity_sprites,obstacle_sprites, graphics['characters'][0])

    return player
