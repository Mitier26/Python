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
# 케릭터는 항상 움직여야 한다.
# 케릭터의 크기를 알아야한다.
character_size = character.get_rect().size # 이미지의 크기를 구해온다.
character_width = character_size[0] # 케릭터의 가로 크기
character_height = character_size[1]    # 케릭터의 세로 크기
character_x_pos = (screen_width /2) - (character_width /2)  # 화면 가로 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이벤트 루프
running = True 
while running:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            running = False 
    
    screen.blit(background, (0,0))  

    # 케릭터를 화면에 그린다.
    screen.blit(character,(character_x_pos, character_y_pos))

    pygame.display.update() 


pygame.quit()