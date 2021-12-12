import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Miter Game")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("D:/Projects/Python/[00]Game/background.png")

# 스프라이트(케릭터) 불러오기
character = pygame.image.load("D:/Projects/Python/[00]Game/chracter.png")

# 케릭터의 크기, 위치
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width /2) - (character_width /2)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 enemy 캐릭터 스프라이트 불러오기
enemy = pygame.image.load("D:/Projects/Python/[00]Game/enemy.png")

# enemy 의 크기, 위치
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width /2) - (enemy_width /2)
enemy_y_pos = (screen_height /2) - (enemy_height /2)


# 이벤트 루프
running = True 
while running:
    #FPS
    dt = clock.tick(60) # 게임호면의 초당 프레임 수를 설정

    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        # 키보드에서 손을 때면, 키업, 키 입력이 멈추면
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    # 키보드 입력값을 케릭터에서 대입한다.
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리, 케릭터가 화면 밖으로 나가지 않도록 한다.
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # 세로 경계갑 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    # 캐릭터를 처음 만들면 그 위치에 상자가 있다.
    # 캐릭터의 이동에 맞추어 상자의 위치를 변경해야 한다.
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했다")
        running = False
    
    # 배경을 화면에 그린다.
    screen.blit(background, (0,0))  

    # 케릭터를 화면에 그린다.
    screen.blit(character,(character_x_pos, character_y_pos))

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update() 


pygame.quit()