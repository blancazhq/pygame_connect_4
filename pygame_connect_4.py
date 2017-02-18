import pygame
import random


play_again = True

class Win_checker(object):

    def __init__(self, win_marker, winning_location):
        self.win_marker = win_marker

    def win_checker_engine(self, game_record, location_record):
        # i represents columns; j represents rows
        for i in range(4):
            for j in range(3):
                if game_record[i][j].name == game_record[i+1][j].name == game_record[i+2][j].name == game_record[i+3][j].name and game_record[i][j].name != "nothing":
                    self.win_marker = 1
                    self.winning_location = location_record[i][j]
                    return True
                    break
                elif game_record[i][j].name == game_record[i][j+1].name == game_record[i][j+2].name == game_record[i][j+3].name and game_record[i][j].name != "nothing":
                    self.win_marker = 2
                    self.winning_location = location_record[i][j+3]
                    return True
                    break
                elif game_record[i][j].name == game_record[i+1][j+1].name == game_record[i+2][j+2].name == game_record[i+3][j+3].name and game_record[i][j].name != "nothing":
                    self.win_marker = 4
                    self.winning_location = location_record[i][j+3]
                    return True
                    break
                elif game_record[i][j+3].name == game_record[i+1][j+2].name == game_record[i+2][j+1].name == game_record[i+3][j].name and game_record[i][j+3].name != "nothing":
                    self.win_marker = 3
                    self.winning_location = location_record[i][j+3]
                    return True
                    break
                else:
                    continue



class Player1(object):
    def __init__(self,image, input):
        self.input = input
        self.image = image

    def move(self, screen, game_record, row_counter, location_record, background_image):
        #the first index is the column, the second index is the current row.
        screen.blit(background_image, (0,0))
        circle = Circle(self.image,screen)
        game_record[self.input][row_counter[self.input]] = circle
        row_counter[self.input] +=1
        sound = pygame.mixer.Sound('sounds/brush.wav')
        sound.play()
        for i in range(7):
            for j in range(6):
                screen.blit(game_record[i][j].image, location_record[i][j])
        pygame.display.update()



class Player2(object):
    def __init__(self,image, input):
        self.input = input
        self.image = image

    def move(self, screen, game_record, row_counter, location_record, background_image):
        #the first index is the column, the second index is the current row.
        screen.blit(background_image, (0,0))
        star = Star(self.image,screen)
        game_record[self.input][row_counter[self.input]] = star
        row_counter[self.input] +=1
        sound = pygame.mixer.Sound('sounds/brush.wav')
        sound.play()
        for i in range(7):
            for j in range(6):
                screen.blit(game_record[i][j].image, location_record[i][j])
        pygame.display.update()



class Gem (object):
    def __init__(self,image,screen):
        self.image = image

class Nothing(Gem):
    def __init__(self, image):
        self.image = image
        #nothing_image = pygame.image.load('images/nothing.png').convert_alpha()
        self.name = "nothing"

class Star (Gem):
    def __init__(self,image,screen):
        self.name = "star"
        self.image = image
        #pygame.image.load('images/star.png').convert_alpha()

class Circle (Gem):
    def __init__(self,image,screen):
        self.name = "circle"
        self.image = image
        #pygame.image.load('images/circle.png').convert_alpha()

