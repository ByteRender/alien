import sys

import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()
        # 设定 pygame 窗口大小
        self.screen = pygame.display.set_mode((1200, 800))
        # 设定窗口的标题
        pygame.display.set_caption('Alien')

    def run_game(self):
        # 没有退出的话，游戏应该一直执行，所以用死循环
        while True:
            # 监听pygame中的事件，包含鼠标和键盘事件，以及其它事件
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    # 整个系统退出，并关闭程序和窗口
                    sys.exit()

            # 一直绘制屏幕 帧绘制
            pygame.display.flip()


# python 通用的主入口写法
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
