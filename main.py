###########################
#Nach einem Punkt soll countdown kommen danach startet der ball wieder von der Mitte
###########################





import pygame
from paddle import Paddle
from ball import Ball
import time

pygame.init()


BLACK = ( 0,0,0 )
WHITE = ( 255,255,255 )

Width = 700
Height = 500

screenSize = (700, 500)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Pong")


#OBJECTS
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195


#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()


def text_objects(text, font):
  textSurface = font.render(text, True, WHITE)
  return textSurface, textSurface.get_rect()


def message_display(text, scoreA, scoreB):
  largeText = pygame.font.Font('freesansbold.ttf', 50)
  TextSurf, TextRect = text_objects(text, largeText)
  TextRect.center = ((Width / 2), (Height / 2))
  screen.blit(TextSurf, TextRect)

  pygame.display.update()

  time.sleep(2)

  main_loop(scoreA, scoreB)

def newRound(scoreA, scoreB):
  message_display('Next Round get Ready', scoreA, scoreB)



# -----------Main Program----------
def main_loop(scoreA, scoreB):

  # The loop will be used to control how fast the screen updates
  carryOn = True

  #Initialise player scores
  # scoreA = 0
  # scoreB = 0


  while carryOn:
    # Main event loop
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_x:
          pygame.quit()
      #print(event)

    #Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
      paddleA.moveUp(5)
    if keys[pygame.K_s]:
      paddleA.moveDown(5)
    if keys[pygame.K_UP]:
      paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
      paddleB.moveDown(5)

    # --------Game logic should go here
    all_sprites_list.update()


    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=690:
      scoreA += 1
      if scoreA == 5:
        pygame.quit()
        quit()
      ball.rect.x = 345
      ball.rect.y = 195
      pygame.display.update()
      newRound(scoreA, scoreB)
      ball.velocity[0] = -ball.velocity[0]
      #pygame.display.update(ball)
    if ball.rect.x<=0:
      scoreB += 1
      if scoreB == 5:
        pygame.quit()
        quit()
      ball.rect.x = 345
      ball.rect.y = 195
      pygame.display.update()
      newRound(scoreA, scoreB)
      ball.velocity[0] = -ball.velocity[0]
      #pygame.display.update(ball)
    if ball.rect.y>490:
      ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
      ball.velocity[1] = -ball.velocity[1] 

    # Detect collision between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
      ball.bounce()


    # ---- Drawing code should go here
    # First, clear the screen to black
    screen.fill(BLACK)
    #Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    # Now lets draw all the sprites in one go.
    all_sprites_list.draw(screen)


    #Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))

    # --- Go ahead and update the screen with what we have drawn
    pygame.display.update()

    # ---- Limit to 60 frames per second
    clock.tick(60)



main_loop(0,0)
# Once we have exited the main programm loop we can stop the game engine:
pygame.quit()

