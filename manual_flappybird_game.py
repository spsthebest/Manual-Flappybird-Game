#manual flappybird
import pygame
import random

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappybird")

# specifying colors
bgcolor = "#F3E5AB"  # vanilla
score_color = "black"
alert_color = "red"
pipes_color = (127, 127, 127)  # gray
bird_color = "#00BF00"  # green

# making bird
bird_width = 40
bird_height = 40
bird_x = 60
bird_y = screen_height // 2
bird_y_change = 0

# making pipe
pipe_width = 60
pipe_height = random.randint(150, 450)
pipe_x = screen_width
pipe_y = 0
pipe_gap = 150
pipe_speed = 3

# game settings
gravity = 0.5
jump = -10
score = 0
font = pygame.font.SysFont(None, 35)  # game over display text (size 35)
clock = pygame.time.Clock()  # controls framerate of the game
game_over = False

# defining function to display the score on screen
def show_score(score):
    value = font.render("Score : " + str(score), True, score_color)
    screen.blit(value, [10, 10])  # displays score at the top left corner

# function to display a game over message
def game_over_message():
    message = font.render("Game Over! Press R to restart", True, alert_color)
    screen.blit(message, [screen_width // 6, screen_height // 2])

# main game function
def main_game():
    global bird_y, bird_y_change, pipe_x, pipe_height, score, game_over
    while not game_over:
        for event in pygame.event.get():  # event handling
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_y_change = jump

        bird_y_change += gravity
        bird_y += bird_y_change
        pipe_x -= pipe_speed

        if pipe_x < -pipe_width:
            pipe_x = screen_width
            pipe_height = random.randint(150, 450)
            score += 1

        screen.fill(bgcolor)
        pygame.draw.rect(screen, bird_color, [bird_x, bird_y, bird_width, bird_height])  # defining bird
        pygame.draw.rect(screen, pipes_color, [pipe_x, pipe_y, pipe_width, pipe_height])  # upper pipe
        pygame.draw.rect(screen, pipes_color, [pipe_x, pipe_height + pipe_gap, pipe_width, screen_height - pipe_height - pipe_gap])  # lower pipe

        if bird_y < 0 or bird_y > screen_height - bird_height:  # check if bird hits the top or bottom
            game_over = True
        if bird_x + bird_width > pipe_x and bird_x < pipe_x + pipe_width:
            if bird_y < pipe_height or bird_y + bird_height > pipe_height + pipe_gap:
                game_over = True

        show_score(score)
        pygame.display.update()
        clock.tick(45)  # framerate 45fps

    while game_over:
        game_over_message()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    bird_y = screen_height // 2
                    bird_y_change = 0
                    pipe_x = screen_width
                    pipe_height = random.randint(150, 450)
                    score = 0
                    game_over = False
                    main_game()

if __name__ == "__main__":
    main_game()
