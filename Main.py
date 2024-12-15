import pygame

print('Start Setup')
pygame.init()
window = pygame.display.set_mode(size=(800, 650))
print('End Setup')

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close Window
            quit()  # end pygame