def main():
    global play_again
    global screen



    background_image = pygame.image.load('images/background.png')

    x,y,width,height = background_image.get_rect()

    grid_bound = (x+125, y+123, x+475, y+425)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Connect 4')
    screen.blit(background_image, (0,0))
    pygame.display.update()
    clock = pygame.time.Clock()
    tick = clock.tick(60)
    game_music = pygame.mixer.Sound('sounds/music.wav')
    nothing_image = pygame.image.load('images/nothing.png').convert_alpha()
    circle_image1 = pygame.image.load('images/circle1.png').convert_alpha()
    circle_image2 = pygame.image.load('images/circle2.png').convert_alpha()
    circle_image3 = pygame.image.load('images/circle3.png').convert_alpha()
    star_image1 = pygame.image.load('images/star1.png').convert_alpha()
    star_image2 = pygame.image.load('images/star2.png').convert_alpha()
    star_image3 = pygame.image.load('images/star3.png').convert_alpha()
    win_marker_image1 = pygame.image.load('images/win_marker1.png').convert_alpha()
    win_marker_image2 = pygame.image.load('images/win_marker2.png').convert_alpha()
    win_marker_image3 = pygame.image.load('images/win_marker3.png').convert_alpha()
    win_marker_image4 = pygame.image.load('images/win_marker4.png').convert_alpha()
    background_player1_won_image = pygame.image.load('images/background_player1_won.png').convert_alpha()
    background_player2_won_image = pygame.image.load('images/background_player2_won.png').convert_alpha()
    background_tie_image = pygame.image.load('images/background_tie.png').convert_alpha()
    button_image = pygame.image.load('images/button.png').convert_alpha()
    circle_basket_image = pygame.image.load('images/circle_basket.png').convert_alpha()
    player1_image = pygame.image.load('images/player1.png').convert_alpha()
    star_basket_image = pygame.image.load('images/star_basket.png').convert_alpha()
    player2_image = pygame.image.load('images/player2.png').convert_alpha()


    # game_record is the status of how each cell
    game_record = [[" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "]]
    for i in range(len(game_record)):
        for j in range(len(game_record[0])):
            nothing = Nothing(nothing_image)
            game_record[i][j] = nothing

    location_record = [[(125, 375), (125, 325), (125, 275), (125, 225), (125, 175), (125, 125)],
    [(175, 375), (175, 325), (175, 275), (175, 225), (175, 175), (175, 125)],
    [(225, 375), (225, 325), (225, 275), (225, 225), (225, 175), (225, 125)],
    [(275, 375), (275, 325), (275, 275), (275, 225), (275, 175), (275, 125)],
    [(325, 375), (325, 325), (325, 275), (325, 225), (325, 175), (325, 125)],
    [(375, 375), (375, 325), (375, 275), (375, 225), (375, 175), (375, 125)],
    [(425, 375), (425, 325), (425, 275), (425, 225), (425, 175), (425, 125)]]
    # if player makes a move, the column input's will change the value of its index of the row_counter
    row_counter = [0, 0, 0, 0, 0, 0, 0]
    round_counter = 0
    quit_game = False
    play_again = False
    player_input = -1
    click = False
    win_check = False
    winner = ""
    delay = False
    win_marker = 0
    winning_location = (0, 0)

    game_music.play(-1)

    screen.blit(button_image, (15, 415))
    screen.blit(circle_basket_image, (15, 245))
    screen.blit(player1_image, (15, 200))
    pygame.display.update()

    while not quit_game:

        while click == False and win_check == False and play_again == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop_game = True
                    quit_game = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] in range(125, 175) and event.pos[1] in range(125, 425):
                        player_input = 0
                        click = True
                    if event.pos[0] in range(175, 225) and event.pos[1] in range(125, 425):
                        player_input = 1
                        click = True
                    if event.pos[0] in range(225, 275) and event.pos[1] in range(125, 425):
                        player_input = 2
                        click = True
                    if event.pos[0] in range(275, 325) and event.pos[1] in range(125, 425):
                        player_input = 3
                        click = True
                    if event.pos[0] in range(325, 375) and event.pos[1] in range(125, 425):
                        player_input = 4
                        click = True
                    if event.pos[0] in range(375, 425) and event.pos[1] in range(125, 425):
                        player_input = 5
                        click = True
                    if event.pos[0] in range(425, 475) and event.pos[1] in range(125, 425):
                        player_input = 6
                        click = True
                    if event.pos[0] in range(0, 50) and event.pos[1] in range(425, 475): #new game button
                        play_again = True
                        break
                    if event.pos[0] in range(50, 100) and event.pos[1] in range(425, 475):
                        quit_game = True
                if play_again == True:
                    break

            if play_again == True or quit_game == True:
                break


        while click == True and win_check == False and play_again == False:
            circle_image_list = [circle_image1, circle_image2, circle_image3]
            circle_image = random.choice(circle_image_list)
            player1 = Player1(circle_image, player_input)
            player1.move(screen, game_record, row_counter, location_record, background_image)
            round_counter += 1
            win_checker = Win_checker(win_marker, winning_location)
            if win_checker.win_checker_engine(game_record, location_record) == True:
                win_check = True
                winner = "player 1"
                screen.blit(background_image, (0,0))
                for i in range(7):
                    for j in range(6):
                        screen.blit(game_record[i][j].image, location_record[i][j])
                if win_checker.win_marker == 1:
                    screen.blit(win_marker_image1, win_checker.winning_location)
                elif win_checker.win_marker == 2:
                    screen.blit(win_marker_image2, win_checker.winning_location)
                elif win_checker.win_marker == 3:
                    screen.blit(win_marker_image3, win_checker.winning_location)
                elif win_checker.win_marker == 4:
                    screen.blit(win_marker_image4, win_checker.winning_location)
                pygame.display.update()
            if round_counter >= 42:
                win_check = True
            click = False
            if win_check == False and play_again == False:
                screen.blit(button_image, (15, 415))
                screen.blit(star_basket_image, (15, 245))
                screen.blit(player2_image, (15, 200))
                pygame.display.update()


        while click == False and win_check== False and play_again == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop_game = True
                    quit_game = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] in range(125, 175) and event.pos[1] in range(125, 425):
                        player_input = 0
                        click = True
                    if event.pos[0] in range(175, 225) and event.pos[1] in range(125, 425):
                        player_input = 1
                        click = True
                    if event.pos[0] in range(225, 275) and event.pos[1] in range(125, 425):
                        player_input = 2
                        click = True
                    if event.pos[0] in range(275, 325) and event.pos[1] in range(125, 425):
                        player_input = 3
                        click = True
                    if event.pos[0] in range(325, 375) and event.pos[1] in range(125, 425):
                        player_input = 4
                        click = True
                    if event.pos[0] in range(375, 425) and event.pos[1] in range(125, 425):
                        player_input = 5
                        click = True
                    if event.pos[0] in range(425, 475) and event.pos[1] in range(125, 425):
                        player_input = 6
                        click = True
                    if event.pos[0] in range(0, 50) and event.pos[1] in range(425, 475): #new game button
                        play_again = True
                        break
                    if event.pos[0] in range(50, 100) and event.pos[1] in range(425, 475):
                        quit_game = True
                        break

            if play_again == True or quit_game == True:
                break

        while click == True and win_check == False and play_again == False:
            star_image_list = [star_image1, star_image2, star_image3]
            star_image = random.choice(star_image_list)
            player2 = Player2(star_image, player_input)
            player2.move(screen, game_record, row_counter, location_record, background_image)
            round_counter += 1
            win_checker = Win_checker(win_marker, winning_location)
            if win_checker.win_checker_engine(game_record, location_record) == True:
                win_check = True
                winner = "player 2"
                screen.blit(background_image, (0,0))
                for i in range(7):
                    for j in range(6):
                        screen.blit(game_record[i][j].image, location_record[i][j])
                if win_checker.win_marker == 1:
                    screen.blit(win_marker_image1, win_checker.winning_location)
                elif win_checker.win_marker == 2:
                    screen.blit(win_marker_image2, win_checker.winning_location)
                elif win_checker.win_marker == 3:
                    screen.blit(win_marker_image3, win_checker.winning_location)
                elif win_checker.win_marker == 4:
                    screen.blit(win_marker_image4, win_checker.winning_location)
                pygame.display.update()
            if round_counter >= 42:
                win_check = True
            click = False
            if win_check == False and play_again == False:
                screen.blit(button_image, (15, 415))
                screen.blit(circle_basket_image, (15, 245))
                screen.blit(player1_image, (15, 200))
                pygame.display.update()

        while win_check == True and play_again == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop_game = True
                    quit_game = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] in range(0, 50) and event.pos[1] in range(425, 475): #new game button
                        play_again = True
                        break
                    if event.pos[0] in range(50, 100) and event.pos[1] in range(425, 475):
                        quit_game = True
                        break
            if play_again == True or quit_game == True:
                break
            if winner == "player 1":
                if delay == False:
                    pygame.time.delay(3000)
                    delay = True
                screen.blit(background_player1_won_image, (0,0))
                pygame.display.update()
            elif winner == "player 2":
                if delay == False:
                    pygame.time.delay(3000)
                    delay = True
                screen.blit(background_player2_won_image, (0,0))
                pygame.display.update()
            elif winner == "":
                if delay == False:
                    pygame.time.delay(3000)
                    delay = True
                screen.blit(background_tie_image, (0,0))
                pygame.display.update()
            screen.blit(button_image, (15, 415))
            pygame.display.update()
            play_again = False

        if play_again == True or quit_game == True:
            break



pygame.quit()


if __name__ == '__main__':
    while play_again:
        main()
