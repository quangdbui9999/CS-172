'''
Full name: Quang Bui
Drexel user ID: 14392331
Purpose of the file: HW4.py will contain the main script of all the program.
'''


import pygame
from ball import Ball
from block import Block
from text import Text
from background import BackgroundEnvironment
from fileProcessing import FileProcessing

# Function that returns if two rectangles intersect:
def intersect(rect1, rect2):
    if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (
            rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
        return True
    return False

def exitGame():
    if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
        pygame.quit()
        print("THE PROGRAM IS FINISHED")
        exit()

# Main Script
if __name__ == "__main__":
    # Get the Mouse location
    mouse_location_pressed = (0, 0)
    xv = 0
    yv = 0

    # Some constant number
    DELTA_TIME = 0.1
    GRAVITY = 6.67
    REBOUND_CONSTANT = 0.7
    COEFFICIENT_FRICTION = 0.5

    RADIANT_ORCHILD = (181, 101, 167)
    CHILI_PEPPER = (155, 35, 53)
    TANGERINE_TANGO = (221, 65, 36)
    HONEYSUCLE = (214, 80, 118)

    WIDTH_SCREEN = 1200
    HEIGHT_SCREEN = 800
    TEXT_CAPTION = "CS-172-Quang's Game"
    X_LEFT_BOUNDARY = 13
    X_RIGHT_BOUNDARY = 1180
    Y_TOP_BOUNDARY = 13
    Y_BOTTOM_BOUNDARY = 702
    ERROR = 0.0001

    # Press letter 'p' on keyboard to Pause the Game
    pauseGame = False  # False: game is playing
    score = 0 # the score update when a Ball hits Blocks

    # Initialize the environment
    pygame.init()

    # Set up the Background Image
    background_environment = BackgroundEnvironment()

    # Set up the Screen's size
    surface = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))

    # Set Screen's caption
    pygame.display.set_caption(TEXT_CAPTION)

    #
    #surface.fill((255, 255, 128))

    # Set up for the animation
    fpsclock = pygame.time.Clock()

    # drawables: is a list contain some blocks
    drawables = []

    # Create the blocks
    newBlock = Block(630, 500)
    newBlock.smallBlock(drawables, 1050, 200)
    newBlock.mediumBlock(drawables, 1065, 400)
    newBlock.largeBlock(drawables, 1080, 700)

    # Create a Ball
    newBall = Ball(50, HEIGHT_SCREEN - 85, (255, 0, 0))
    newBall.setVisible(True)
    positionBall = list(newBall.getLocation())

    # count_block will How many Block that are created
    count_block = len(drawables)

    # Create Text
    newText = Text(f"Score: {int(score)}", 5, 5, RADIANT_ORCHILD, 32)

    # winGame Text will appear when we Finish Game
    winGame = Text(f"CONGRATULATION! YOU WON THE GAME", 45, 240, CHILI_PEPPER, 52)

    # Create FileProcessing
    fileScore = FileProcessing()

    # Game: Main loop
    while True:
        # We select the event for the game
        for event in pygame.event.get():
            # Event handling the Pause Game
            if event.type == pygame.KEYDOWN:
                if event.__dict__['key'] == pygame.K_p:
                    pauseGame = True
            # Event Handling to :aunch the Ball
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_location_pressed = pygame.mouse.get_pos()
                xv = mouse_location_pressed[0] - positionBall[0]
                yv = (mouse_location_pressed[1] - positionBall[1]) * (-1)

            # Event Handling to Quit the Game
            exitGame()

        # Pause the game
        while pauseGame == True:
            # Event Handling
            for event in pygame.event.get():
                exitGame()
                # Check the number of block is empty
                if (count_block) == 0: # check emply
                    pygame.time.delay(6000) # pause the Game 6 seconds and then quiting the Game
                    pygame.quit()
                    exit()
                # If users press letter 'p' on Keyboard => Game is playing
                if event.type == pygame.KEYDOWN:
                    if event.__dict__['key'] == pygame.K_p:
                        pauseGame = False

        #surface.fill((255, 255, 128))
        # Insert background environment
        surface.blit(background_environment.getImage(), background_environment.getLocation())

        # Draw the line
        pygame.draw.line(surface, (0, 0, 0), (0, HEIGHT_SCREEN - 85), (WIDTH_SCREEN, HEIGHT_SCREEN - 85), 3)

        for drawable in drawables:
            # Check the Ball and Blocks are intersect
            if intersect(newBall.get_rect(), drawable.get_rect()) and drawable.getVisible():
                count_block -= 1 # remove the blocks from the drawables list
                drawable.setVisible(False) # make the block is invisible
                score = score + 1 # get score for each bloxk
                newText.setScore(score) # update score
                newText.setMessage(f"Score: {int(newText.getScore())}", 30) # update score on Graphic User Interface

            # if the Blocks are visible
            if drawable.getVisible():
                #draw the blocks
                drawable.draw(surface)
        #winGame.draw(surface)
        # Check the block is emplty

        if count_block == 0:
            winGame.draw(surface)
            # print the maximum and total score of file "highScore.txt"
            fileScore.writeFile(score)
            maxScore = Text(f"Max Score is: {fileScore.getMaxScore()}.", WIDTH_SCREEN - 880, Y_BOTTOM_BOUNDARY - 360, TANGERINE_TANGO, 64)
            maxScore.draw(surface)
            totalScore = Text(f"Total Score is: {fileScore.getTotlaScore()}.", WIDTH_SCREEN - 900, Y_BOTTOM_BOUNDARY - 240, HONEYSUCLE, 64)
            totalScore.draw(surface)

            pauseGame = True

        # Compute the xv (increase in the x direction) and yv (decrease in the y-direction)
        if abs(float(yv)) >= ERROR:
            positionBall[0] = int(positionBall[0] + (xv * DELTA_TIME))
            positionBall[1] = int(positionBall[1] - (yv * DELTA_TIME))
            newBall.setLocation(positionBall)

            # Check boundary, make the Ball always on the Screen and on the bottom line
            if not (X_LEFT_BOUNDARY <= positionBall[0] <= X_RIGHT_BOUNDARY):
                yv = COEFFICIENT_FRICTION * yv
                xv = REBOUND_CONSTANT * (-1) * xv
            if not (Y_TOP_BOUNDARY <= positionBall[1] <= Y_BOTTOM_BOUNDARY):
                xv = COEFFICIENT_FRICTION * xv
                yv = REBOUND_CONSTANT * (-1) * yv
            else:
                yv = yv - (GRAVITY * DELTA_TIME)

        # Update the Ball and Score
        newText.draw(surface)
        newBall.draw(surface)

        # Update the Screen
        pygame.display.update()
        fpsclock.tick(30)