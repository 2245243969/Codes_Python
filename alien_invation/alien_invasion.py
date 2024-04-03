import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()  # 初始化背景，让Pygame能够正确地工作
        self.clock = pygame.time.Clock()  # 控制帧率
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # 载入飞船

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(120)  # 将游戏的帧率设为120帧

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # 检查按键是否释放
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """响应按下"""
        if event.key == pygame.K_RIGHT:  # 检查按下的键（event.key)是不是右方向键
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # 检查按下的键（event.key)是不是左方向键
            self.ship.moving_left = True

    def _check_keyup_events(self,event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  # 释放是就将ship.moving_right设置为False,让ship.py中控制右移动的循环停止
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)  # 调用fill()方法填充屏幕背景色
        self.ship.blitme()

        pygame.display.flip()  # 让最近绘制的屏幕可见


if __name__ == '__main__':
    """创建游戏实例并运行游戏"""
    ai = AlienInvasion()
    ai.run_game()
