import pygame

class Player:

   def __init__(self, screenWidth, screenHeight):

      self.posRangeX = screenWidth
      self.posRangeY = screenHeight

      self.posX = screenWidth/2
      self.posY = screenHeight/2

      self.speed = 10

      self.sizeMax = 20
      self.sizeMin = 10
      # might as well start out at the minimum size
      self.size = self.sizeMin

      self.state = 'growing'

   def updateSize(self):

      # player size changes
      if self.state == 'growing' and self.size >= self.sizeMin:
         self.size = self.size + 1
         if self.size >= self.sizeMax:
            self.state = 'shrinking'

      if self.state == 'shrinking' and self.size <= self.sizeMax:
         self.size = self.size - 1
         if self.size <= self.sizeMin:
            self.state = 'growing'

   def updatePos(self, keys):

      # left border collision detection
      if (self.posX != 0 + self.sizeMax) and (self.posX > 0 + self.sizeMax + 5):
       # player movement input
       if keys[pygame.K_LEFT]:
          self.posX = self.posX - self.speed
      # right border collision detection
      if (self.posX != self.posRangeX - self.sizeMax) and (self.posX < self.posRangeX - (self.sizeMax + 5)):
       # player movement input
       if keys[pygame.K_RIGHT]:
          self.posX = self.posX + self.speed 
      # vertical border collision detection
      if (self.posY != 0 + self.sizeMax) and (self.posY > 0 + self.sizeMax + 5):
       # player movement input
       if keys[pygame.K_UP]:
          self.posY = self.posY - self.speed
      # vertical border collision detection
      if (self.posY != self.posRangeY - self.sizeMax) and (self.posY < self.posRangeY - (self.sizeMax + 5)):
       # player movement input
       if keys[pygame.K_DOWN]:
          self.posY = self.posY + self.speed