import pygame,sys
from level import Level
from menu import MainMenu
from transition import transition

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption("The Other")
        self.clock = pygame.time.Clock()
    
        programIcon = pygame.image.load('../../graphics/icon/icon.png')
        pygame.display.set_icon(programIcon)

        self.mainmenu = MainMenu()
        self.level = Level('level 1')
    

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.level = Level('level 1')
                        transition(self.screen, self.mainmenu.textfont, 'level 1')
                    if event.key == pygame.K_2:
                        self.level = Level('level 2')
                        transition(self.screen, self.mainmenu.textfont, 'level 2')
                    if event.key == pygame.K_3:
                        self.level = Level('level 3')
                        transition(self.screen, self.mainmenu.textfont, 'level 3')
                    if event.key == pygame.K_4:
                        self.level = Level('level 4')
                        transition(self.screen, self.mainmenu.textfont, 'level 4')

            self.screen.fill("Black")

            if not self.mainmenu.start:
                self.mainmenu.draw()

            else:
                self.level.run()

                
            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()