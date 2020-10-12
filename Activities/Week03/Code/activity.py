"""
    Kids Hack Labs
    Fall 2020 - Senior
    Week 03: pygame review
    In-class activity
"""
#Steps 1 and 2 involve external activites
#such as creating folders and files

#Step 3: module imports
import sys
import pygame

#Step 4: cleanup function
def cleanup():
    pygame.quit()
    sys.exit()

#Step 5: application entry point
def main():
    #Steps 5.1 through 5.5 -> Setup
    pygame.init()
    screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
    new_size = screen.get_size()
    pygame.display.set_caption("Week 03 code")
    is_running = True

    #Steps 5.6 and substeps down to 5.6.4
    while is_running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                is_running = False
            if evt.type == pygame.VIDEORESIZE:
                new_size = evt.size

        if new_size != screen.get_size():
            screen = pygame.display.set_mode(new_size, pygame.RESIZABLE)

        screen.fill((63, 127, 255))
        pygame.display.flip()

    #Step 5.6.5 actually has to be called outside the while loop
    cleanup()

#Step 5.7 and substeps:
if __name__ == "__main__":
    main()

"""
    Obs.: The code was simplified, and it is just hard-coded so that
          students can get a starting point over which to expand. The
          details of the code will be discussed in Week 04. Students
          are also encouraged to re-code the example above as their
          'homework', so as to familiarize themselves with the steps.
"""
