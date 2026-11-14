import pygame


def draw_pattern(screen, rect, pattern):
    surface = pygame.Surface(rect.size)
    surface.fill("white")

    if pattern in (0, 2):
        for y in range(0, rect.height, 12):
            pygame.draw.line(surface, "blue", (0, y), (rect.width - 1, y))

    if pattern in (1, 2):
        for x in range(0, rect.width, 12):
            pygame.draw.line(surface, "blue", (x, 0), (x, rect.height - 1))

    if pattern == 3:
        for x in range(-rect.height, rect.width, 12):
            pygame.draw.line(surface, "blue", (x, 0), (x + rect.height, rect.height))

    screen.blit(surface, rect)
    pygame.draw.rect(screen, "black", rect, 2)


def main():
    pygame.init()

    try:
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()

        x1, y1 = 250, 200
        x2, y2 = 550, 400
        rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)

        pattern = 0
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_LEFT:
                        rect.x -= 10
                    elif event.key == pygame.K_RIGHT:
                        rect.x += 10
                    elif event.key == pygame.K_UP:
                        rect.y -= 10
                    elif event.key == pygame.K_DOWN:
                        rect.y += 10
                    elif event.key == pygame.K_PAGEUP:
                        pattern = (pattern + 1) % 4
                    elif event.key == pygame.K_PAGEDOWN:
                        pattern = (pattern - 1) % 4

            rect.clamp_ip(screen.get_rect())

            screen.fill((235, 235, 235))
            draw_pattern(screen, rect, pattern)

            pygame.display.set_caption(
                f"ЛР № 1 | Узор {pattern + 1}/4 | Стрелки | PgUp/PgDn | Esc"
            )
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()