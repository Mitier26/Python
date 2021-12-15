import pygame
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




# 이벤트 루프
running = True 
while running:
    #FPS
    dt = clock.tick(60) # 게임호면의 초당 프레임 수를 설정

    # 2.  이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            running = False
        
    
    # 3. 게임 캐릭터 처리

    # 4. 충돌 처리
    
    # 5. 화면에 그리기
    
    pygame.display.update() 

# 잠시 대기
pygame.time.delay(2000) # 2초 대기

# 게임 종료
pygame.quit()