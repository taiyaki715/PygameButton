import pygame
from pygame.locals import *

import sys
import threading


class Button:
    def __init__(self, master, posx, posy, x, y, 
                 bg_color=(255, 255, 255), bg_color_onmouse=(255, 255, 255), 
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
        thread = threading.Thread(target=self._main_loop)
        thread.start()
        print('thread started')

    def _main_loop(self):
        while True:
            self._check_event()
            pygame.display.update()

    def _check_event(self):
        if self.is_onmouse():
            print('mouseon')

    def is_onmouse(self):
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

        if self.get_position()[0] < mouse_x < self.get_position()[0] + self.get_size()[0] and \
           self.get_position()[1] < mouse_y < self.get_position()[1] + self.get_size()[1]:
            return True
        else:
            return False

    def is_clicked(self):
        pass

    def show(self):
        self._generate()

    def get_size(self):
        return self.size

    def get_position(self):
        return self.position


def hello():
    print('hello')


pygame.init()
screen = pygame.display.set_mode((1000, 1000))
b = Button(screen, 150, 150, 300, 100, bg_color=(255, 0, 0), text="TEST")
b.show()

while True:
    for event in pygame.event.get():
        pass
    pygame.display.update()

input()
pygame.quit()
sys.exit()
