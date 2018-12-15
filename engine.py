import pygame

def main():
    # Initializing pygame session
    pygame.init()
    pygame.display.set_caption("Shooter Dude")

    # Initializing Game Surface
    screen = pygame.display.set_mode((800,600))

    # Main Game Loop
    while True:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
    
if __name__ == "__main__":
    main()