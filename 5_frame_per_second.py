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

# 이벤트 루프
running = True 
while running:
    #FPS
    dt = clock.tick(60) # 게임호면의 초당 프레임 수를 설정

    # FPS 특이점
    # 프레임 마다 움직이는 속도가 달라진다.
    # 캐릭터가 1초 동안 100 만큼 이동을 해야함
    # 10 fps : 1 초 동안 10번 동작 -> 1번에 몇 만큼 이동? 10만큼 10 * 10 = 100
    # 20 fps : 1 초 동안 20번 동작 -> 1번에 5만큼 이동! 5 * 20 = 100

    #print("fps : " + str(clock.get_fps()))

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
    # character_x_pos += to_x
    # character_y_pos += to_y
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
    
    # 배경을 화면에 그린다.
    screen.blit(background, (0,0))  

    # 케릭터를 화면에 그린다.
    screen.blit(character,(character_x_pos, character_y_pos))

    pygame.display.update() 


pygame.quit()