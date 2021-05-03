#IMPORT
import pygame, time, sys, os, random
from pathlib import Path
pygame.init()
size =20

#Màu sắc của game
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
gray = pygame.Color(128, 128, 128)
red = pygame.Color(255, 0, 0)

#Khai Báo Biến
    #Vị trí ban đầu của rắn
snakePos = [180,60]
snakeBody = [[180,60],[160,60],[140,60]] #size ban đầu gồm 3 khối, mỗi khối có size m=20
    #Vị trí thức ăn
foodx = random.randrange(1,71)
foody = random.randrange(1,45)
if (foodx % 2 != 0): foodx += 1
if (foody % 2 != 0): foody += 1
foodPos= [foodx * 10, foody * 10]
foodExist = True
    #Hướng đi ban đầu của rắn
snakeDirect = 'Right'
changeTo = snakeDirect
    #Điểm số
score = 0

#Tạo Window game
gameWindow = pygame.display.set_mode((735, 475))
pygame.display.set_caption('SnakeGameByTony')

#Hiển Thị Điểm
def show_score(check = 1):
    scoreFont = pygame.font.SysFont('consolas',20)
    scoreSurf = scoreFont.render('SCORE: {0}'.format(score),True,white) 
    scoreRect = scoreSurf.get_rect()
    
    if (check == 1): scoreRect.midtop = (70,20)
    else: scoreRect.midtop = (360,230)
    gameWindow.blit(scoreSurf,scoreRect)

#GAME_OVER
def game_over():
    gameFont = pygame.font.SysFont('consolas',40)   
    gameSurf = gameFont.render('GAME OVER!',True,red)
    gameRect = gameSurf.get_rect()

    gameRect.midtop = (360,150)
    gameWindow.blit(gameSurf,gameRect)

    show_score(0)
    pygame.display.flip()
    time.sleep(5) # thời gian chờ trước khi thoát
    pygame.quit()
    sys.exit()

#Main Loop
while True:
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        # Xử lý Phím bấm
        if event.type == pygame.KEYDOWN: #Nếu có phím nào đó được ấn(xuống)
            if event.key == pygame.K_RIGHT:
                changeTo = 'RIGHT'
            if event.key == pygame.K_LEFT:
                changeTo = 'LEFT'
            if event.key == pygame.K_UP:
                changeTo = 'UP'
            if event.key == pygame.K_DOWN:
                changeTo = 'DOWN'  
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.evet.Event(pygame.QUIT))                                     
    
    #Thực hiện hướng đi
        
        #Không quay đầu
    if changeTo == 'RIGHT' and not snakeDirect == 'LEFT':
        snakeDirect = 'RIGHT'
    if changeTo == 'LEFT' and not snakeDirect == 'RIGHT':
        snakeDirect = 'LEFT'
    if changeTo == 'UP' and not snakeDirect == 'DOWN':
        snakeDirect = 'UP'                        
    if changeTo == 'DOWN' and not snakeDirect == 'UP':
        snakeDirect = 'DOWN'            
        
        #Cập nhật vị trí 
    if snakeDirect == 'RIGHT':
        snakePos[0] += size
    if snakeDirect == 'LEFT' :
        snakePos[0] -= size
    if snakeDirect == 'UP'   :
        snakePos[1] -= size
    if snakeDirect == 'DOWN' :
        snakePos[1] += size
        
    #Tăng kích thước
    snakeBody.insert(0,list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodExist = False
    else: 
        snakeBody.pop()

    #Thêm thức ăn mới
    if foodExist == False:
        foodx = random.randrange(1,71)
        foody = random.randrange(1,45)
        if (foodx % 2 != 0): foodx += 1
        if (foody % 2 != 0): foody += 1
        foodPos= [foodx * 10, foody * 10]
    foodExist = True
    #Hiển thị các phần tử ra màn hình
        #Phần thân và nền màn hình
    gameWindow.fill(black)   
    for pos in snakeBody[0:]:
        pygame.draw.rect(gameWindow,white,pygame.Rect(pos[0],pos[1],size,size))    
        #Phần đầu
    pygame.draw.rect(gameWindow, gray,pygame.Rect(snakePos[0], snakePos[1],size,size))
        #Thức ăn
    pygame.draw.rect(gameWindow,red,pygame.Rect(foodPos[0],foodPos[1],size,size))
        #Đường viền
    pygame.draw.rect(gameWindow,gray,(10,10,720,450),2)
    show_score()

    #Trường hợp GAME OVER
        #Đụng tường
    if snakePos[0] > 710 or snakePos[0] < 10:
        game_over()
    if snakePos[1] > 450 or snakePos[1] < 10:
        game_over()
        #Đụng chính snake (gặp bug: rắn sau loop đầu không tự dài ra mà lại ngắn đi)
    for body in snakeBody[1:]:
        if snakePos[0] == body[0] and snakePos[1] == body[1]:
            game_over()
        
    pygame.display.flip()  

    