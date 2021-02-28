import sys
import threading
import time

import pygame
import pygame.locals


class Button:
    def __init__(self, master,
                 position_x, position_y, size_x, size_y,
                 background_color=(255, 255, 255), text_color=(0, 0, 0),
                 background_color_hovered=(255, 255, 255),
                 text_color_hovered=(0, 0, 0),
                 text="", text_font=None,
                 function=None):

        self.config = {'background': {'color': background_color,
                                      'color_hovered': background_color_hovered},
                       'text': {'color': text_color,
                                'color_hovered': text_color_hovered,
                                'font': text_font},
                       'function': function}

        self.master = master
        self.position = (position_x, position_y)
        self.size = (size_x, size_y)
        self.background_color = self.config['background']['color']
        self.text = text
        self.text_color = self.config['text']['color']

        if self.config['text']['font'] is None:
            self.config['text']['font'] = pygame.font.Font(None, 40)

    def get_position(self):
        """
        Returns button position as tuple.
        """
        return self.position

    def get_size(self):
        """
        Returns button size as tuple.
        """
        return self.size

    def is_hovered(self):
        """
        Return TRUE if mouse cursor is on the button.
        """
        mouse_position_x = pygame.mouse.get_pos()[0]
        mouse_position_y = pygame.mouse.get_pos()[1]

        # Check if mouse cursor is on the button.
        if self.get_position()[0] < mouse_position_x < self.get_position()[0] + self.get_size()[0] and \
           self.get_position()[1] < mouse_position_y < self.get_position()[1] + self.get_size()[1]:
            return True
        else:
            return False

    def is_clicked(self):
        """
        Return TRUE while the button is being clicked.
        """
        if pygame.mouse.get_pressed()[0] and self.is_hovered():
            return True
        else:
            return False

    def show(self):
        """
        Show button.
        """
        # self._draw()
        main_loop = threading.Thread(target=self._loop)
        main_loop.start()

    def _draw(self):
        pygame.draw.rect(self.master, self.background_color,
                         (*self.position, *self.size))
        text = self.config['text']['font'].render(self.text, True, self.config['text']['color'])
        self.master.blit(text, (self.get_position()[0] + (self.get_size()[0] - len(self.text) * 15) / 2, self.get_position()[1] + self.get_size()[1] * 0.5 - 10))

    def _loop(self):
        """
        Main loop.
        """
        while True:
            self._check_event()
            self._draw()
            pygame.display.update()
            time.sleep(0.05)

    def _check_event(self):
        """
        Button event listner.
        """
        if self.is_hovered():
            self.change_background_color(self.config['background']['color_hovered'])
        else:
            self.change_background_color(self.config['background']['color'])
        
        if self.is_clicked():
            self.config['function']

    def change_background_color(self, color):
        """
        Change backgroud color to given RGB data.
        """
        self.background_color = color


"""
Test codes.
"""
pygame.init()
screen = pygame.display.set_mode((500, 500))
b = Button(screen, 150, 150, 300, 100, background_color=(255, 0, 0), text="TEST")
b.show()

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()