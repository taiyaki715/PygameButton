import pygame
from pygame.locals import *

import sys
import threading
import time


class Button:
    def __init__(self, master, posx, posy, x, y, 
                 bg_color=(255, 255, 255), bg_color_onmouse=(255, 255, 0), 
                 text=None, text_font=None, text_color=(255, 255, 255), func=None):
        self.master = master
        self.position = (posx, posy)
        self.size = (x, y)
        self.bg_color = bg_color
        self.bg_color_onmouse = bg_color_onmouse
        self.text = text
        self.text_color = text_color
        self.function = func

        if text_font is None:
            self.text_font = pygame.font.Font(None, 40)
        else:
            self.text_font = text_font

    def _generate(self):
        pygame.draw.rect(self.master, self.bg_color,
                         (*self.position, *self.size))
        text = self.text_font.render(self.text, True, self.text_color)
        self.master.blit(text, (self.get_position()[0] + (self.get_size()[0] - len(self.text)*15) / 2, self.get_position()[1] + self.get_size()[1]*0.5 - 10))

    def _main_loop(self):
        while True:
            self._check_event()
            self._generate()
            pygame.display.update()
            time.sleep(0.05)

    def _check_event(self):
        if self.is_onmouse():
            # マウスオーバ時イベント処理
            self.change_backGround_color(self.bg_color_onmouse)
        else:
            self.change_backGround_color(self.bg_color)
        if self.is_clicked():
            # マウスクリック時イベント処理
            self.function()

    def is_onmouse(self):
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

        if self.get_position()[0] < mouse_x < self.get_position()[0] + self.get_size()[0] and \
           self.get_position()[1] < mouse_y < self.get_position()[1] + self.get_size()[1]:
            return True
        else:
            return False

    def is_clicked(self):
        if self.is_onmouse() and pygame.mouse.get_pressed()[0]:
            # クリック時処理
            pass

    def show(self):
        self._generate()
        self.main_thread = threading.Thread(target=self._main_loop)
        self.main_thread.start()

    def get_size(self):
        return self.size

    def get_position(self):
        return self.position

    def change_backGround_color(self, color):
        self.bg_color = color


# テスト用コード
pygame.init()
screen = pygame.display.set_mode((500, 500))
b = Button(screen, 150, 150, 300, 100, bg_color=(255, 0, 0), text="TEST")
b.show()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

input()
pygame.quit()
sys.exit()
