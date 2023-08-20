import pygame
import sys

# 초기화
pygame.init()

# 화면 크기
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 화면 생성
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("간단한 레이싱 게임")

# 차량 초기 위치
car_x, car_y = WIDTH // 2, HEIGHT - 100
car_width, car_height = 50, 100

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= 5
    if keys[pygame.K_RIGHT]:
        car_x += 5

    # 화면 지우기
    screen.fill(WHITE)

    # 차량 그리기
    pygame.draw.rect(screen, RED, (car_x, car_y, car_width, car_height))

    # 화면 업데이트
    pygame.display.flip()

# 게임 종료
pygame.quit()
sys.exit()
