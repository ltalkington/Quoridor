#Author: Logan Talkington
#Date: 8/1/2021
#Description: This is a program that will play the board game Quoridor with minor variances
import pygame

class QuoridorGame:
    """This is a class for the Quoridor Game and will have all playing functionality inside of it"""

    def __init__(self):
        """Initializes the board game for start"""
        board_count = 0
        fence_count = 0
        self._board = [[' . ' for  board_count in range(9)] for rows in range(9)]
        self._fences = [[' + ' for fence_count in range(9)] for rows in range(9)]
        self._board[0][4] = ' P1'
        self._board[8][4] = ' P2'
        self.player1_position = (0,4)
        self.player2_position = (8,4)
        self._game_over = False
        self._player1_turn = True
        self._player2_turn = False
        self._pawn_in_way_position = ()
        self._player1_fences = 10
        self._player2_fences = 10

    def print_board(self):
        """Prints the board out for views in the terminal"""
        baseline = ['+ ==  ' for count in range(8)]
        print(''.join(baseline))

        for row in range(0,9):
            print('| ' + '  '.join(self._board[row]) + ' |')
            print('+    ' + '  '.join(self._fences[row]))
        print(''.join(baseline))
        print('**********************************************')

    def get_board(self):
        """returns the current board for viewing"""
        new_board = self._board
        return new_board

    def get_player1_fences(self):
        """Returns the fence count for pygame for player 1"""
        return self._player1_fences

    def get_player2_fences(self):
        """Returns the fence count for pygame for player 2"""
        return self._player2_fences



    def get_player1_position(self):
        """Returns player 1 position for pygame class"""
        return self.player1_position

    def get_player2_position(self):
        """Returns player 2 position for pygame class"""
        return self.player2_position

    def get_fences(self):
        """returns the current fences"""
        return self._fences

    def get_game_status(self):
        """Returns the game status for the pygame class"""
        return self._game_over

    def update_player_position(self, player_num, coordinates):
        """This method will update the player's current position on the board"""
        x = coordinates[0]
        y = coordinates[1]
        player1_positionx = self.player1_position[0]
        player1_positiony = self.player1_position[1]
        player2_positionx = self.player2_position[0]
        player2_positiony = self.player2_position[1]
        if player_num == 1:
            self._board[player1_positionx][player1_positiony] = ' . ' #changes the old position of player to nothing
            self.player1_position = (x,y) # changes the position of player1 in the class
        elif player_num == 2:
            self._board[player2_positionx][player2_positiony] = ' . '  # changes the old position of player to nothing
            self.player2_position = (x,y)

    def pawn_in_way_player1(self, player_num, coordinates):
        """This will correspond if there is a pawn in the way of another pawn for moves"""
        x = coordinates[0]
        y = coordinates[1]
        if x < 8 and y < 8:
            if self._board[x + 1][y] == ' P2':
                self._pawn_in_way_position = (x+1, y)
                return True
            elif self._board[x][y + 1] == ' P2':
                self._pawn_in_way_position = (x, y+1)
                return True
            elif self._board[x - 1][y] == ' P2':
                self._pawn_in_way_position = (x - 1, y)
                return True
            elif self._board[x][y - 1] == ' P2':
                self._pawn_in_way_position = (x, y-1)
                return True
        elif x == 8 and y < 8:
            if self._board[x][y + 1] == ' P2':
                self._pawn_in_way_position = (x, y+1)
                return True
            elif self._board[x - 1][y] == ' P2':
                self._pawn_in_way_position = (x - 1, y)
                return True
            elif self._board[x][y - 1] == ' P2':
                self._pawn_in_way_position = (x, y-1)
                return True
        elif x < 8 and y == 8:
            if self._board[x + 1][y] == ' P2':
                self._pawn_in_way_position = (x + 1, y)
                return True
            elif self._board[x - 1][y] == ' P2':
                self._pawn_in_way_position = (x - 1, y)
                return True
            elif self._board[x][y - 1] == ' P2':
                self._pawn_in_way_position = (x, y -1)
                return True

    def pawn_in_way_player2(self, player_num, coordinates):
        """This will correspond if there is a pawn in the way of another pawn for moves"""
        x = coordinates[0]
        y = coordinates[1]
        if x < 8 and y < 8:
            if self._board[x + 1][y] == ' P1':
                self._pawn_in_way_position = (x+1, y)
                return True
            elif self._board[x][y + 1] == ' P1':
                self._pawn_in_way_position = (x, y+1)
                return True
            elif self._board[x - 1][y] == ' P1':
                self._pawn_in_way_position = (x - 1, y)
                return True
            elif self._board[x][y - 1] == ' P1':
                self._pawn_in_way_position = (x, y-1)
                return True
        elif x == 8 and y < 8:
            if self._board[x][y + 1] == ' P1':
                self._pawn_in_way_position = (x, y+1)
                return True
            elif self._board[x - 1][y] == ' P1':
                self._pawn_in_way_position = (x - 1, y)
                return True
            elif self._board[x][y - 1] == ' P1':
                self._pawn_in_way_position = (x, y-1)
                return True
        elif x < 8 and y == 8:
            if self._board[x + 1][y] == ' P1':
                self._pawn_in_way_position = (x + 1, y)
                return True
            elif self._board[x - 1][y] == ' P1':
                self._pawn_in_way_position = (x - 1, y)
                return True
            elif self._board[x][y - 1] == ' P1':
                self._pawn_in_way_position = (x, y -1)
                return True

    def valid_move_player1(self, player_num, coordinates):
        """The if statements for valid move that will determine if a move is
        legal and will pass to the valid move function for player1"""
        x = coordinates[0]
        y = coordinates[1]
        if not self.pawn_in_way_player1(player_num, coordinates):
            if x < 8 and y < 8:
                if self._board[x + 1][y] == ' P1':
                    return True
                elif self._board[x][y + 1] == ' P1':
                    return True
                elif self._board[x - 1][y] == ' P1':
                    return True
                elif self._board[x][y - 1] == ' P1':
                    return True
            elif x == 8 and y < 8:
                if self._board[x][y + 1] == ' P1':
                    return True
                elif self._board[x - 1][y] == ' P1':
                    return True
                elif self._board[x][y - 1] == ' P1':
                    return True
            elif x < 8 and y == 8:
                if self._board[x + 1][y] == ' P1':
                    return True
                elif self._board[x - 1][y] == ' P1':
                    return True
                elif self._board[x][y - 1] == ' P1':
                    return True
        else:
            in_way_x = self._pawn_in_way_position[0]
            in_way_y = self._pawn_in_way_position[1]
            if in_way_y == y and abs(in_way_x - x) == 1:
                return True
            elif in_way_x == x and abs(in_way_y-y):
                return True

    def valid_move_player2(self, player_num, coordinates):
        """The if statements for valid move that will determine if a move is
        legal and will pass to the valid move function for player2"""
        x = coordinates[0]
        y = coordinates[1]
        if not self.pawn_in_way_player2(player_num, coordinates):
            if x < 8 and y < 8:
                if self._board[x + 1][y] == ' P2':
                    return True
                elif self._board[x][y + 1] == ' P2':
                    return True
                elif self._board[x - 1][y] == ' P2':
                    return True
                elif self._board[x][y - 1] == ' P2':
                    return True
            elif x == 8 and y < 8:
                if self._board[x][y + 1] == ' P2':
                    return True
                elif self._board[x - 1][y] == ' P2':
                    return True
                elif self._board[x][y - 1] == ' P2':
                    return True
            elif x < 8 and y == 8:
                if self._board[x + 1][y] == ' P2':
                    return True
                elif self._board[x - 1][y] == ' P2':
                    return True
                elif self._board[x][y - 1] == ' P2':
                    return True
        else:
            in_way_x = self._pawn_in_way_position[0]
            in_way_y = self._pawn_in_way_position[1]
            print(in_way_x - x)

            if in_way_y == y and abs(in_way_x - x) == 1:
                return True
            elif in_way_x == x and abs(in_way_y-y):
                return True

    def fence_in_way(self, player_num, coordinates):
        """A method that will determine if a fence is in a way of a movement for a pawn"""
        x = coordinates[0]
        y = coordinates[1]
        if player_num == 1:
            current_x = self.player1_position[0]
            current_y = self.player1_position[1]
            if x - current_x == 1:
                if '=' in self._fences[x][y]:
                    return False
                return True
            if x - current_x == -1:
                if '=' in self._fences[x][y]:
                    return False
                return True
            if y - current_y == 1:
                if '|' in self._fences[x][y]:
                    return False
                return True
            if y - current_y == -1:
                if '|' in self._fences[x][y+1]:
                    return False
                return True
            else:
                return True
        elif player_num == 2:
            current_x = self.player2_position[0]
            current_y = self.player2_position[1]
            if x - current_x == 1:
                if '=' in self._fences[x][y]:
                    return False
                return True
            if x - current_x == -1:
                if '=' in self._fences[x][y]:
                    return False
                return True
            if y - current_y == 1:
                if '|' in self._fences[x][y]:
                    return False
                return True
            if y - current_y == -1:
                if '|' in self._fences[x][y+1]:
                    return False
                return True
            else:
                return True

    def valid_move(self, player_num, coordinates):
        """determines if a move is valid or not by judging pawn position’s and next coordinates"""
        x = coordinates[0]
        y = coordinates[1]
        if player_num == 1:
            if x == self.player1_position[0] and y == self.player1_position[1]:
                return False
            elif self.valid_move_player1(player_num, coordinates):
                return True
            else:
                return False
        elif player_num == 2:
            if x == self.player2_position[0] and y == self.player2_position[1]:
                return False
            elif self.valid_move_player1(player_num, coordinates):
                return True
            else:
                return False
        else:
            print('no player by that number')

    def move_pawn(self, player_num, coordinates):
        """Functionality to move a pawn on game board and will call other methods to
        verify player turn and validate move """

        if not self._game_over:
            x = coordinates[1]
            y = coordinates[0]
            new_coordinates = (x, y)
            if x > -1 and y > -1:
                if x < 9 and y < 9:
                    if self._player1_turn:
                        if player_num == 1:
                            if self.valid_move(player_num, new_coordinates):
                                if self.fence_in_way(player_num, new_coordinates):
                                    self._board[x][y] = ' P1'
                                    self.update_player_position(player_num, new_coordinates)
                                    self.player1_turn_over()
                                    if self.is_winner(1):
                                        print("Game Over")
                                        self._game_over = True
                                        return "Game is over and player 1 has won"
                                    else:
                                        return True
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    elif self._player2_turn:
                        if player_num == 2:
                            if self.valid_move(player_num, new_coordinates):
                                if self.fence_in_way(player_num, new_coordinates):
                                    self._board[x][y] = ' P2'
                                    self.update_player_position(player_num, new_coordinates)
                                    self.player2_turn_over()
                                    if self.is_winner(2):
                                        self._game_over = True
                                        return "Game is over and player 2 has won"
                                    else:
                                        return True
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def player1_turn_over(self):
        """Makes the turn be player 2's turn instead of player 1"""
        self._player1_turn = False
        self._player2_turn = True

    def player2_turn_over(self):
        """Makes the turn be player 1's turn instead of player 2"""
        self._player1_turn = True
        self._player2_turn = False

    def place_fence(self, player_num, direction, coordinates):
        """This will create functionality to create a fence for either
         player and call other functions to validate move validatity """
        x = coordinates[1]
        y = coordinates[0]
        new_coordinates = (x,y)
        if player_num == 1:
            if self._player1_fences > 0:
                if self._player1_turn:
                    self.fence_placement_player(player_num, direction, new_coordinates)
                    self.player1_turn_over()
                    return True
            else:
                return False
        elif player_num == 2:
            if self._player2_fences > 0:
                if self._player2_turn:
                    self.fence_placement_player(player_num, direction, new_coordinates)
                    self.player2_turn_over()
                    return True
            else:
                return False

    def fence_placement_player(self, player_num, direction, coordinates):
        """This does the placement of a fence for both players"""
        x = coordinates[1]
        y = coordinates[0]
        if direction == 'h':
            if '|' in self._fences[x][y]:
                self._fences[x][y] = '|=+'
                self.print_board()
                self.reduce_fence_count(player_num)
            else:
                self._fences[x][y] = '==+'
                self.print_board()
                self.reduce_fence_count(player_num)
        elif direction == 'v':
            if '==' in self._fences[x][y]:
                self._fences[x][y] = '=|+'
                self.print_board()
                self.reduce_fence_count(player_num)
            else:
                self._fences[x][y] = '|+'
                self.print_board()
                self.reduce_fence_count(player_num)
        else:
            return False

    def reduce_fence_count(self,player_num):
        """This is a method that will reduce the amount of remaining fences a
        player has in their inventory"""
        if player_num == 1:
            self._player1_fences -= 1
        else:
            self._player2_fences -= 1

    def get_player_turn(self):
        """Returns which player's turn it is"""
        if self._player1_turn:
            return 1
        else:
            return 2

    def is_winner(self, player_num):
        """This will return if either player is a winner by seeing if they are
        in the correct endgame baseline or it will return false"""
        if player_num == 1:
            if self.player1_position[0] == 8:
                return True
            else:
                return False
        elif player_num == 2:
            if self.player2_position[0] == 0:
                return True
            else:
                return False

