import pygame
import sys
import random
from pygame.locals import *
# pip install pygame
class Snake(object):
    # 定义一个颜色的类
    # 制作背景和蛇、果实的的颜色,o~255,0,0,0,是代表黑色，255，255，255代表白色
    def __init__(self):
        self.black = pygame.Color(0, 0, 0)    # 黑色
        self.red = pygame.Color(255, 0, 0)    # 红色
        self.white = pygame.Color(255, 255, 255)   # 白色
    #定义一个游戏结束的类
    def gameover(self):
        pygame.quit()
        sys.exit()   # Esc
    #定义一个初始化
    def initialize(self):
        pygame.init()  # 模块初始化
        # 定义蛇运动的速度
        # 会控制每个循环多长时间运行一次。这就好比，有个定时器在控制着时间进程，一到时间就告诉CPU：
        # 现在该开始循环了！
        clock = pygame.time.Clock()
        # 定义一个游戏界面 ,
        # 生成windows窗口，pygame.display.set_mode。
        # 返回的是一个对象(surface对象是用于表示图像的图像，只要指定尺寸，就可以利用)
        playSurface = pygame.display.set_mode((900, 700))
        # 设置界面名字
        pygame.display.set_caption('贪吃蛇')
        # 初始化变量
        snakePosition = [80, 80]  # 贪吃蛇起始位置，前面的参数数水平方向的距离，后面的参数是垂直方向的距离
        # 贪吃蛇的长度，设定为方块的三百，每个方块的长度为25
        snakebody = [[80, 80], [60, 80], [40, 80]]
        targetPosition = [200, 400]  # 方块的初始位置
        targetflag = 1  # 定义一个标记，目的用来判断果实是否被吃掉
        direction = 'right'  # 初始化运动方向
        changeDirection = direction  # 改变方向变量
        self.main(snakebody,targetPosition,targetflag,direction,changeDirection,snakePosition,playSurface,clock)
    #定义一个主要程序的类
    def main(self,snakebody,targetPosition,targetflag,direction,changeDirection,snakePosition,playSurface,clock):
        while True:   # 键盘监听事件
            # 用循环来获得pygame中的所有事件
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()    # 终止程序
                    sys.exit()

                # 创建一个键盘的事件
                elif event.type == KEYDOWN:
                    # 判断键盘的方向
                    if event.key == K_RIGHT:
                        changeDirection = 'right'
                        print('向右')
                    if event.key == K_LEFT:
                        changeDirection = 'left'
                        print("向左")
                    if event.key == K_DOWN:
                        print('向下')
                        changeDirection = 'down'
                    if event.key == K_UP:
                        print('向上')
                        changeDirection = 'up'
                        # 判断是否按下了esc键
                    if event.key == K_ESCAPE:
                        pygame.event.post(pygame.event.Event(QUIT))

                # 判断蛇的方向
            if (changeDirection == 'left' and not direction == 'right'):
                direction = changeDirection
            if (changeDirection == 'right' and not direction == 'left'):
                direction = changeDirection
            if (changeDirection == 'down' and not direction == 'up'):
                direction = changeDirection
            if (changeDirection == 'up' and not direction == 'down'):
                direction = changeDirection
            # 根据方向移动蛇头位置
            if direction == 'right':
                snakePosition[0] += 20
            if direction == 'left':
                snakePosition[0] -= 20
            if direction == 'up':
                snakePosition[1] -= 20
            if direction == 'down':
                snakePosition[1] += 20

            # 增加蛇的长度
            # 判断蛇是否吃掉了果实
            snakebody.insert(0, list(snakePosition))
            if (snakePosition[0] == targetPosition[0] and snakePosition[1] == targetPosition[1]):
                targetflag = 0
            else:
                snakebody.pop()
            # 随机再生成一个新的方块
            if targetflag == 0:
                x = random.randrange(1, 40)  # 水平方向
                y = random.randrange(1, 30)  # 垂直方向
                targetPosition = [int(x * 20), int(y * 20)]
                targetflag = 1
            # 绘制显示图
            playSurface.fill(self.black)  # 背景
            for position in snakebody:
                pygame.draw.rect(playSurface, self.white, Rect(position[0], position[1], 20, 20))  # 蛇的身体
                pygame.draw.rect(playSurface, self.red, Rect(targetPosition[0], targetPosition[1], 20, 20))  # 果实
            # 游戏结束
            # 蛇碰壁啦
            pygame.display.flip()
            if (snakePosition[0] > 900 or snakePosition[0] < 0):
                snake.gameover()
            elif (snakePosition[1] > 700 or snakePosition[1] < 0):
                snake.gameover()
                # 蛇碰到自己身体啦
            for i in snakebody[1:]:
                if(snakePosition[0] == i[0] and snakePosition[1] == i[1]):
                    snake.gameover()

            # 控制游戏速度，值越大速度越快
            clock.tick(6)

snake = Snake()
snake.initialize()



