import pygame
import random
import sys

# Инициализация PyGame
pygame.init()

# Константы
WIDTH, HEIGHT = 400, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RESTART_BUTTON_COLOR = (0, 255, 0)
RESTART_BUTTON_TEXT_COLOR = (0, 0, 0)

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")
clock = pygame.time.Clock()

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 60))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.vel_y = 0
        self.score = 0  # Счетчик расстояния

    def update(self):
        self.vel_y += 0.2  # Гравитация
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 6
        if keys[pygame.K_RIGHT]:
            self.rect.x += 6

        self.rect.y += self.vel_y

        # Ограничение по горизонтали
        if self.rect.left < 0:
            self.rect.right = WIDTH
        if self.rect.right > WIDTH:
            self.rect.left = 1

# Класс платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((80, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Класс экрана "Game Over"
class GameOverScreen:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 36)  # Шрифт Arial, размер 36
        self.text_surface = self.font.render('Game Over!', True, (255, 0, 0))  # Красный текст
        self.text_rect = self.text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

        # Кнопка рестарта
        self.restart_button_width = 150
        self.restart_button_height = 50
        self.restart_button_x = (WIDTH - self.restart_button_width) // 2
        self.restart_button_y = HEIGHT // 2 + 50
        self.restart_button_rect = pygame.Rect(self.restart_button_x, self.restart_button_y, self.restart_button_width, self.restart_button_height)
        self.restart_button_text = self.font.render('Restart', True, RESTART_BUTTON_TEXT_COLOR)
        self.restart_button_text_rect = self.restart_button_text.get_rect(center=self.restart_button_rect.center)

    def display(self, screen):
        screen.blit(self.text_surface, self.text_rect)

        # Отображение кнопки рестарта
        pygame.draw.rect(screen, RESTART_BUTTON_COLOR, self.restart_button_rect)
        screen.blit(self.restart_button_text, self.restart_button_text_rect)

        pygame.display.flip()

    def handle_restart_button(self, mouse_pos, mouse_pressed):
        if self.restart_button_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            return True
        return False

# Создание групп спрайтов
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# Создание игрока
player = Player()
all_sprites.add(player)

# Создание начальных платформ
for i in range(6):
    if i == 0:
        # Первая платформа под игроком
        x = WIDTH // 2 - 40
        y = HEIGHT // 2 + 50
    else:
        x = random.randint(0, WIDTH - 100)
        y = random.randint(i * 100, i * 100 + 100)
    platform = Platform(x, y)
    all_sprites.add(platform)
    platforms.add(platform)

# Шрифт для отображения счета
font = pygame.font.SysFont('Arial', 24)

# Основной игровой цикл
running = True
game_over = False
game_over_screen = GameOverScreen()

try:
    while running:
        clock.tick(FPS)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        if not game_over:
            all_sprites.update()

            # Проверка столкновений игрока с платформами
            if player.vel_y > 0:  # Только если игрок падает
                hits = pygame.sprite.spritecollide(player, platforms, False)
                if hits:
                    player.vel_y = -10  # Прыжок вверх

            # Проверка, упал ли игрок ниже экрана
            if player.rect.top > HEIGHT:
                game_over = True  # Устанавливаем флаг окончания игры

            # Прокрутка экрана вверх, если игрок поднимается
            if player.rect.top <= HEIGHT // 2.5:
                player.rect.y += abs(player.vel_y)
                player.score += abs(player.vel_y)  # Увеличиваем счет
                for platform in platforms:
                    platform.rect.y += abs(player.vel_y)
                    # Удаление платформ, которые вышли за нижнюю границу
                    if platform.rect.top >= HEIGHT:
                        platform.kill()

            # Добавление новых платформ
            while len(platforms) < 7:
                x = random.randint(0, WIDTH - 200)
                y = random.randint(-50, 0)
                platform = Platform(x, y)
                all_sprites.add(platform)
                platforms.add(platform)

            # Рендеринг
            screen.fill(BLACK)
            all_sprites.draw(screen)

            # Отображение счета
            score_text = font.render(f"Score: {int(player.score)}", True, WHITE)
            screen.blit(score_text, (10, 10))

            pygame.display.flip()
        else:
            # Отображение экрана "Game Over"
            screen.fill(BLACK)  # Очистка экрана
            game_over_screen.display(screen)

            # Обработка нажатия кнопки рестарта
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if game_over_screen.handle_restart_button(mouse_pos, mouse_pressed):
                game_over = False
                player.rect.center = (WIDTH // 2, HEIGHT // 2)
                player.vel_y = 0
                player.score = 0  # Сброс счета

except KeyboardInterrupt:
    print("Игра завершена пользователем.")

finally:
    pygame.quit()
    sys.exit()