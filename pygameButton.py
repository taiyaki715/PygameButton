import threading
import time

import pygame
import pygame.locals


class Button:
    def __init__(self, master,
                 position_x, position_y, size_x, size_y,
                 background_color=(255, 255, 255), text_color=(0, 0, 0),
                 background_color_hovered=(255, 255, 255),
                 background_color_clicked=(255, 255, 255),
                 text_color_hovered=(0, 0, 0),
                 text_color_clicked=(0, 0, 0),
                 text="", text_font=None,
                 function=None):

        self.config = {'background': {'color': background_color,
                                      'color_hovered': background_color_hovered,
                                      'color_clicked': background_color_clicked},
                       'text': {'color': text_color,
                                'color_hovered': text_color_hovered,
                                'color_clicked': text_color_clicked,
                                'font': text_font},
                       'function': function}

        self.master = master
        self.position = (position_x, position_y)
        self.size = (size_x, size_y)
        self.background_color = self.config['background']['color']
        self.label = text
        self.text_color = self.config['text']['color']

        self.click_duration = 0

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
        text = self.config['text']['font'].render(self.label, True, self.config['text']['color'])
        self.master.blit(text, (self.get_position()[0] + (self.get_size()[0] - len(self.label) * 15) / 2, self.get_position()[1] + self.get_size()[1] * 0.5 - 10))

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
        if self.is_clicked():
            self.change_background_color(self.config['background']['color_clicked'])
            if self.click_duration == 0:
                self.config['function']()
            self.click_duration += 1
            return
        else:
            self.change_background_color(self.config['background']['color'])
            self.click_duration = 0

        if self.is_hovered():
            self.change_background_color(self.config['background']['color_hovered'])
        else:
            self.change_background_color(self.config['background']['color'])

    def change_background_color(self, color):
        """
        Change backgroud color to given RGB data.
        """
        self.background_color = color
