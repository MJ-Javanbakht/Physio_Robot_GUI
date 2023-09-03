# Flappy Bird physio
import math
import pygame
import sys
import random
import time 

class Game():
  #START PYGAME MADOULES
  pygame.init()

  # ALL VARIABLE
  display_witdh = 374
  display_height = 650
  floor_x = 0
  #a gravity = 0.2
  #a bird_movment = 0
  bird_list_index = 0
  pipe_list = []
  game_status = True
  game_font = pygame.font.Font('/home/physio/codes/Physio Robot/Physio_Robot_GUI/modules/games/assets/font/Flappy.TTF', 40)
  score = 0
  high_score = 0
  active_score = True

  bird_position = 325
  up = 1

  isotonic_number = 1 ####
  isotonic_pipe = 0   ####

  #--------# 
  win_sound = pygame.mixer.Sound('/home/physio/codes/Physio Robot/Physio_Robot_GUI/modules/games/assets/sound/smb_stomp.wav')
  game_over_sound = pygame.mixer.Sound('/home/physio/codes/Physio Robot/Physio_Robot_GUI/modules/games/assets/sound/smb_mariodie.wav')
  #-------#
  background_image = pygame.transform.rotozoom(pygame.image.load('/home/physio/codes/Physio Robot/Physio_Robot_GUI/modules/games/assets/img/bg2.png'),0 ,1.3)
  floor_image = pygame.transform.rotozoom(pygame.image.load('/home/physio/codes/Physio Robot/Physio_Robot_GUI/modules/games/assets/img/floor.png'), 0, 1.2)

  bird_image_mid = pygame.transform.rotozoom(pygame.image.load('/home/physio/codes/Physio Robot/Physio_Robot_GUI/modules/games/assets/img/red_bird_mid_flap.png'), 0, 1.4)
  bird_image_up = pygame.transform.rotozoom(pygame.image.load('/home/physio/codes/Physio Robot/Physio_Robot_GUI/modules/games/assets/img/red_bird_up_flap.png'), 0, 1.4)
  bird_image_down = pygame.transform.rotozoom(pygame.image.load('/home/physio/codes/Physio Robot/Physio_Robot_GUI/modules/games/assets/img/red_bird_down_flap.png'), 0, 1.4)

  bird_list = [bird_image_mid, bird_image_up, bird_image_down]

  bird_image = bird_list[bird_list_index]

  pipe_image = pygame.transform.rotozoom(pygame.image.load('/home/physio/codes/Physio Robot/Physio_Robot_GUI/modules/games/assets/img/pipe_green.png'), 0, 1.2)

  game_over_image = pygame.transform.rotozoom(pygame.image.load('/home/physio/codes/Physio Robot/Physio_Robot_GUI/modules/games/assets/img/message.png'), 0, 1.2)
  game_over_image_rect = game_over_image.get_rect(center=(187,350))

  # RECTANGEL ARROUND
  bird_image_rect = bird_image.get_rect(center=(50,450)) 

  # CREATE BIRD FLAP
  create_flap = pygame.USEREVENT +1
  pygame.time.set_timer(create_flap, 75)  

  # CREATE PIPE
  create_pipe = pygame.USEREVENT
  pygame.time.set_timer(create_pipe, 4000)   ###

  def start(self):
    #GAME DISPLAY
    self.main_screen = pygame.display.set_mode((self.display_witdh, self.display_height))

    # GAME TIMER
    self.clock = pygame.time.Clock()
  
  def generate_pipe_rect(self) : ####
    isotonic_pipe = round(- math.sin((self.isotonic_number*3.14)/2)*150 + 350)
    pipe_rect_top = self.pipe_image.get_rect(midbottom=(400, isotonic_pipe - 150 ))
    pipe_rect_bottom = self.pipe_image.get_rect(midtop=(400, isotonic_pipe))
    return pipe_rect_top,pipe_rect_bottom

  def move_pipe_rect(self, pipes) :
    for pipe in pipes:
      pipe.centerx -= 2
    inside_pipes = [pipe for pipe in pipes if pipe.right > -50]    
    return inside_pipes
  
  def display_pipes(self, pipes) :
    for pipe in pipes:
      if pipe.bottom >= 500:
        self.main_screen.blit(self.pipe_image, pipe)
      else :
        reversed_pipes = pygame.transform.flip(self.pipe_image, False, True)
        self.main_screen.blit(reversed_pipes, pipe)

  def check_collision(self, pipes):
    # global self.active_score
    for pipe in pipes:
      if self.bird_image_rect.colliderect(pipe):
        self.game_over_sound.play()
        time.sleep(2)
        self.active_score = True
        return False
      if self.bird_image_rect.top <= 0 or self.bird_image_rect.bottom >= 550 :
        self.game_over_sound.play()
        time.sleep(2)
        self.active_score = True
        return False
    return True  

  def brid_animition(self):
    new_bird = self.bird_list[self.bird_list_index]
    new_bird_rect = new_bird.get_rect(center=(50, self.bird_image_rect.centery))
    return new_bird, new_bird_rect

  def display_score(self, status) :
    if status == 'active' :
      text1 = self.game_font.render(str(self.score), False, (255, 255, 255))  
      text1_rect =text1.get_rect(center=(187, 50))
      self.main_screen.blit(text1, text1_rect)
    if status == 'game_over' :
      #SCORE
      text1 = self.game_font.render(f'Score : {self.score}', False, (255, 255, 255))  
      text1_rect =text1.get_rect(center=(187, 50))
      self.main_screen.blit(text1, text1_rect)
      #HIGH SCORE
      text2 = self.game_font.render(f'HighScore : {self.high_score}', False, (0, 255, 0))  
      text2_rect =text2.get_rect(center=(187, 100))
      self.main_screen.blit(text2, text2_rect)

  def update_score(self):
    # global self.score, self.high_score, self.active_score 
    if self.pipe_list:
      for pipe in self.pipe_list:
        if 53 > pipe.centerx > 47 and self.active_score :
          self.score += 1
          self.win_sound.play()
          self.active_score = False 
        if pipe.centerx < 0 :
          self.active_score = True  
    if self.score > self.high_score :
      self.high_score = self.score

    return self.high_score        

  def run(self, node, ROM):
    node.nmt.state = 'OPERATIONAL'
    counter = 0
     ####
    # GAME LOGIC
    while True:
        
        for event in pygame.event.get():
            counter += 1 ###         
            if event.type == pygame.QUIT:
              # END PYGAME MODULES
              pygame.quit()
              return
              # TERMINATE PROGRAM
              sys.exit()
            if event.type == pygame.KEYDOWN :
              if event.key == pygame.K_SPACE :
                bird_movment = 0
                bird_movment -= 5
              if event.key == pygame.K_SPACE and self.game_status == False :
                self.score = 0
                self.game_status = True
                self.pipe_list.clear()
                self.bird_image_rect.center = (50, 450) ###
                bird_movment = 0
                
            if event.type == self.create_pipe :
              self.pipe_list.extend(self.generate_pipe_rect()) 
              self.isotonic_number += 2 ###
            if event.type == self.create_flap :
              if self.bird_list_index < 2:
                self.bird_list_index += 1 
              else :
                self.bird_list_index = 0  
                
              self.bird_image, self.bird_image_rect = self.brid_animition()   
            print(1) ####
            pos = node.tpdo[1]['Position actual value'].raw * 360 / (1280000 * 25)
            self.bird_position =  (pos*6 + 450) ###


        # DISPLAY BG2
        self.main_screen.blit(self.background_image, (0, 0))

        if self.game_status :
          # CHECK COLLISION
          self.game_status = self.check_collision(self.pipe_list)
          # DISPLAY BIRD IMAGE
          self.main_screen.blit(self.bird_image, self.bird_image_rect)
          # DISPLAY GAME     
          # DISPLAY PIPE 
          self.pipe_list = self.move_pipe_rect(self.pipe_list)
          self.display_pipes(self.pipe_list)
          # Bird Gravity and movement
          #a bird_movment += gravity
          #a self.bird_image_rect.centery += bird_movment
          self.bird_image_rect.centery = self.bird_position

          #SHOW SCORE
          self.update_score()
          self.display_score('active')
        else :
          self.main_screen.blit(self.game_over_image, self.game_over_image_rect)
          self.display_score('game_over')  
    
        # DISPLAY FLOOR.PNG
        self.floor_x -= 0.75
        self.main_screen.blit(self.floor_image, (self.floor_x, 540))
        self.main_screen.blit(self.floor_image, (336*1.2+self.floor_x, 540))
        if self.floor_x <= -336*1.2:
            self.floor_x = 0

        
        pygame.display.update()
        # SET GAME SPEED
        self.clock.tick(30)  