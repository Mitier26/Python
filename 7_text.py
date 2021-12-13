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

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트 , 크기)

# 총 시간
total_time = 10

# 시간 시간 정보
start_ticks = pygame.time.get_ticks()   # 시작 tick를 받아옴

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

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 시작 시간에서 경과 시간을 빼면 플레이한 시간이 나온다.
    # / 1000 : 밀리세컨드 이기 때문에

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    # render :  시간, True, 글자색상
    screen.blit(timer, (10,10))

    # 만약 시간이 0 이하이면
    if total_time - elapsed_time <= 0:
        running = False


    pygame.display.update() 

# 잠시 대기
pygame.time.delay(2000) # 2ㅗ 대기

# 게임 종료
pygame.quit()