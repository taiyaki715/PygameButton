import pygame
import threading


class Button:
    def __init__(self, master, posx, posy, x, y, 
                 button_color=(255, 255, 255), onmouse_button_color=(255, 255, 255), 
                 text=None, text_font=None, text_color=(255, 255, 255), func=None):
        self.master = master
        self.position = (posx, posy)
        self.size = (x, y)
        self.color = button_color
        self.color_onmouse = onmouse_button_color
        self.text = text
        self.text_color = text_color
        self.function = func

        if text_font is None:
            self.text_font = pygame.font.Font(None, 40)
        else:
            self.text_font = text_font

    def _make(self):
        pygame.draw.rect(self.master, self.color,
                         (*self.position, *self.size))
        text = self.text_font.render(self.text, True, self.text_color)
        self.master.blit(text, (self.get_position()[0] + (self.get_size()[0] - len(self.text)*15) / 2, self.get_position()[1] + self.get_size()[1]*0.5 - 10))
        pygame.display.update()

    def show(self):
        self.thread = threading.Thread(target=self._make)
        self.thread.start()

    def get_size(self):
        return self.size

    def get_position(self):
        return self.position


pygame.init()
screen = pygame.display.set_mode((1000, 1000))
b = Button(screen, 150, 150, 300, 100, button_color=(255, 0, 0), text="Hello")
b.show()
input()
