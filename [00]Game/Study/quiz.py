import pygame
from random import *
##########################################################
# 기본 초기화 (반드시 해야 하는 것)

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Miter Game")

# FPS
clock = pygame.time.Clock()
##########################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경 그림 선택
background = pygame.image.load("D:/Projects/Python/[00]Game/background_quiz.png")
player = pygame.image.load("D:/Projects/Python/[00]Game/character_quiz.png")
enemy = pygame.image.load("D:/Projects/Python/[00]Game/enemy_quiz.png")

# 플레이어, 적 화면에 배치 충동 처리

# 위에서 불러온 player 그림의 크기를 가지고 온다.
player_size = player.get_rect().size
# 그림의 크기에서 높이와 넓이를 분리
player_width = player_size[0]
player_height = player_size[1]
# player의 초기 위치 설정
player_x_pos = (screen_width /2) - (player_width /2)
player_y_pos = screen_height - player_height

to_x = 0
player_speed = 0.5

# 적의 크기 위치 정해야 한다.
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (random() * (screen_width - enemy_width)) 
enemy_y_pos = screen_height - enemy_height

enemy_speed = 0.5
enemy_to_y = 0

game_font = pygame.font.Font(None, 40)

start_ticks = pygame.time.get_ticks()


# 이벤트 루프
running = True 
while running:
    #FPS
    dt = clock.tick(60) # 게임호면의 초당 프레임 수를 설정

    # 2.  이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                to_x += player_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                to_x = 0
    
    if enemy_y_pos <= screen_height:
        enemy_to_y = enemy_speed
    elif enemy_y_pos > screen_height:
        enemy_y_pos = 0 - enemy_height
        enemy_to_y = 0
        enemy_x_pos = (random() * (screen_width - enemy_width))
    
    

    player_x_pos += to_x * dt
    enemy_y_pos += enemy_to_y * dt

    # 3. 게임 캐릭터 처리
    if player_x_pos < 0:
        player_x_pos = 0
    elif player_x_pos > screen_width - player_width:
        player_x_pos = screen_width - player_width
    
    # 4. 충돌 처리
    player_rect = player.get_rect()
    player_rect.left = player_x_pos
    player_rect.top = player_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if player_rect.colliderect(enemy_rect):
        print("충돌해따")
        running = False

    # 5. 화면에 그리기
    
    screen.blit(background, (0,0))
    screen.blit(player, (player_x_pos, player_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(elapsed_time)), True, (255,255,255))
    # render :  시간, True, 글자색상
    screen.blit(timer, (10,10))
    
    pygame.display.update() 

# 게임 종료
pygame.quit()