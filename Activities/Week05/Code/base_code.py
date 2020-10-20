import sys
import pygame

from pygame import Color, Rect, Surface

def cleanup():
    pygame.quit()
    sys.exit()

def main():
    pygame.init()
    screen_size = (600, 600)
    screen_title = "Week 05 code"
    screen = pygame.display.set_mode(screen_size,
                                     pygame.RESIZABLE)
    pygame.display.set_caption(screen_title)

    #CLASS CODE GOES HERE (pt 1):

    #CLASS CODE ENDS HERE
    
    is_running = True

    while is_running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                is_running = False
            if evt.type == pygame.VIDEORESIZE:
                screen_size = evt.size

        if screen_size != screen.get_size():
            screen = pygame.display.set_mode(screen_size,
                                             pygame.RESIZABLE)
            #CHALLENGE CODE GOES HERE
            
            #CHALLENGE CODE ENDS HERE
            
        #CLASS CODE GOES HERE (pt 2):

        #CLASS CODE ENDS HERE
            
        pygame.display.flip()

    cleanup()

#Driver code:
if __name__ == "__main__":
    main()
