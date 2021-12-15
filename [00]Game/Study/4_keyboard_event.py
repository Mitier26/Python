import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Miter Game")

# 배경 이미지 불러오기
background = pygame.image.load("D:/Projects/Python/[00]Game/background.png")

# 스프라이트(케릭터) 불러오기
character = pygame.image.load("D:/Projects/Python/[00]Game/chracter.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width /2) - (character_width /2)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True 
while running:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            running = False
        
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 케릭터를 왼쪽으로
                to_x -= 0.5
            elif event.key == pygame.K_RIGHT:   # 케릭터를 오른쪽으로
                to_x += 0.5
            elif event.key == pygame.K_UP:  # 케릭터를 위로
                to_y -= 0.5
            elif event.key == pygame.K_DOWN:    # 케릭터를 아래로
                to_y += 0.5
        
        # 키보드에서 손을 때면, 키업, 키 입력이 멈추면
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    # 키보드 입력값을 케릭터에서 대입한다.
    character_x_pos += to_x
    character_y_pos += to_y

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