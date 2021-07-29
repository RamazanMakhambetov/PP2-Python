import pygame
import random

from pygame.key import name

WIDTH, HEIGHT = 700, 500

class Blockwall(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.Surface([25, 25])
        self.image.fill(pygame.Color('red'))
        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(WIDTH - 25)

    def update(self):
        self.rect.y += 1

        if self.rect.y > HEIGHT:
            self.reset_pos()


class Blockfood(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.Surface([25, 25])
        self.image.fill(pygame.Color('green'))
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def init(self, x, y):
        super().init()
        self.image = pygame.Surface([20, 20])
        self.image.fill(pygame.Color('blue'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

class Game(object):
    block_wall = None
    block_food = None
    all_blocks = None
    player = None
    game_over = False
    game_win = False
    collision = 0
    score = 0

    def init(self):
        self.score = 0
        self.collision = 0
        self.game_over = False
        self.game_win = False
        self.block_wall = pygame.sprite.Group()
        self.block_food = pygame.sprite.Group()
        self.all_blocks = pygame.sprite.Group()

        for i in range(40):
            block = Blockwall()
            block.rect.x = random.randrange(WIDTH - 25)
            block.rect.y = random.randrange(-300, HEIGHT)
            self.block_wall.add(block)
            self.all_blocks.add(block)

        for i in range(20):
            block = Blockfood()
            block.rect.x = random.randrange(WIDTH - 25)
            block.rect.y = random.randrange(HEIGHT - 25)
            self.block_food.add(block)
            self.all_blocks.add(block)

        self.player = Player(50, 50)
        self.all_blocks.add(self.player)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over or self.game_win:
                    self.init()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, 3)
    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, -3)

        return False

    def run_logic(self):
        if not self.game_over and not self.game_win:
            self.all_blocks.update()

            blocks_wall_list = pygame.sprite.spritecollide(self.player, self.block_wall, True)
            blocks_food_list = pygame.sprite.spritecollide(self.player, self.block_food, True)

            for block in blocks_wall_list:
                self.collision += 1
                if self.collision % 2 == 0:
                    self.score -= 1
            
            for block in blocks_food_list:
                self.score += 1

            if len(self.block_wall) == 0 or self.score < 0:
                self.game_over = True

            if len(self.block_food) == 0:
                self.game_win = True

    def display_frame(self, screen):
        screen.fill(pygame.Color('white'))
        font_50 = pygame.font.SysFont('Arial', 50)
        font_25 = pygame.font.SysFont('serif', 25)
        
        if self.game_over:
            render_game_over = font_50.render('GAME OVER!', True, pygame.Color('black'))
            render_restart = font_25.render('Click to restart', True, pygame.Color('black'))
            screen.blit(render_game_over, (210, 150))
            screen.blit(render_restart, (260, 300))
        if not self.game_over:
            self.all_blocks.draw(screen)

        if self.game_win:
            render_game_over = font_50.render('GAME WIN!', True, pygame.Color('black'))
            render_restart = font_25.render('Click to restart', True, pygame.Color('black'))
            screen.blit(render_game_over, (230, 150))
            screen.blit(render_restart, (260, 300))
        if not self.game_win:
            self.all_blocks.draw(screen)

        render_score = font_25.render(f'Score: {self.score}', True, pygame.Color('black'))
        screen.blit(render_score, [10, 10])
        
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption('Hungry Lion')
    pygame.mouse.set_visible(0)
    clock = pygame.time.Clock()

    run = False
    game = Game()
    while not run:
        run = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(90)

    pygame.quit()

if name == "main":
    main()