import pygame

def levelmusic(level):
    if level == 'level 1':
        bg_music = pygame.mixer.Sound('../../audio/level1/background.ogg')
        bg_music.set_volume(0.25)
        bg_music.play(loops =-1)

    if level == 'level 2':
        pygame.mixer.stop()
        bg_music = pygame.mixer.Sound('../../audio/level2/background.ogg')
        bg_music.set_volume(0.25)
        bg_music.play(loops =-1)

    if level == 'level 3':
        pygame.mixer.stop()
        bg_music = pygame.mixer.Sound('../../audio/level3/background.ogg')
        bg_music.set_volume(0.25)
        bg_music.play(loops =-1)
    
    if level == 'level 4':
        pygame.mixer.stop()
        bg_music = pygame.mixer.Sound('../../audio/level4/background.wav')
        bg_music.set_volume(0.25)
        bg_music.play(loops =-1)

def transition (screen,font,level):
    text_timer = 5000
    
    if level == 'level 1':
        tick = pygame.mixer.Sound ('../../audio/menu/tick.mp3') 
        tick.play(loops = 0)
        while text_timer != 1000:
            screen.fill('Black')
            daytext = font.render('Dia 1', False, 'White')
            daytext_rect = daytext.get_rect(center = (640,200))
            
            sitetext = font.render('Campamento', False, 'White')
            sitetext_rect = sitetext.get_rect(center = (640,240))

            screen.blit(daytext,daytext_rect)
            screen.blit(sitetext, sitetext_rect)
            text_timer-=1
            pygame.display.update()

        tick = pygame.mixer.Sound ('../../audio/menu/tick.mp3') 
        tick.play(loops = 0)
        while text_timer !=0:
            screen.fill('Black')
            text_timer-=1
            pygame.display.update()
        levelmusic(level)

    if level == 'level 2':
        tick = pygame.mixer.Sound ('../../audio/menu/tick.mp3') 
        tick.play(loops = 0)
        while text_timer != 1000:
            screen.fill('Black')
            daytext = font.render('Dia 2', False, 'White')
            daytext_rect = daytext.get_rect(center = (640,200))
            
            sitetext = font.render('Escuela', False, 'White')
            sitetext_rect = sitetext.get_rect(center = (640,240))

            screen.blit(daytext,daytext_rect)
            screen.blit(sitetext, sitetext_rect)
            text_timer-=1
            pygame.display.update()

        tick = pygame.mixer.Sound ('../../audio/menu/tick.mp3') 
        tick.play(loops = 0)
        while text_timer !=0:
            screen.fill('Black')
            text_timer-=1
            pygame.display.update()
        levelmusic(level)
    
    if level == 'level 3':
        tick = pygame.mixer.Sound ('../../audio/menu/tick.mp3') 
        tick.play(loops = 0)
        while text_timer != 1000:
            screen.fill('Black')
            daytext = font.render('Dia 3', False, 'White')
            daytext_rect = daytext.get_rect(center = (640,200))
            
            sitetext = font.render('Casa', False, 'White')
            sitetext_rect = sitetext.get_rect(center = (640,240))

            screen.blit(daytext,daytext_rect)
            screen.blit(sitetext, sitetext_rect)
            text_timer-=1
            pygame.display.update()

        tick = pygame.mixer.Sound ('../../audio/menu/tick.mp3') 
        tick.play(loops = 0)
        while text_timer !=0:
            screen.fill('Black')
            text_timer-=1
            pygame.display.update()
        levelmusic(level)
    
    if level == 'level 4':
        tick = pygame.mixer.Sound ('../../audio/menu/tick.mp3') 
        tick.play(loops = 0)
        while text_timer != 1000:
            screen.fill('Black')
            daytext = font.render('Dia 4', False, 'White')
            daytext_rect = daytext.get_rect(center = (640,200))

            screen.blit(daytext,daytext_rect)
            text_timer-=1
            pygame.display.update()
        tick = pygame.mixer.Sound ('../../audio/menu/tick.mp3') 
        tick.play(loops = 0)
        while text_timer !=0:
            screen.fill('Black')
            text_timer-=1
            pygame.display.update()
        levelmusic(level)

