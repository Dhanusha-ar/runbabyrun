import pygame
import sys
from pygame.locals import *
from settings import *
from world import World

pygame.init()


class Platformer:

  def __init__(self):

    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Platformer")

    self.clock = pygame.time.Clock()
    self.player_event = False

    self.bg_img = pygame.image.load('assets/terrain/bgb.jpg')
    self.bg_img = pygame.transform.scale(self.bg_img, (WIDTH, HEIGHT))

    self.bg1_img = pygame.image.load('assets/terrain/bgfinal.jpg')
    self.bg1_img = pygame.transform.scale(self.bg1_img, (WIDTH, HEIGHT))

    self.world = World(world_map, self.screen)
    self.in_main_menu = True

  def draw_text(self, text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

  def game(self):
    from world import World
    while True:
      self.screen.blit(self.bg1_img, (0, 0))

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            self.player_event = "left"
          elif event.key == pygame.K_RIGHT:
            self.player_event = "right"
          elif event.key == pygame.K_SPACE:
            self.player_event = "space"
        elif event.type == pygame.KEYUP:
          self.player_event = False

      self.world.update(self.player_event)

      pygame.display.update()
      self.clock.tick(60)

  def main_menu(self):
    from world import World
    while self.in_main_menu:
      # Your game start menu code here
      self.screen.blit(self.bg_img,
                       (0, 0))  # Replace with your background or menu elements

      font = pygame.font.SysFont(None, 50)
      self.draw_text(None, font, (255, 255, 255), self.screen, 50, 40)

      mx, my = pygame.mouse.get_pos()

      start_button = pygame.Rect(380, 150, 150, 50)

      pygame.draw.rect(self.screen, (0,0,0,0), start_button)

      self.draw_text('START', font, (255, 255, 255), self.screen, 400, 160)

      click = False
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
          if event.button == 1:
            if start_button.collidepoint((mx, my)):
              click = True

      pygame.display.update()

      if click:
        self.in_main_menu = False
        self.game()


if __name__ == "__main__":
  play = Platformer()
  play.main_menu()