class PygameStart():
    """Creates the pygame implementation"""
    def __init__(self, gameID):
        """Initialzes the pygame functionality"""
        pygame.init()
        pygame.display.set_caption("Quoridor Game")

        self._screen = pygame.display.set_mode((800, 800))
        self._gameID = gameID
        self._board = gameID.get_board()
        self._fences = gameID.get_fences()
        self._player_turn = gameID.get_player_turn()
        self._done = False
        self._BLACK = (0, 0, 0)
        self._WHITE = (200, 200, 200)
        self._P1 = (20, 20, 100)
        self._P2 = (100, 20, 10)
        self._WINDOW_HEIGHT = 400
        self._WINDOW_WIDTH = 400
        self._distance_from_edge= 40
        self._distance_from_top = 20
        self._margin = 10
        self._width = 70
        self._height = 70
        self._current_pos_p1 = self._gameID.get_player1_position()
        self._current_pos_p2 = self._gameID.get_player2_position()
        self._game_over = self._gameID.get_game_status()
        self._fences_count_p1 = self._gameID.get_player1_fences()
        self._fences_count_p2 = self._gameID.get_player2_fences()


    def pygame_run(self):
        """Runs the pygame screen"""
        while not self._done:
            self.create_grid()
            self.update_player_pos()
            self.update_game_status()
            self.update_player_turn()
            self.update_player_fences()

            for event in pygame.event.get():
                player_1x = self._current_pos_p1[0]
                player_1y = self._current_pos_p1[1]
                player_2x = self._current_pos_p2[0]
                player_2y = self._current_pos_p2[1]
                mouse = pygame.mouse.get_pos()
                if self._game_over == False:
                    if pygame.mouse.get_pressed()[0]:
                        if (self._player_turn == 1 and self._fences_count_p1 > 0) or (self._player_turn == 2 and self._fences_count_p2 > 0):
                            print(mouse)
                            if mouse[0] >50 and mouse[0] <120 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0,0))
                            elif mouse[0] >130 and mouse[0] <200 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 1))
                            elif mouse[0] >210 and mouse[0] <280 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 2))
                            elif mouse[0] >290 and mouse[0] <360 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 3))
                            elif mouse[0] >370 and mouse[0] <440 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 4))
                            elif mouse[0] >450 and mouse[0] <520 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 5))
                            elif mouse[0] >530 and mouse[0] <600 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 6))
                            elif mouse[0] >610 and mouse[0] <680 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 7))
                            elif mouse[0] >690 and mouse[0] <760 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 8))
                            ######NEXT column FOR 1
                            elif mouse[0] > 120 and mouse[0] < 130 and mouse[1] > 30 and mouse[1] < 100:
                                self._gameID.place_fence(self._player_turn, 'v', (0, 1))
                            elif mouse[0] >130 and mouse[0] <200 and mouse[1] > 180 and mouse[1] <190:
                                self._gameID.place_fence(self._player_turn, 'h', (1, 1))
                            elif mouse[0] >210 and mouse[0] <280 and mouse[1] > 180 and mouse[1] <190:
                                self._gameID.place_fence(self._player_turn, 'h', (1, 2))
                            elif mouse[0] >290 and mouse[0] <360 and mouse[1] > 180 and mouse[1] <190:
                                self._gameID.place_fence(self._player_turn, 'h', (1, 3))
                            elif mouse[0] >370 and mouse[0] <440 and mouse[1] > 180 and mouse[1] <190:
                                self._gameID.place_fence(self._player_turn, 'h', (1, 4))
                            elif mouse[0] >450 and mouse[0] <520 and mouse[1] > 180 and mouse[1] <190:
                                self._gameID.place_fence(self._player_turn, 'h', (1, 5))
                            elif mouse[0] >530 and mouse[0] <600 and mouse[1] > 180 and mouse[1] <190:
                                self._gameID.place_fence(self._player_turn, 'h', (1, 6))
                            elif mouse[0] >610 and mouse[0] <680 and mouse[1] > 180 and mouse[1] <190:
                                self._gameID.place_fence(self._player_turn, 'h', (1, 7))
                            elif mouse[0] >690 and mouse[0] <760 and mouse[1] > 180 and mouse[1] <190:
                                self._gameID.place_fence(self._player_turn, 'h', (1, 8))
                            ######NEXT ROW FOR 2
                            elif mouse[0] > 50 and mouse[0] < 120 and mouse[1] > 260 and mouse[1] < 270:
                                self._gameID.place_fence(self._player_turn, 'h', (2, 0))
                            elif mouse[0] > 130 and mouse[0] < 200 and mouse[1] > 260 and mouse[1] < 270:
                                self._gameID.place_fence(self._player_turn, 'h', (2, 1))
                            elif mouse[0] > 210 and mouse[0] < 280 and mouse[1] > 260 and mouse[1] < 270:
                                self._gameID.place_fence(self._player_turn, 'h', (2, 2))
                            elif mouse[0] > 290 and mouse[0] < 360 and mouse[1] > 260 and mouse[1] < 270:
                                self._gameID.place_fence(self._player_turn, 'h', (2, 3))
                            elif mouse[0] > 370 and mouse[0] < 440 and mouse[1] > 260 and mouse[1] < 270:
                                self._gameID.place_fence(self._player_turn, 'h', (2, 4))
                            elif mouse[0] > 450 and mouse[0] < 520 and mouse[1] > 260 and mouse[1] < 270:
                                self._gameID.place_fence(self._player_turn, 'h', (2, 5))
                            elif mouse[0] > 530 and mouse[0] < 600 and mouse[1] > 260 and mouse[1] < 270:
                                self._gameID.place_fence(self._player_turn, 'h', (2, 6))
                            elif mouse[0] > 610 and mouse[0] < 680 and mouse[1] > 260 and mouse[1] < 270:
                                self._gameID.place_fence(self._player_turn, 'h', (2, 7))
                            elif mouse[0] > 690 and mouse[0] < 760 and mouse[1] > 260 and mouse[1] < 270:
                                self._gameID.place_fence(self._player_turn, 'h', (2, 8))
                            ######NEXT ROW FOR 3
                            elif mouse[0] > 50 and mouse[0] < 120 and mouse[1] > 340 and mouse[1] < 350:
                                self._gameID.place_fence(self._player_turn, 'h', (3, 0))
                            elif mouse[0] > 130 and mouse[0] < 200 and mouse[1] > 340 and mouse[1] < 350:
                                self._gameID.place_fence(self._player_turn, 'h', (3, 1))
                            elif mouse[0] > 210 and mouse[0] < 280 and mouse[1] > 340 and mouse[1] < 350:
                                self._gameID.place_fence(self._player_turn, 'h', (3, 2))
                            elif mouse[0] > 290 and mouse[0] < 360 and mouse[1] > 340 and mouse[1] < 350:
                                self._gameID.place_fence(self._player_turn, 'h', (3, 3))
                            elif mouse[0] > 370 and mouse[0] < 440 and mouse[1] > 340 and mouse[1] < 350:
                                self._gameID.place_fence(self._player_turn, 'h', (3, 4))
                            elif mouse[0] > 450 and mouse[0] < 520 and mouse[1] > 340 and mouse[1] < 350:
                                self._gameID.place_fence(self._player_turn, 'h', (3, 5))
                            elif mouse[0] > 530 and mouse[0] < 600 and mouse[1] > 340 and mouse[1] < 350:
                                self._gameID.place_fence(self._player_turn, 'h', (3, 6))
                            elif mouse[0] > 610 and mouse[0] < 680 and mouse[1] > 340 and mouse[1] < 350:
                                self._gameID.place_fence(self._player_turn, 'h', (3, 7))
                            elif mouse[0] > 690 and mouse[0] < 760 and mouse[1] > 340 and mouse[1] < 350:
                                self._gameID.place_fence(self._player_turn, 'h', (3, 8))
                            ######NEXT ROW FOR 4
                            elif mouse[0] > 120 and mouse[0] < 130 and mouse[1] > 30 and mouse[1] < 100:
                                self._gameID.place_fence(self._player_turn, 'h', (1, 1))
                            elif mouse[0] > 120 and mouse[0] < 130 and mouse[1] > 420 and mouse[1] < 430:
                                self._gameID.place_fence(self._player_turn, 'h', (4, 1))
                            elif mouse[0] > 210 and mouse[0] < 280 and mouse[1] > 420 and mouse[1] < 430:
                                self._gameID.place_fence(self._player_turn, 'h', (4, 2))
                            elif mouse[0] > 290 and mouse[0] < 360 and mouse[1] > 420 and mouse[1] < 430:
                                self._gameID.place_fence(self._player_turn, 'h', (4, 3))
                            elif mouse[0] > 370 and mouse[0] < 440 and mouse[1] > 420 and mouse[1] < 430:
                                self._gameID.place_fence(self._player_turn, 'h', (4, 4))
                            elif mouse[0] > 450 and mouse[0] < 520 and mouse[1] > 420 and mouse[1] < 430:
                                self._gameID.place_fence(self._player_turn, 'h', (4, 5))
                            elif mouse[0] > 530 and mouse[0] < 600 and mouse[1] > 420 and mouse[1] < 430:
                                self._gameID.place_fence(self._player_turn, 'h', (4, 6))
                            elif mouse[0] > 610 and mouse[0] < 680 and mouse[1] > 420 and mouse[1] < 430:
                                self._gameID.place_fence(self._player_turn, 'h', (4, 7))
                            elif mouse[0] > 690 and mouse[0] < 760 and mouse[1] > 420 and mouse[1] < 430:
                                self._gameID.place_fence(self._player_turn, 'h', (4, 8))
                                ######NEXT ROW FOR 5
                            elif mouse[0] > 50 and mouse[0] < 120 and mouse[1] > 500 and mouse[1] < 510:
                                self._gameID.place_fence(self._player_turn, 'h', (5, 0))
                            elif mouse[0] > 130 and mouse[0] < 200 and mouse[1] > 500 and mouse[1] < 510:
                                self._gameID.place_fence(self._player_turn, 'h', (5, 1))
                            elif mouse[0] > 210 and mouse[0] < 280 and mouse[1] > 500 and mouse[1] < 510:
                                self._gameID.place_fence(self._player_turn, 'h', (5, 2))
                            elif mouse[0] > 290 and mouse[0] < 360 and mouse[1] > 500 and mouse[1] < 510:
                                self._gameID.place_fence(self._player_turn, 'h', (5, 3))
                            elif mouse[0] > 370 and mouse[0] < 440 and mouse[1] > 500 and mouse[1] < 510:
                                self._gameID.place_fence(self._player_turn, 'h', (5, 4))
                            elif mouse[0] > 450 and mouse[0] < 520 and mouse[1] > 500 and mouse[1] < 510:
                                self._gameID.place_fence(self._player_turn, 'h', (5, 5))
                            elif mouse[0] > 530 and mouse[0] < 600 and mouse[1] > 500 and mouse[1] < 510:
                                self._gameID.place_fence(self._player_turn, 'h', (5, 6))
                            elif mouse[0] > 610 and mouse[0] < 680 and mouse[1] > 500 and mouse[1] < 510:
                                self._gameID.place_fence(self._player_turn, 'h', (5, 7))
                            elif mouse[0] > 690 and mouse[0] < 760 and mouse[1] > 500 and mouse[1] < 510:
                                self._gameID.place_fence(self._player_turn, 'h', (5, 8))

                                ######NEXT ROW FOR 6
                            elif mouse[0] > 50 and mouse[0] < 120 and mouse[1] > 580 and mouse[1] < 590:
                                self._gameID.place_fence(self._player_turn, 'h', (6, 0))
                            elif mouse[0] > 130 and mouse[0] < 200 and mouse[1] > 580 and mouse[1] < 590:
                                self._gameID.place_fence(self._player_turn, 'h', (6, 1))
                            elif mouse[0] > 210 and mouse[0] < 280 and mouse[1] > 580 and mouse[1] < 590:
                                self._gameID.place_fence(self._player_turn, 'h', (6, 2))
                            elif mouse[0] > 290 and mouse[0] < 360 and mouse[1] > 580 and mouse[1] < 590:
                                self._gameID.place_fence(self._player_turn, 'h', (6, 3))
                            elif mouse[0] > 370 and mouse[0] < 440 and mouse[1] > 580 and mouse[1] < 590:
                                self._gameID.place_fence(self._player_turn, 'h', (6, 4))
                            elif mouse[0] > 450 and mouse[0] < 520 and mouse[1] > 580 and mouse[1] < 590:
                                self._gameID.place_fence(self._player_turn, 'h', (6, 5))
                            elif mouse[0] > 530 and mouse[0] < 600 and mouse[1] > 580 and mouse[1] < 590:
                                self._gameID.place_fence(self._player_turn, 'h', (6, 6))
                            elif mouse[0] > 610 and mouse[0] < 680 and mouse[1] > 580 and mouse[1] < 590:
                                self._gameID.place_fence(self._player_turn, 'h', (6, 7))
                            elif mouse[0] > 690 and mouse[0] < 760 and mouse[1] > 580 and mouse[1] < 590:
                                self._gameID.place_fence(self._player_turn, 'h', (6, 8))
                                ######NEXT ROW FOR 7
                            elif mouse[0] > 50 and mouse[0] < 120 and mouse[1] > 660 and mouse[1] < 670:
                                self._gameID.place_fence(self._player_turn, 'h', (7, 0))
                            elif mouse[0] > 130 and mouse[0] < 200 and mouse[1] > 660 and mouse[1] < 670:
                                self._gameID.place_fence(self._player_turn, 'h', (7, 1))
                            elif mouse[0] > 210 and mouse[0] < 280 and mouse[1] > 660 and mouse[1] < 670:
                                self._gameID.place_fence(self._player_turn, 'h', (7, 2))
                            elif mouse[0] > 290 and mouse[0] < 360 and mouse[1] > 660 and mouse[1] < 670:
                                self._gameID.place_fence(self._player_turn, 'h', (7, 3))
                            elif mouse[0] > 370 and mouse[0] < 440 and mouse[1] > 660 and mouse[1] < 670:
                                self._gameID.place_fence(self._player_turn, 'h', (7, 4))
                            elif mouse[0] > 450 and mouse[0] < 520 and mouse[1] > 660 and mouse[1] < 670:
                                self._gameID.place_fence(self._player_turn, 'h', (7, 5))
                            elif mouse[0] > 530 and mouse[0] < 600 and mouse[1] > 660 and mouse[1] < 670:
                                self._gameID.place_fence(self._player_turn, 'h', (7, 6))
                            elif mouse[0] > 610 and mouse[0] < 680 and mouse[1] > 660 and mouse[1] < 670:
                                self._gameID.place_fence(self._player_turn, 'h', (7, 7))
                            elif mouse[0] > 690 and mouse[0] < 760 and mouse[1] > 660 and mouse[1] < 670:
                                self._gameID.place_fence(self._player_turn, 'h', (7, 8))
                            elif mouse[0] >50 and mouse[0] <120 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0,0))
                            elif mouse[0] >130 and mouse[0] <200 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 1))
                            elif mouse[0] >210 and mouse[0] <280 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 2))
                            elif mouse[0] >290 and mouse[0] <360 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 3))
                            elif mouse[0] >370 and mouse[0] <440 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 4))
                            elif mouse[0] >450 and mouse[0] <520 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 5))
                            elif mouse[0] >530 and mouse[0] <600 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 6))
                            elif mouse[0] >610 and mouse[0] <680 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 7))
                            elif mouse[0] >690 and mouse[0] <760 and mouse[1] > 100 and mouse[1] <110:
                                self._gameID.place_fence(self._player_turn, 'h', (0, 8))

                            ######NEXT column FOR 1
                            elif mouse[0] > 120 and mouse[0] < 130 and mouse[1] > 30 and mouse[1] < 100:
                                self._gameID.place_fence(self._player_turn, 'v', (1, 0))
                            elif mouse[0] > 120 and mouse[0] < 130 and mouse[1] > 110 and mouse[1] < 180:
                                self._gameID.place_fence(self._player_turn, 'v', (1, 1))
                            elif mouse[0] > 120 and mouse[0] < 130 and mouse[1] > 190 and mouse[1] < 260:
                                self._gameID.place_fence(self._player_turn, 'v', (2, 1))
                            elif mouse[0] > 120 and mouse[0] < 130 and mouse[1] > 270 and mouse[1] < 340:
                                self._gameID.place_fence(self._player_turn, 'v', (3, 1))
                            elif mouse[0] > 120 and mouse[0] < 130 and mouse[1] > 350 and mouse[1] < 420:
                                self._gameID.place_fence(self._player_turn, 'v', (4, 1))
                            elif mouse[0] > 120 and mouse[0] < 130 and mouse[1] > 430 and mouse[1] < 500:
                                self._gameID.place_fence(self._player_turn, 'v', (5, 1))
                            elif mouse[0] > 120 and mouse[0] < 130 and mouse[1] > 510 and mouse[1] < 580:
                                self._gameID.place_fence(self._player_turn, 'v', (6, 1))
                            elif mouse[0] > 120 and mouse[0] < 130 and mouse[1] > 590 and mouse[1] < 660:
                                self._gameID.place_fence(self._player_turn, 'v', (7, 1))
                            elif mouse[0] > 120 and mouse[0] < 130 and mouse[1] > 690 and mouse[1] < 739:
                                self._gameID.place_fence(self._player_turn, 'v', (8, 1))
                                ######NEXT column FOR 2
                            elif mouse[0] > 200 and mouse[0] < 210 and mouse[1] > 30 and mouse[1] < 100:
                                self._gameID.place_fence(self._player_turn, 'v', (0, 2))
                            elif mouse[0] > 200 and mouse[0] < 210 and mouse[1] > 110 and mouse[1] < 180:
                                self._gameID.place_fence(self._player_turn, 'v', (1, 2))
                            elif mouse[0] > 200 and mouse[0] < 210 and mouse[1] > 190 and mouse[1] < 260:
                                self._gameID.place_fence(self._player_turn, 'v', (2, 2))
                            elif mouse[0] > 200 and mouse[0] < 210 and mouse[1] > 270 and mouse[1] < 340:
                                self._gameID.place_fence(self._player_turn, 'v', (3, 2))
                            elif mouse[0] > 200 and mouse[0] < 210 and mouse[1] > 350 and mouse[1] < 420:
                                self._gameID.place_fence(self._player_turn, 'v', (4, 2))
                            elif mouse[0] > 200 and mouse[0] < 210 and mouse[1] > 430 and mouse[1] < 500:
                                self._gameID.place_fence(self._player_turn, 'v', (5, 2))
                            elif mouse[0] > 200 and mouse[0] < 210 and mouse[1] > 510 and mouse[1] < 580:
                                self._gameID.place_fence(self._player_turn, 'v', (6, 2))
                            elif mouse[0] > 200 and mouse[0] < 210 and mouse[1] > 590 and mouse[1] < 660:
                                self._gameID.place_fence(self._player_turn, 'v', (7, 2))
                            elif mouse[0] > 200 and mouse[0] < 210 and mouse[1] > 690 and mouse[1] < 739:
                                self._gameID.place_fence(self._player_turn, 'v', (8, 2))
                                ######NEXT column FOR 3
                            elif mouse[0] > 280 and mouse[0] < 290 and mouse[1] > 30 and mouse[1] < 100:
                                self._gameID.place_fence(self._player_turn, 'v', (0, 3))
                            elif mouse[0] > 280 and mouse[0] < 290 and mouse[1] > 110 and mouse[1] < 180:
                                self._gameID.place_fence(self._player_turn, 'v', (1, 3))
                            elif mouse[0] > 280 and mouse[0] < 290 and mouse[1] > 190 and mouse[1] < 260:
                                self._gameID.place_fence(self._player_turn, 'v', (2, 3))
                            elif mouse[0] > 280 and mouse[0] < 290 and mouse[1] > 270 and mouse[1] < 340:
                                self._gameID.place_fence(self._player_turn, 'v', (3, 3))
                            elif mouse[0] > 280 and mouse[0] < 290 and mouse[1] > 350 and mouse[1] < 420:
                                self._gameID.place_fence(self._player_turn, 'v', (4, 3))
                            elif mouse[0] > 280 and mouse[0] < 290 and mouse[1] > 430 and mouse[1] < 500:
                                self._gameID.place_fence(self._player_turn, 'v', (5, 3))
                            elif mouse[0] > 280 and mouse[0] < 290 and mouse[1] > 510 and mouse[1] < 580:
                                self._gameID.place_fence(self._player_turn, 'v', (6, 3))
                            elif mouse[0] > 280 and mouse[0] < 290 and mouse[1] > 590 and mouse[1] < 660:
                                self._gameID.place_fence(self._player_turn, 'v', (7, 3))
                            elif mouse[0] > 280 and mouse[0] < 290 and mouse[1] > 690 and mouse[1] < 739:
                                self._gameID.place_fence(self._player_turn, 'v', (8, 3))
                                ######NEXT column FOR 4
                            elif mouse[0] > 360 and mouse[0] < 370 and mouse[1] > 30 and mouse[1] < 100:
                                self._gameID.place_fence(self._player_turn, 'v', (0, 4))
                            elif mouse[0] > 360 and mouse[0] < 370 and mouse[1] > 110 and mouse[1] < 180:
                                self._gameID.place_fence(self._player_turn, 'v', (1, 4))
                            elif mouse[0] > 360 and mouse[0] < 370 and mouse[1] > 190 and mouse[1] < 260:
                                self._gameID.place_fence(self._player_turn, 'v', (2, 4))
                            elif mouse[0] > 360 and mouse[0] < 370 and mouse[1] > 270 and mouse[1] < 340:
                                self._gameID.place_fence(self._player_turn, 'v', (3, 4))
                            elif mouse[0] > 360 and mouse[0] < 370 and mouse[1] > 350 and mouse[1] < 420:
                                self._gameID.place_fence(self._player_turn, 'v', (4, 4))
                            elif mouse[0] > 360 and mouse[0] < 370 and mouse[1] > 430 and mouse[1] < 500:
                                self._gameID.place_fence(self._player_turn, 'v', (5, 4))
                            elif mouse[0] > 360 and mouse[0] < 370 and mouse[1] > 510 and mouse[1] < 580:
                                self._gameID.place_fence(self._player_turn, 'v', (6, 4))
                            elif mouse[0] > 360 and mouse[0] < 370 and mouse[1] > 590 and mouse[1] < 660:
                                self._gameID.place_fence(self._player_turn, 'v', (7, 4))
                            elif mouse[0] > 360 and mouse[0] < 370 and mouse[1] > 690 and mouse[1] < 739:
                                self._gameID.place_fence(self._player_turn, 'v', (8, 4))
                                ######NEXT column FOR 5
                            elif mouse[0] > 440 and mouse[0] < 450 and mouse[1] > 30 and mouse[1] < 100:
                                self._gameID.place_fence(self._player_turn, 'v', (0, 5))
                            elif mouse[0] > 440 and mouse[0] < 450 and mouse[1] > 110 and mouse[1] < 180:
                                self._gameID.place_fence(self._player_turn, 'v', (1, 5))
                            elif mouse[0] > 440 and mouse[0] < 450 and mouse[1] > 190 and mouse[1] < 260:
                                self._gameID.place_fence(self._player_turn, 'v', (2, 5))
                            elif mouse[0] > 440 and mouse[0] < 450 and mouse[1] > 270 and mouse[1] < 340:
                                self._gameID.place_fence(self._player_turn, 'v', (3, 5))
                            elif mouse[0] > 440 and mouse[0] < 450 and mouse[1] > 350 and mouse[1] < 420:
                                self._gameID.place_fence(self._player_turn, 'v', (4, 5))
                            elif mouse[0] > 440 and mouse[0] < 450 and mouse[1] > 430 and mouse[1] < 500:
                                self._gameID.place_fence(self._player_turn, 'v', (5, 5))
                            elif mouse[0] > 440 and mouse[0] < 450 and mouse[1] > 510 and mouse[1] < 580:
                                self._gameID.place_fence(self._player_turn, 'v', (6, 5))
                            elif mouse[0] > 440 and mouse[0] < 450 and mouse[1] > 590 and mouse[1] < 660:
                                self._gameID.place_fence(self._player_turn, 'v', (7, 5))
                            elif mouse[0] > 440 and mouse[0] < 450 and mouse[1] > 690 and mouse[1] < 739:
                                self._gameID.place_fence(self._player_turn, 'v', (8, 5))
                                ######NEXT column FOR 6
                            elif mouse[0] > 520 and mouse[0] < 530 and mouse[1] > 30 and mouse[1] < 100:
                                self._gameID.place_fence(self._player_turn, 'v', (0, 6))
                            elif mouse[0] > 520 and mouse[0] < 530 and mouse[1] > 110 and mouse[1] < 180:
                                self._gameID.place_fence(self._player_turn, 'v', (1, 6))
                            elif mouse[0] > 520 and mouse[0] < 530 and mouse[1] > 190 and mouse[1] < 260:
                                self._gameID.place_fence(self._player_turn, 'v', (2, 6))
                            elif mouse[0] > 520 and mouse[0] < 530 and mouse[1] > 270 and mouse[1] < 340:
                                self._gameID.place_fence(self._player_turn, 'v', (3, 6))
                            elif mouse[0] > 520 and mouse[0] < 530 and mouse[1] > 350 and mouse[1] < 420:
                                self._gameID.place_fence(self._player_turn, 'v', (4, 6))
                            elif mouse[0] > 520 and mouse[0] < 530 and mouse[1] > 430 and mouse[1] < 500:
                                self._gameID.place_fence(self._player_turn, 'v', (5, 6))
                            elif mouse[0] > 520 and mouse[0] < 530 and mouse[1] > 510 and mouse[1] < 580:
                                self._gameID.place_fence(self._player_turn, 'v', (6, 6))
                            elif mouse[0] > 520 and mouse[0] < 530 and mouse[1] > 590 and mouse[1] < 660:
                                self._gameID.place_fence(self._player_turn, 'v', (7, 6))
                            elif mouse[0] > 520 and mouse[0] < 530 and mouse[1] > 690 and mouse[1] < 739:
                                self._gameID.place_fence(self._player_turn, 'v', (8, 6))
                                ######NEXT column FOR 7
                            elif mouse[0] > 600 and mouse[0] < 610 and mouse[1] > 30 and mouse[1] < 100:
                                self._gameID.place_fence(self._player_turn, 'v', (0, 7))
                            elif mouse[0] > 600 and mouse[0] < 610 and mouse[1] > 110 and mouse[1] < 180:
                                self._gameID.place_fence(self._player_turn, 'v', (1, 7))
                            elif mouse[0] > 600 and mouse[0] < 610 and mouse[1] > 190 and mouse[1] < 260:
                                self._gameID.place_fence(self._player_turn, 'v', (2, 7))
                            elif mouse[0] > 600 and mouse[0] < 610 and mouse[1] > 270 and mouse[1] < 340:
                                self._gameID.place_fence(self._player_turn, 'v', (3, 7))
                            elif mouse[0] > 600 and mouse[0] < 610 and mouse[1] > 350 and mouse[1] < 420:
                                self._gameID.place_fence(self._player_turn, 'v', (4, 7))
                            elif mouse[0] > 600 and mouse[0] < 610 and mouse[1] > 430 and mouse[1] < 500:
                                self._gameID.place_fence(self._player_turn, 'v', (5, 7))
                            elif mouse[0] > 600 and mouse[0] < 610 and mouse[1] > 510 and mouse[1] < 580:
                                self._gameID.place_fence(self._player_turn, 'v', (6, 7))
                            elif mouse[0] > 600 and mouse[0] < 610 and mouse[1] > 590 and mouse[1] < 660:
                                self._gameID.place_fence(self._player_turn, 'v', (7, 7))
                            elif mouse[0] > 600 and mouse[0] < 610 and mouse[1] > 690 and mouse[1] < 739:
                                self._gameID.place_fence(self._player_turn, 'v', (8, 7))
                                ######NEXT column FOR 7
                            elif mouse[0] > 680 and mouse[0] < 690 and mouse[1] > 30 and mouse[1] < 100:
                                self._gameID.place_fence(self._player_turn, 'v', (0, 8))
                            elif mouse[0] > 680 and mouse[0] < 690 and mouse[1] > 110 and mouse[1] < 180:
                                self._gameID.place_fence(self._player_turn, 'v', (1, 8))
                            elif mouse[0] > 680 and mouse[0] < 690 and mouse[1] > 190 and mouse[1] < 260:
                                self._gameID.place_fence(self._player_turn, 'v', (2, 8))
                            elif mouse[0] > 680 and mouse[0] < 690 and mouse[1] > 270 and mouse[1] < 340:
                                self._gameID.place_fence(self._player_turn, 'v', (3, 8))
                            elif mouse[0] > 680 and mouse[0] < 690 and mouse[1] > 350 and mouse[1] < 420:
                                self._gameID.place_fence(self._player_turn, 'v', (4, 8))
                            elif mouse[0] > 680 and mouse[0] < 690 and mouse[1] > 430 and mouse[1] < 500:
                                self._gameID.place_fence(self._player_turn, 'v', (5, 8))
                            elif mouse[0] > 680 and mouse[0] < 690 and mouse[1] > 510 and mouse[1] < 580:
                                self._gameID.place_fence(self._player_turn, 'v', (6, 8))
                            elif mouse[0] > 680 and mouse[0] < 690 and mouse[1] > 590 and mouse[1] < 660:
                                self._gameID.place_fence(self._player_turn, 'v', (7, 8))
                            elif mouse[0] > 680 and mouse[0] < 690 and mouse[1] > 690 and mouse[1] < 739:
                                self._gameID.place_fence(self._player_turn, 'v', (8, 8))
                    if event.type == pygame.QUIT:
                        self._done = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            if self._gameID.get_player_turn() == 1:
                                self._gameID.move_pawn(1, (player_1y, player_1x - 1))
                            else:
                                self._gameID.move_pawn(2, (player_2y, player_2x - 1))
                        elif event.key == pygame.K_a:
                            if self._gameID.get_player_turn() == 1:
                                print(self._gameID.move_pawn(1, (player_1y - 1, player_1x)))
                                print('this is stuff ' , player_1y -1 , player_1x)
                            else:
                                self._gameID.move_pawn(2, (player_2y -1, player_2x))
                        elif event.key == pygame.K_s:
                            if self._gameID.get_player_turn() == 1:
                                self._gameID.move_pawn(1, (player_1y, player_1x + 1))
                            else:
                                self._gameID.move_pawn(2, (player_2y, player_2x + 1))
                        elif event.key == pygame.K_d:
                            if self._gameID.get_player_turn() == 1:
                                self._gameID.move_pawn(1, (player_1y + 1, player_1x))
                            else:
                                self._gameID.move_pawn(2, (player_2y + 1, player_2x))
                else:
                    pygame.font.init()
                    myfont = pygame.font.SysFont('Comic Sans MS', 50)
                    textsurface = myfont.render('Game Over', False, (200, 100, 100))
                    pygame.draw.rect(self._screen, (255, 255, 255), [280, 300, 300, 100])
                    self._screen.blit(textsurface, (300, 300))

                pygame.display.flip()

    def update_board(self):
        """update the playing board by calling the Quoridor class again"""
        next_board = self._gameID.get_board()
        self._board = next_board

    def update_game_status(self):
        """updates the game status by calling the Quoridor class"""
        next_status = self._gameID.get_game_status()
        self._game_over = next_status

    def update_player_pos(self):
        """updates the player's position of both player 1 and 2"""
        self._current_pos_p1 = self._gameID.get_player1_position()
        self._current_pos_p2 = self._gameID.get_player2_position()

    def update_player_turn(self):
        """Moves the player turn into the main playing function"""
        next = self._gameID.get_player_turn()
        self._player_turn = next

    def update_player_fences(self):
        """updates the player fence counts"""
        next_p1 = self._gameID.get_player1_fences()
        next_p2 = self._gameID.get_player2_fences()
        self._fences_count_p1 = next_p1
        self._fences_count_p2 = next_p2

    def create_grid(self):
        """Creates an initial grid"""
        self.update_board()
        for boardRow in range(9):
            for boardColumn in range(9):
                xCoordinate = ((self._margin + self._width) * boardColumn + self._margin) + self._distance_from_edge
                yCoordinate = ((self._margin + self._height) * boardRow + self._margin) + self._distance_from_top

                if '.' in self._board[boardRow][boardColumn]:
                    current_color = self._WHITE
                    pygame.draw.rect(self._screen, current_color, [xCoordinate, yCoordinate, self._width, self._height])
                elif 'P1' in self._board[boardRow][boardColumn]:
                    current_color = self._P1
                    pygame.draw.rect(self._screen, current_color, [xCoordinate, yCoordinate, self._width, self._height])
                elif 'P2' in self._board[boardRow][boardColumn]:
                    current_color = self._P2
                    pygame.draw.rect(self._screen, current_color, [xCoordinate, yCoordinate, self._width, self._height])
                else:
                    print('nothing')
                if '|' in self._fences[boardRow][boardColumn] and '==' in self._fences[boardRow][boardColumn]:
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate-6, yCoordinate), (xCoordinate - 6, yCoordinate + 70), 6)
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate, yCoordinate+74), (xCoordinate + 70, yCoordinate + 74), 6)
                elif '|' in self._fences[boardRow][boardColumn]:
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate-6, yCoordinate), (xCoordinate - 6, yCoordinate + 70), 6)
                elif '==' in self._fences[boardRow][boardColumn]:
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate, yCoordinate+74), (xCoordinate + 70, yCoordinate +74), 6)

                if boardColumn == 0 and boardRow == 8:
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate-7, yCoordinate), (xCoordinate - 7, yCoordinate + 70), 6)
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate, yCoordinate +75), (xCoordinate + 70, yCoordinate+75), 6)

                elif boardColumn == 8 and boardRow == 0:
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate + 70, yCoordinate-7),
                                     (xCoordinate, yCoordinate-7), 6)
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate + 75, yCoordinate),
                                     (xCoordinate + 75, yCoordinate + 70), 6)
                elif boardColumn == 0 and boardRow == 0:
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate - 7, yCoordinate),
                                     (xCoordinate - 7, yCoordinate + 70), 6)
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate, yCoordinate - 7),
                                     (xCoordinate + 70, yCoordinate - 7), 6)
                elif boardColumn == 8 and boardRow == 8:
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate + 75, yCoordinate),
                                     (xCoordinate + 75, yCoordinate + 70), 6)
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate, yCoordinate + 75),
                                     (xCoordinate + 70, yCoordinate + 75), 6)
                elif boardRow == 8 and (boardColumn != 8 or boardColumn != 0):
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate + 70, yCoordinate + 75), (xCoordinate, yCoordinate + 75), 6)
                elif boardColumn == 8 and (boardRow != 8 or boardRow != 0):
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate + 75, yCoordinate + 70), (xCoordinate + 75, yCoordinate), 6)
                elif boardColumn == 8 and boardRow == 8:
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate + 75, yCoordinate + 70), (xCoordinate + 75, yCoordinate), 6)
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate + 70, yCoordinate + 75), (xCoordinate, yCoordinate + 75), 6)
                elif boardRow == 0 and boardColumn != 8:
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate, yCoordinate -7), (xCoordinate + 70, yCoordinate-7), 6)
                elif boardColumn == 0 and boardRow != 8:
                    pygame.draw.line(self._screen, (110, 220, 255), (xCoordinate-7, yCoordinate), (xCoordinate - 7, yCoordinate + 70), 6)

if __name__ == '__main__':
    q1 = QuoridorGame()
    #print(q1.move_pawn(1, (3, 0)))
    #q1.place_fence(2, 'v', (1,6))
    #q1.place_fence(1, 'h', (7, 4))
    #q1.move_pawn(2, (5, 8))
    #q1.move_pawn(1, (4, 2))
    #q1.move_pawn(2, (6, 8))
    #q1.move_pawn(1, (4, 3))
    #q1.print_board()
    p1 = PygameStart(q1)
    p1.pygame_run()

