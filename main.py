import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

# test_surface  = pygame.Surface((100, 200))
# test_surface.fill("red")

sky_surface  = pygame.image.load("graphics/Sky.png").convert()
ground_surface  = pygame.image.load("graphics/ground.png").convert()

test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
score_surf = test_font.render("Press SPACE to jump", False, "green")  # text, anti-aliasing, color
score_rect = score_surf.get_rect(center=(400,50))

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_gravity = 0
player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
# player_rectangle = pygame.Rect(left, top, width, height)
# player_rect = player_surface.get_rect(topleft = (80, 200))
player_rect = player_surface.get_rect(midbottom = (80, 300))

game_active = True

while True:
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, "Pink", score_rect)
        pygame.draw.rect(screen, "Pink", score_rect, 20)
        # pygame.draw.aaline(screen, "Pink", (0, 0), (800, 600))
        screen.blit(score_surf, score_rect)

        screen.blit(snail_surf, snail_rect)
        snail_rect.x -= 5
        if snail_rect.x < -50:
            snail_rect.x = 800

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False

        # if player_rect.colliderect(snail_rect):
        #     print("collision")

        # rect1.collidepoint((x, y))

        # if player_rect.collidepoint(pygame.mouse.get_pos()):
        #     print(pygame.mouse.get_pressed())
    else:  # show menu with new game option
        pass


    pygame.display.update()
    clock.tick(60)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("jump")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("mouse on a player")
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                    


