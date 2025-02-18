import pygame


pygame.init()

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# Colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)

# Paddle Class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 100])
        self.image.fill(color_white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - self.rect.height:
            self.rect.y += self.speed

# Ball Class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(color_white)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed_x = 5
        self.speed_y = 5

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top and bottom walls
        if self.rect.y <= 0 or self.rect.y >= SCREEN_HEIGHT - self.rect.height:
            self.speed_y = -self.speed_y

        # Reset ball if it goes past the paddles
        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH // 2
            self.rect.y = SCREEN_HEIGHT // 2
            self.speed_x = -self.speed_x

# Main Function
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pong')

    # Create sprites
    all_sprites = pygame.sprite.Group()
    paddle1 = Paddle(50, SCREEN_HEIGHT // 2 - 50)
    paddle2 = Paddle(SCREEN_WIDTH - 60, SCREEN_HEIGHT // 2 - 50)
    ball = Ball()
    all_sprites.add(paddle1, paddle2, ball)

    # Main game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move_up()
        if keys[pygame.K_s]:
            paddle1.move_down()
        if keys[pygame.K_UP]:
            paddle2.move_up()
        if keys[pygame.K_DOWN]:
            paddle2.move_down()

        # Update ball position
        ball.update()

        # Check for collisions between the ball and paddles
        if pygame.sprite.collide_rect(ball, paddle1) or pygame.sprite.collide_rect(ball, paddle2):
            ball.speed_x = -ball.speed_x

        # Drawing
        screen.fill(color_black)
        all_sprites.draw(screen)
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()


