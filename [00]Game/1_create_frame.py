# 파이게임자 설치 되었는지 확인해야 한다.
import pygame

# 초기화 (반드시 필요)
# pygame을 사용하기 위해서는 꼭 해야 한다.
pygame.init()
# init이 안될 경우 : 파일 > 설정 > linting > Python> Lintiong:Enabeled를 끄자

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
# 화면을 설정하고 screen 변수에 저장한ㄷ.

# 화면 타이틀 설정
pygame.display.set_caption("Miter Game")

# 바로 프로그램이 종료되지 않게해야 게임창이 사라지지 않는다.

# 이벤트 루프
running = True  # 게임이 실행중인가?
while running:
    for event in pygame.event.get():    # pygame을 하기 위한 필수 조건
    # 외부 동작을 체크하는 것이다.
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임 진행중이 아님

# pygame 종료
pygame.quit()