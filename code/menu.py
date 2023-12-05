import pygame,sys
from transition import transition

class MainMenu():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.bg = pygame.transform.scale_by(pygame.image.load('../../graphics/menu/background.png').convert_alpha(), 2)
        self.bg_rect = self.bg.get_rect(midbottom = (640,720))
        self.start = False
        self.option = pygame.image.load('../../graphics/menu/Option.png').convert_alpha()
            
        self.titlefont = pygame.font.Font('../../graphics/font/Title.ttf',200)
        self.textfont = pygame.font.Font('../../graphics/font/Text.ttf',35)

        self.bg_music = pygame.mixer.Sound('../../audio/menu/Theme.ogg') 
        self.bg_music.set_volume(0.25)
        self.bg_music.play(loops = -1)
        
    def draw(self):
        # Background
        self.screen.blit(self.bg, self.bg_rect)

        # Title Outlines
        titleout1 = self.titlefont.render('The', False,('#3b4453'))
        titleout1 = pygame.transform.scale_by(titleout1,1.05)
        titleout1_rect = titleout1.get_rect(topleft = (410,5))


        titleout2 = self.titlefont.render('Other', False,('#3b4453'))
        titleout2 = pygame.transform.scale_by(titleout2,1.02)
        titleout2_rect = titleout2.get_rect(topleft = (625,5))

        self.screen.blit(titleout1, titleout1_rect)
        self.screen.blit(titleout2, titleout2_rect)


        # Title
        title = self.titlefont.render('The Other', False,('#990000'))
        title_rect = title.get_rect(midtop = (640,5))
        self.screen.blit(title, title_rect)


        # Start 
        start = self.textfont.render('Start',False,'White')
        start_rect = start.get_rect(midright = (1190,250))

        startop = self.option
        startop_rect = startop.get_rect(midright = (1240,250))
        self.screen.blit(startop, startop_rect)

        # Quit
        quit = self.textfont.render('Quit',False,'White')
        quit_rect = quit.get_rect(midright = (1190,350))
        
        quitop = self.option
        quitop_rect = quitop.get_rect(midright = (1240, 350))
        self.screen.blit(quitop, quitop_rect)
        # Options are drawn

        self.screen.blit(start,start_rect)
        self.screen.blit(quit,quit_rect)
        
        self.input(startop_rect,quitop_rect)
        pygame.display.update()

    def input(self,startpos, quitpos):
        mousepressed = pygame.mouse.get_pressed()
        mousepos = pygame.mouse.get_pos()

        if startpos.collidepoint(mousepos):
            if mousepressed[0]:
                self.bg_music.fadeout(1000)
                transition(self.screen,self.textfont,'level 1')
                self.start = True

        if quitpos.collidepoint(mousepos):
             if mousepressed[0]:
                pygame.quit()
                sys.exit()
                