import asyncio
import pygame
import time

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Chess")

font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
button_font = pygame.font.Font('freesansbold.ttf', 30)



async def main():
    timer= pygame.time.Clock()
    fps = 60
    #region Game variable and images
    white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', "knight", 'rook',
                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    white_location = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), 
                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
    black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', "knight", 'rook',
                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    black_location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), 
                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
    #white_location = [(0, 7), (1, 7), (2, 7), (3, 7), (2, 3), (5, 7), (6, 7), (7, 7), 
    #                  (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
    #black_location = [(0, 0), (1, 0), (2, 0), (1, 5), (4, 3), (5, 0), (6, 0), (7, 0), 
    #                  (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
    #white_pieces = ['rook', 'knight', 'bishop', 'king', 'bishop', 'knight', 'rook', 
    #                   'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    #white_location = [(0, 7), (4, 3), (2, 7), (2, 6), (5, 7), (6, 7), (7, 7),
    #                  (0, 6), (1, 5), (3, 6), (6, 6), (7, 6)]
    #black_pieces = ['rook', 'knight', 'bishop', 'king', 'bishop', "knight", 'rook',
    #                   'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    #black_location = [(0, 0), (1, 0), (5, 3), (4, 0), (1, 4), (6, 0), (7, 0),
    #                  (0, 1), (1, 1), (2, 1), (2, 3), (5, 1), (6, 1), (7, 1)]
    white_king_place = white_location[white_pieces.index('king')]
    black_king_place = black_location[black_pieces.index('king')]
    WAITING_INTERVAL = 2  # seconds



    captured_pieces_white = []
    captured_pieces_black = []
    #endregion 

    # 0 - white turn | 1 - black turn
    turn_step = 0
    selection = 100
    valid_moves = []

    #region Load in game piece images
    black_queen = pygame.image.load('assets/images/black queen.png')
    black_queen = pygame.transform.scale(black_queen, (65, 65))
    black_queen_small = pygame.transform.scale(black_queen, (45, 45))
    black_king = pygame.image.load('assets/images/black king.png')
    black_king = pygame.transform.scale(black_king, (65, 65))
    black_king_small = pygame.transform.scale(black_king, (45, 45))
    black_rook = pygame.image.load('assets/images/black rook.png')
    black_rook = pygame.transform.scale(black_rook, (65, 65))
    black_rook_small = pygame.transform.scale(black_rook, (45, 45))
    black_bishop = pygame.image.load('assets/images/black bishop.png')
    black_bishop = pygame.transform.scale(black_bishop, (65, 65))
    black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
    black_knight = pygame.image.load('assets/images/black knight.png')
    black_knight = pygame.transform.scale(black_knight, (65, 65))
    black_knight_small = pygame.transform.scale(black_knight, (45, 45))
    black_pawn = pygame.image.load('assets/images/black pawn.png')
    black_pawn = pygame.transform.scale(black_pawn, (50, 50))
    black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
    white_queen = pygame.image.load('assets/images/white queen.png')
    white_queen = pygame.transform.scale(white_queen, (65, 65))
    white_queen_small = pygame.transform.scale(white_queen, (45, 45))
    white_king = pygame.image.load('assets/images/white king.png')
    white_king = pygame.transform.scale(white_king, (65, 65))
    white_king_small = pygame.transform.scale(white_king, (45, 45))
    white_rook = pygame.image.load('assets/images/white rook.png')
    white_rook = pygame.transform.scale(white_rook, (65, 65))
    white_rook_small = pygame.transform.scale(white_rook, (45, 45))
    white_bishop = pygame.image.load('assets/images/white bishop.png')
    white_bishop = pygame.transform.scale(white_bishop, (65, 65))
    white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
    white_knight = pygame.image.load('assets/images/white knight.png')
    white_knight = pygame.transform.scale(white_knight, (65, 65))
    white_knight_small = pygame.transform.scale(white_knight, (45, 45))
    white_pawn = pygame.image.load('assets/images/white pawn.png')
    white_pawn = pygame.transform.scale(white_pawn, (50, 50))
    white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
    white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
    small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                        white_rook_small, white_bishop_small]
    black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
    small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                        black_rook_small, black_bishop_small]
    piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
    #endregion


    white_king_moved = False
    white_rook1_moved = False
    white_rook2_moved = False
    black_king_moved = False
    black_rook1_moved = False
    black_rook2_moved = False



    #region function
    # draw main game board
    def draw_board():
        for column in range(8):
            for row in range(8):
                if (column + row) % 2 == 0:
                    pygame.draw.rect(screen, (255, 228, 205), [280 + (column * 90), row * 90, 90, 90])
                else:
                    pygame.draw.rect(screen, (119, 63, 26), [280 + (column * 90), row * 90, 90, 90])
                pygame.draw.rect(screen, 'light gray', [0, 0, 280, 90])
                pygame.draw.rect(screen, 'black', [0, 0, 280, 90], 5)
                pygame.draw.rect(screen, 'light gray', [0, 630, 280, 90])
                pygame.draw.rect(screen, 'black', [0, 628, 280, 92], 5)
                pygame.draw.rect(screen, 'dark gray', [0, 540, 280, 90])
                pygame.draw.rect(screen, 'black', [0, 540, 280, 93], 5)
                status_text = ['White : ', 'White : ', 'Black : ', 'Black : ']
                screen.blit(font.render(status_text[turn_step] + 'counter', True, 'black'), (60, 35))
                screen.blit(font.render('Forfeit', True, 'black'), (105, 665))

    #draw pieces onto board
    def draw_pieces():
        for i in range(len(white_pieces)):
            index = piece_list.index(white_pieces[i])
            if white_pieces[i] == 'pawn':
                screen.blit(white_pawn, (white_location[i][0] * 90 + 298, white_location[i][1] * 90 + 20))
            else:
                screen.blit(white_images[index], (white_location[i][0] * 90 + 293, white_location[i][1] * 90 + 13))
            if turn_step < 2 :
                if selection == i:
                    pygame.draw.rect(screen, 'black', [white_location[i][0] * 90 + 280, white_location[i][1] * 90, 90, 90], 4)
                
        for i in range(len(black_pieces)):
            index = piece_list.index(black_pieces[i])
            if black_pieces[i] == 'pawn':
                screen.blit(black_pawn, (black_location[i][0] * 90 + 298, black_location[i][1] * 90 + 20))
            else:
                screen.blit(black_images[index], (black_location[i][0] * 90 + 293, black_location[i][1] * 90 + 13))
            if turn_step >= 2:
                if selection == i:
                    pygame.draw.rect(screen, 'black', [black_location[i][0] * 90 + 280, black_location[i][1] * 90, 90, 90], 4)
                    
    # fonction to check pieces
    def check_options(pieces, locations, turn):
        moves_list = []
        all_moves_list = []
        
        for i in range(len(pieces)):
            location = locations[i]
            piece = pieces[i]
            if piece == 'pawn':
                moves_list = check_pawn(location, turn)
            elif piece == 'rook':
                moves_list = check_rook(location, turn)
                for i in roque(i, piece, turn):
                    moves_list.append(i)
            elif piece == 'knight':
                moves_list = check_knight(location, turn)
            elif piece == 'bishop':
                moves_list = check_bishop(location, turn)
            elif piece == 'queen':
                moves_list = check_queen(location, turn)
            elif piece == 'king':
                moves_list = check_king(location, turn)
                for i in roque(i, piece, turn):
                    moves_list.append(i)
            if turn == 'white':
                for i in moves_list:
                    if i in white_location:
                        index = moves_list.index(i)
                        moves_list.pop(index)
            if turn == 'black':
                for i in moves_list:
                    if i in black_location:
                        index = moves_list.index(i)
                        moves_list.pop(index)
            all_moves_list.append(moves_list)
        return all_moves_list

    # function to updates options if check
    def check_options_update():
        white = king_danger_place(black_pieces, black_location, 'black')
        black = king_danger_place(white_pieces, white_location, 'white')
        black_options = check_options(black_pieces, black_location, 'black')
        white_options = check_options(white_pieces, white_location, 'white')
        for i in white:
            if white_king_place in white[i]:
                white_left = check_options_check(i, 'white')
                for a in range(len(white_options)):
                    remove_list = []
                    stay = 0
                    if a == white_pieces.index('king'):
                        pass
                    else:
                        for c in range(len(white_options[a])):
                            stay = 0
                            for b in white_left:
                                if white_options[a][c] == b:
                                    stay += 1
                            if stay == 0:
                                to_remove = white_options[a][c]
                                remove_list.append(to_remove)
                        for d in remove_list:
                            white_options[a].remove(d)
                for i in white_options:
                    if i in white_location:
                        index = white_options.index(i)
                        white_options.pop(index)
                return white_options 
        for i in black:
            if black_king_place in black[i]:
                black_left = check_options_check(i, 'black')
                for a in range(len(black_options)):
                    remove_list = []
                    stay = 0
                    if a == 4:
                        pass
                    else:
                        for c in range(len(black_options[a])):
                            for b in black_left:
                                if black_options[a][c] == b:
                                    stay += 1
                            if stay == 0:
                                pass
                                to_remove = black_options[a][c]
                                remove_list.append(to_remove)
                        for d in remove_list:
                            black_options[a].remove(d)
                for i in black_options:
                    if i in black_location:
                        index = black_options.index(i)
                        black_options.pop(index)
                return black_options

    # function to check moves when king in check
    def check_options_check(location, turn):
        moves_list = []
        all_moves_list = []
        
        if turn == 'white':
            index = black_location.index(location)
            piece = black_pieces[index]
            king = white_king_place
        elif turn == 'black':
            index = white_location.index(location)
            piece = white_pieces[index]
            king = black_king_place
        if piece == 'pawn':
            moves_list = [location]
        elif piece == 'rook':
            moves_list = rook_position_check(location, king)
            moves_list.append(location)
        elif piece == 'knight':
            moves_list = [location]
        elif piece == 'bishop':
            moves_list = bishop_position_check(location, king)
            moves_list.append(location)
        elif piece == 'queen':
            moves_list = queen_position_check(location, king)
            moves_list.append(location)
        for i in moves_list:
            all_moves_list.append(i)
        return all_moves_list

    # funtion to check position for rook if check
    def rook_position_check(location, king):
        moves_list = []
        move = (king[0] - location[0], king[1] - location[1])
        if move[0] != 0:
            if move[0] > 0:
                for i in range(1, move[0]):
                    moves_list.append((location[0]+i, location[1]))
            elif move[0] < 0:
                for i in range(-1, move[0], -1):
                    moves_list.append((location[0]+i, location[1]))
        if move[1] != 0:
            if move[1] > 0:
                for i in range(1, move[1]):
                    moves_list.append((location[1]+i, location[1]))
            elif move[1] < 0:
                for i in range(-1, move[1], -1):
                    moves_list.append((location[1]+i, location[1]))
        return moves_list
                    
    # function to check position for bishop if check
    def bishop_position_check(location, king):
        moves_list = []
        move = (king[0] - location[0], king[1] - location[1])
        if move[0] > 0 and move[1] > 0:
            for i in range(1, move[0]):
                moves_list.append((location[0]+i, location[1]+i))
        elif move[0] < 0 and move[1] > 0:
            for i in range(-1, move[0], -1):
                moves_list.append((location[0]+i, location[1]-i))
        elif move[0] < 0 and move[1] < 0:
            for i in range(1, move[1]):
                moves_list.append((location[1]-i, location[1]-i))
        elif move[0] > 0 and move[1] < 0:
            for i in range(-1, move[1], -1):
                moves_list.append((location[1]-i, location[1]+i))
        return moves_list

    # function to check queen position when check
    def queen_position_check(location, king):
        moves_list = bishop_position_check(location, king)
        second_list = rook_position_check(location, king)
        for i in range(len(second_list)):
            moves_list.append(second_list[i])
        return moves_list

    # fonction to check valid pawn moves
    def check_pawn(position, color):
        moves_list = []
        second = False
        if color == 'white':
            if (position[0], position[1] - 1) not in white_location and \
                    (position[0], position[1] - 1) not in black_location and position[1] > 0:
                moves_list.append((position[0], position[1] - 1))
                second = True
            
            if (position[0], position[1] - 2) not in white_location and \
                    (position[0], position[1] - 2) not in black_location and position[1] == 6 and second == True:
                moves_list.append((position[0], position[1] - 2))
            
            if (position[0] + 1, position[1] - 1) in black_location:
                moves_list.append((position[0] + 1, position[1] - 1))
            
            if (position[0] - 1, position[1] - 1) in black_location:
                moves_list.append((position[0] - 1, position[1] - 1))
        second = False
        if color == 'black':
            if (position[0], position[1] + 1) not in white_location and \
                    (position[0], position[1] + 1) not in black_location and position[1] < 7:
                moves_list.append((position[0], position[1] + 1))
                second = True
            
            if (position[0], position[1] + 2) not in white_location and \
                    (position[0], position[1] + 2) not in black_location and position[1] == 1 and second == True:
                moves_list.append((position[0], position[1] + 2))
            
            if (position[0] + 1, position[1] + 1) in white_location:
                moves_list.append((position[0] + 1, position[1] + 1))
            
            if (position[0] - 1, position[1] + 1) in white_location:
                moves_list.append((position[0] - 1, position[1] + 1))
                
        return moves_list

    # fonction to check valid rook moves
    def check_rook(position, color):
        moves_list = []
        
        if color == 'white':
            i = 1
            while (position[0]+i) <= 7:
                if (position[0]+i, position[1]) in white_location:
                    moves_list.append((position[0]+i, position[1]))
                    break
                if (position[0]+i, position[1]) in black_location:
                    moves_list.append((position[0]+i, position[1]))
                    break
                else:
                    moves_list.append((position[0]+i, position[1]))
                    i += 1
            i = 1
            while (position[0]-i) >= 0:
                if (position[0]-i, position[1]) in white_location:
                    moves_list.append((position[0]-i, position[1]))
                    break
                if (position[0]-i, position[1]) in black_location:
                    moves_list.append((position[0]-i, position[1]))
                    break
                else:
                    moves_list.append((position[0]-i, position[1]))
                    i += 1
            i = 1
            while (position[1]+i) <= 7:
                if (position[0], position[1]+i) in white_location:
                    moves_list.append((position[0], position[1]+i))
                    break
                if (position[0], position[1]+i) in black_location:
                    moves_list.append((position[0], position[1]+i))
                    break
                else:
                    moves_list.append((position[0], position[1]+i))
                    i += 1
            i = 1
            while (position[1]-i) >= 0:
                if (position[0], position[1]-i) in white_location:
                    moves_list.append((position[0], position[1]-i))
                    break
                if (position[0], position[1]-i) in black_location:
                    moves_list.append((position[0], position[1]-i))
                    break
                else:
                    moves_list.append((position[0], position[1]-i))
                    i += 1
            for i in moves_list:
                    if i in white_location:
                        index = moves_list.index(i)
                        moves_list.pop(index)
                        
        elif color == 'black':
            i = 1
            while (position[0]+i) <= 7:
                if (position[0]+i, position[1]) in black_location:
                    moves_list.append((position[0]+i, position[1]))
                    break
                if (position[0]+i, position[1]) in white_location:
                    moves_list.append((position[0]+i, position[1]))
                    break
                else:
                    moves_list.append((position[0]+i, position[1]))
                    i += 1
            i = 1
            while (position[0]-i) >= 0:
                if (position[0]-i, position[1]) in black_location:
                    moves_list.append((position[0]-i, position[1]))
                    break
                if (position[0]-i, position[1]) in white_location:
                    moves_list.append((position[0]-i, position[1]))
                    break
                else:
                    moves_list.append((position[0]-i, position[1]))
                    i += 1
            i = 1
            while (position[1]+i) <= 7:
                if (position[0], position[1]+i) in black_location:
                    moves_list.append((position[0], position[1]+i))
                    break
                if (position[0], position[1]+i) in white_location:
                    moves_list.append((position[0], position[1]+i))
                    break
                else:
                    moves_list.append((position[0], position[1]+i))
                    i += 1
            i = 1
            while (position[1]-i) >= 0:
                if (position[0], position[1]-i) in black_location:
                    moves_list.append((position[0], position[1]-i))
                    break
                if (position[0], position[1]-i) in white_location:
                    moves_list.append((position[0], position[1]-i))
                    break
                else:
                    moves_list.append((position[0], position[1]-i))
                    i += 1
            for i in moves_list:
                    if i in black_location:
                        index = moves_list.index(i)
                        moves_list.pop(index)
        
        return moves_list

    # fontion to check valid knights moves
    def check_knight(position, color):
        moves_list = []
        
        if color == 'white':
            if (position[0]+2) <= 7:
                if (position[1]+1) <= 7:
                    moves_list.append((position[0]+2, position[1]+1))
                if (position[1]-1) >= 0:
                    moves_list.append((position[0]+2, position[1]-1))
            if (position[0]-2) >= 0:
                if (position[1]+1) <= 7:
                    moves_list.append((position[0]-2, position[1]+1))
                if (position[1]-1) >= 0:
                    moves_list.append((position[0]-2, position[1]-1))
            if (position[1]+2) <= 7:
                if (position[0]+1) <= 7:
                    moves_list.append((position[0]+1, position[1]+2))
                if (position[0]-1) >= 0:
                    moves_list.append((position[0]-1, position[1]+2))
            if (position[1]-2) >= 0:
                if (position[0]+1) <= 7:
                    moves_list.append((position[0]+1, position[1]-2))
                if (position[0]-1) >= 0:
                    moves_list.append((position[0]-1, position[1]-2))
        
        elif color == 'black':
            if (position[0]+2) <= 7:
                if (position[1]+1) <= 7:
                    moves_list.append((position[0]+2, position[1]+1))
                if (position[1]-1) >= 0:
                    moves_list.append((position[0]+2, position[1]-1))
            if (position[0]-2) >= 0:
                if (position[1]+1) <= 7:
                    moves_list.append((position[0]-2, position[1]+1))
                if (position[1]-1) >= 0:
                    moves_list.append((position[0]-2, position[1]-1))
            if (position[1]+2) <= 7:
                if (position[0]+1) <= 7:
                    moves_list.append((position[0]+1, position[1]+2))
                if (position[0]-1) >= 0:
                    moves_list.append((position[0]-1, position[1]+2))
            if (position[1]-2) >= 0:
                if (position[0]+1) <= 7:
                    moves_list.append((position[0]+1, position[1]-2))
                if (position[0]-1) >= 0:
                    moves_list.append((position[0]-1, position[1]-2))
        
        return moves_list

    # fonction to check valid bishop moves
    def check_bishop(position, color):
        moves_list = []
        
        if color == 'white':
            i = 1
            while (position[0]+i) <= 7 and (position[1]+i) <= 7:
                if (position[0]+i, position[1] + i) in white_location:
                    moves_list.append((position[0]+i, position[1]+i))
                    break
                if (position[0]+i, position[1]+i) in black_location:
                    moves_list.append((position[0]+i, position[1]+i))
                    break
                else:
                    moves_list.append((position[0]+i, position[1]+i))
                    i += 1
            i = 1
            while (position[0]-i) >= 0 and (position[1]+i) <= 7:
                if (position[0]-i, position[1]+i) in white_location:
                    moves_list.append((position[0]-i, position[1]+i))
                    break
                if (position[0]-i, position[1]+i) in black_location:
                    moves_list.append((position[0]-i, position[1]+i))
                    break
                else:
                    moves_list.append((position[0]-i, position[1]+i))
                    i += 1
            i = 1
            while (position[0]+i) <= 7 and (position[1]-i) >= 0:
                if (position[0]+i, position[1]-i) in white_location:
                    moves_list.append((position[0]+i, position[1]-i))
                    break
                if (position[0]+i, position[1]-i) in black_location:
                    moves_list.append((position[0]+i, position[1]-i))
                    break
                else:
                    moves_list.append((position[0]+i, position[1]-i))
                    i += 1
            i = 1
            while (position[0]-i) >= 0 and (position[1]-i) >= 0:
                if (position[0]-i, position[1]-i) in white_location:
                    moves_list.append((position[0]-i, position[1]-i))
                    break
                if (position[0]-i, position[1]-i) in black_location:
                    moves_list.append((position[0]-i, position[1]-i))
                    break
                else:
                    moves_list.append((position[0]-i, position[1]-i))
                    i += 1
            for i in moves_list:
                if i in white_location:
                    index = moves_list.index(i)
                    moves_list.pop(index)
                        
        elif color == 'black':
            i = 1
            while (position[0]+i) <= 7 and (position[1]+i) <= 7:
                if (position[0]+i, position[1] + i) in black_location:
                    moves_list.append((position[0]+i, position[1]+i))
                    break
                if (position[0]+i, position[1]+i) in white_location:
                    moves_list.append((position[0]+i, position[1]+i))
                    break
                else:
                    moves_list.append((position[0]+i, position[1]+i))
                    i += 1
            i = 1
            while (position[0]-i) >= 0 and (position[1]+i) <= 7:
                if (position[0]-i, position[1]+i) in black_location:
                    moves_list.append((position[0]-i, position[1]+i))
                    break
                if (position[0]-i, position[1]+i) in white_location:
                    moves_list.append((position[0]-i, position[1]+i))
                    break
                else:
                    moves_list.append((position[0]-i, position[1]+i))
                    i += 1
            i = 1
            while (position[0]+i) <= 7 and (position[1]-i) >= 0:
                if (position[0]+i, position[1]-i) in black_location:
                    moves_list.append((position[0]+i, position[1]-i))
                    break
                if (position[0]+i, position[1]-i) in white_location:
                    moves_list.append((position[0]+i, position[1]-i))
                    break
                else:
                    moves_list.append((position[0]+i, position[1]-i))
                    i += 1
            i = 1
            while (position[0]-i) >= 0 and (position[1]-i) >= 0:
                if (position[0]-i, position[1]-i) in black_location:
                    moves_list.append((position[0]-i, position[1]-i))
                    break
                if (position[0]-i, position[1]-i) in white_location:
                    moves_list.append((position[0]-i, position[1]-i))
                    break
                else:
                    moves_list.append((position[0]-i, position[1]-i))
                    i += 1
            for i in moves_list:
                    if i in black_location:
                        index = moves_list.index(i)
                        moves_list.pop(index)
        
        return moves_list

    # fonction to check valid queen moves
    def check_queen(position, color):
        moves_list = check_bishop(position, color)
        second_list = check_rook(position, color)
        for i in range(len(second_list)):
            moves_list.append(second_list[i])
        if color == 'white':
            for i in moves_list:
                    if i in white_location:
                        index = moves_list.index(i)
                        moves_list.pop(index)
        elif color == 'black':
            for i in moves_list:
                    if i in black_location:
                        index = moves_list.index(i)
                        moves_list.pop(index)
        return moves_list

    # fonction to check valid king moves
    def check_king(position, color):
        moves_list = []
        white_danger_turn = king_danger_place(black_pieces, black_location, 'black')
        black_danger_turn = king_danger_place(white_pieces, white_location, 'white')
        
        if color == 'white':
            if (position[0], position[1] - 1) not in white_location and \
                    (position[1]-1) >= 0:
                moves_list.append((position[0], position[1] - 1))
            
            if (position[0], position[1] + 1) not in white_location and \
                    (position[1]+1) <= 7:
                moves_list.append((position[0], position[1] + 1))
            
            if (position[0] - 1, position[1]) not in white_location and \
                    (position[0]-1) >= 0:
                moves_list.append((position[0] - 1, position[1]))
            
            if (position[0] + 1, position[1]) not in white_location and \
                    (position[0]+1) <= 7:
                moves_list.append((position[0] + 1, position[1]))
            
            if (position[0] - 1, position[1] - 1) not in white_location and \
                    (position[1]-1) >= 0 and (position[0]-1) >= 0:
                moves_list.append((position[0] - 1, position[1] - 1))
            
            if (position[0] + 1, position[1] + 1) not in white_location and \
                    (position[1]+1) <= 7 and (position[0]+1) <= 7:
                moves_list.append((position[0] + 1, position[1] + 1))
            
            if (position[0] - 1, position[1] + 1) not in white_location and \
                    (position[0]-1) >= 0 and (position[1]+1) <= 7:
                moves_list.append((position[0] - 1, position[1] + 1))
            
            if (position[0] + 1, position[1] - 1) not in white_location and \
                    (position[0]+1) <= 7  and (position[1]-1) >= 0:
                moves_list.append((position[0] + 1, position[1] - 1))
            for i in white_danger_turn:
                for j in white_danger_turn[i]:
                    if j in moves_list:
                        index = moves_list.index(j)
                        moves_list.pop(index)
                    
        elif color == 'black':
            if (position[0], position[1] - 1) not in black_location and \
                    (position[1]-1) >= 0:
                moves_list.append((position[0], position[1] - 1))
            
            if (position[0], position[1] + 1) not in black_location and \
                    (position[1]+1) <= 7:
                moves_list.append((position[0], position[1] + 1))
            
            if (position[0] - 1, position[1]) not in black_location and \
                    (position[0]-1) >= 0:
                moves_list.append((position[0] - 1, position[1]))
            
            if (position[0] + 1, position[1]) not in black_location and \
                    (position[0]+1) <= 7:
                moves_list.append((position[0] + 1, position[1]))
            
            if (position[0] - 1, position[1] - 1) not in black_location and \
                    (position[1]-1) >= 0 and (position[0]-1) >= 0:
                moves_list.append((position[0] - 1, position[1] - 1))
            
            if (position[0] + 1, position[1] + 1) not in black_location and \
                    (position[1]+1) <= 7 and (position[0]+1) <= 7:
                moves_list.append((position[0] + 1, position[1] + 1))
            
            if (position[0] - 1, position[1] + 1) not in black_location and \
                    (position[0]-1) >= 0 and (position[1]+1) <= 7:
                moves_list.append((position[0] - 1, position[1] + 1))
            
            if (position[0] + 1, position[1] - 1) not in black_location and \
                    (position[0]+1) <= 7  and (position[1]-1) >= 0:
                moves_list.append((position[0] + 1, position[1] - 1))
            for i in black_danger_turn:
                for j in black_danger_turn[i]:
                    if j in moves_list:
                        index = moves_list.index(j)
                        moves_list.pop(index)
        
        return moves_list

    #check options king
    def check_king_options(position, color):
        moves_list = []
        
        if color == 'white':
            if (position[1]-1) >= 0:
                moves_list.append((position[0], position[1] - 1))
            
            if (position[1]+1) <= 7:
                moves_list.append((position[0], position[1] + 1))
            
            if (position[0]-1) >= 0:
                moves_list.append((position[0] - 1, position[1]))
            
            if (position[0]+1) <= 7:
                moves_list.append((position[0] + 1, position[1]))
            
            if (position[1]-1) >= 0 and (position[0]-1) >= 0:
                moves_list.append((position[0] - 1, position[1] - 1))
            
            if (position[1]+1) <= 7 and (position[0]+1) <= 7:
                moves_list.append((position[0] + 1, position[1] + 1))
            
            if (position[0]-1) >= 0 and (position[1]+1) <= 7:
                moves_list.append((position[0] - 1, position[1] + 1))
            
            if (position[0]+1) <= 7  and (position[1]-1) >= 0:
                moves_list.append((position[0] + 1, position[1] - 1))
                    
        elif color == 'black':
            if (position[1]-1) >= 0:
                moves_list.append((position[0], position[1] - 1))
            
            if (position[1]+1) <= 7:
                moves_list.append((position[0], position[1] + 1))
            
            if (position[0]-1) >= 0:
                moves_list.append((position[0] - 1, position[1]))
            
            if (position[0]+1) <= 7:
                moves_list.append((position[0] + 1, position[1]))
            
            if (position[1]-1) >= 0 and (position[0]-1) >= 0:
                moves_list.append((position[0] - 1, position[1] - 1))
            
            if (position[1]+1) <= 7 and (position[0]+1) <= 7:
                moves_list.append((position[0] + 1, position[1] + 1))
            
            if (position[0]-1) >= 0 and (position[1]+1) <= 7:
                moves_list.append((position[0] - 1, position[1] + 1))
            
            if (position[0]+1) <= 7  and (position[1]-1) >= 0:
                moves_list.append((position[0] + 1, position[1] - 1))
        
        return moves_list

    # fonction to check danger pawn
    def danger_pawn(position, color):
        moves_list = []
        
        if color == 'white':
            moves_list.append((position[0] + 1, position[1] - 1))
            moves_list.append((position[0] - 1, position[1] - 1))
        elif color == 'black':
            moves_list.append((position[0] + 1, position[1] + 1))
            moves_list.append((position[0] - 1, position[1] + 1))
        
        return moves_list

    # fonction to for danger place for king
    def king_danger_place(pieces, locations, turn):
        all_danger_place = {}
        danger_place = []
        
        for i in range(len(pieces)):
            location = locations[i]
            piece = pieces[i]
            if piece == 'pawn':
                danger_place = danger_pawn(location, turn)
            elif piece == 'rook':
                danger_place = check_rook(location, turn)
            elif piece == 'knight':
                danger_place = check_knight(location, turn)
            elif piece == 'bishop':
                danger_place = check_bishop(location, turn)
            elif piece == 'queen':
                danger_place = check_queen(location, turn)
            elif piece == 'king':
                danger_place = check_king_options(location, turn)
            all_danger_place[location] = danger_place
        return all_danger_place

    #function to check if list is empty
    def is_empty(list):
        taille_liste = len(list)
        vide = 0
        est_vide = False
        for i in list:
            if i == []:
                vide += 1
        if taille_liste == vide:
            est_vide = True
        return est_vide

    # fonction to check for checks
    def check_for_checks():
        check_white = False
        check_black = False
        white = king_danger_place(black_pieces, black_location, 'black')
        black = king_danger_place(white_pieces, white_location, 'white')
        white_king = check_king(white_king_place, 'white')
        black_king = check_king(black_king_place, 'black')
        white_options_is_empty = is_empty(white_options)
        black_options_is_empty = is_empty(black_options)
        
        for i in white:
            if white_king_place in white[i]:
                screen.blit(font.render('Check white', True, 'black', 'dark grey'), (60, 125))
                if white_options_is_empty == True:
                    screen.blit(font.render('Checkmate white', True, 'black', 'dark grey'), (60, 125))
                    check_white = True
        for i in black:
            if black_king_place in black[i]:
                screen.blit(font.render('Check black', True, 'black', 'dark grey'), (60, 125))
                if black_options_is_empty == True:
                    screen.blit(font.render('Checkmate black', True, 'black', 'dark grey'), (60, 125))
                    check_black = True
        if check_white == True or check_black == True:
            return True
        else:
            return False

    # check for valid moves for just selected piece
    def check_valid_moves():
        if turn_step < 2:
            options_list = white_options
        else:
            options_list = black_options
        valid_options = options_list[selection]
        return valid_options

    # add the roque
    def roque(index, piece, color):
        moves_list = []
        if color == 'white':
            if white_king_moved == False and white_rook1_moved == False:
                if (1, 7) not in white_location and (1, 7) not in black_location and (2, 7) not in white_location and (2, 7) not in black_location and (3, 7) not in white_location and (3, 7) not in black_location: 
                    if piece == 'king':
                        moves_list.append((2, 7))
            if white_king_moved == False and white_rook2_moved == False:
                if (5, 7) not in white_location and (5, 7) not in black_location and (6, 7) not in white_location and (6, 7) not in black_location: 
                    if piece == 'king':
                        moves_list.append((6, 7))
        if color == 'black':
            if black_king_moved == False and black_rook1_moved == False:
                if (1, 0) not in white_location and (1, 0) not in black_location and (2, 0) not in white_location and (2, 0) not in black_location and (3, 0) not in white_location and (3, 0) not in black_location: 
                    if piece == 'king':
                        moves_list.append((2, 0))
            if black_king_moved == False and black_rook2_moved == False:
                if (5, 0) not in white_location and (5, 0) not in black_location and (6, 0) not in white_location and (6, 0) not in black_location: 
                    if piece == 'king':
                        moves_list.append((6, 0))
        return moves_list

    # draw valid moves on screen
    def draw_valid(moves):
        if turn_step < 2:
            color = 'red'
        else:
            color = 'blue'
        for i in range(len(moves)):
            pygame.draw.circle(screen, color, (moves[i][0]*90 + 280 + 45, moves[i][1]*90 + 45), 5)

    def main_menu():
        screen.fill('black')
        pygame.draw.rect(screen, 'light gray', [360, 285, 280, 70], 0, 10)
        screen.blit(button_font.render('Start Game', True, 'black'), (420, 305))
        pygame.draw.rect(screen, 'light gray', [360, 435, 280, 70], 0, 10)
        screen.blit(button_font.render('Quit', True, (240, 48, 48)), (465, 455))
        screen.blit(big_font.render('Welcome to Chess !', True, 'white'), (275, 120))

    def start_game_menu():
        screen.fill('black')
        pygame.draw.rect(screen, 'light gray', [360, 285, 280, 70], 0, 10)
        screen.blit(button_font.render('Two players', True, 'black'), (415, 305))
        pygame.draw.rect(screen, 'light gray', [360, 435, 280, 70], 0, 10)
        screen.blit(button_font.render('One player', True, 'black'), (420, 455))
        screen.blit(big_font.render('Choose the number of players', True, 'white'), (150, 120))

    # Count value for a color
    def color_value(color):
        values = [1, 3, 3, 5, 9, 0]
        pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
        value = 0
        
        if color == 'white':
            for i in white_pieces:
                index = pieces.index(i)
                value += values[index]
        elif color == 'black':
            for i in black_pieces:
                index = pieces.index(i)
                value += values[index]
        
        return value

    # Calculate score
    def score():
        score = 0
        value_white = color_value('white')
        value_black = color_value('black')
        score = value_white - value_black
        return score

    # affiche le score à l'écran
    def afficher_score():
        value = score()
        if value > 0:
            screen.blit(font.render('Score : ' + str(value), True, 'white'), (100, 575))
        elif value < 0:
            screen.blit(font.render('Score : ' + str(value), True, 'black'), (100, 575))
        elif value == 0:
            screen.blit(font.render('Score : ' + str(value), True, 'light grey'), (100, 575))
            
    def afficher_promotion(color):
        if color =='white':
            pygame.draw.rect(screen, 'white', [460, 270, 180, 180], 0, 0)
            pygame.draw.rect(screen, 'black', [460, 270, 93, 93], 5)
            pygame.draw.rect(screen, 'black', [547.5, 270, 93, 93], 5)
            pygame.draw.rect(screen, 'black', [460, 357.5, 93, 93], 5)
            pygame.draw.rect(screen, 'black', [547.5, 357.5, 93, 93], 5)
            screen.blit(button_font.render('Choose promotion', True, 'black', 'dark grey'), (7, 125))
            screen.blit(white_queen, (2 * 90 + 293.5, 3 * 90 + 13))
            screen.blit(white_rook, (3 * 90 + 293.5, 3 * 90 + 13))
            screen.blit(white_bishop, (2 * 90 + 293.5, 4 * 90 + 13))
            screen.blit(white_knight, (3 * 90 + 293.5, 4 * 90 + 13))
        elif color == 'black':
            pygame.draw.rect(screen, 'white', [460, 270, 180, 180], 0, 0)
            pygame.draw.rect(screen, 'black', [460, 270, 93, 93], 5)
            pygame.draw.rect(screen, 'black', [547.5, 270, 93, 93], 5)
            pygame.draw.rect(screen, 'black', [460, 357.5, 93, 93], 5)
            pygame.draw.rect(screen, 'black', [547.5, 357.5, 93, 93], 5)
            screen.blit(button_font.render('Choose promotion', True, 'black', 'dark grey'), (7, 125))
            screen.blit(black_queen, (2 * 90 + 293.5, 3 * 90 + 13))
            screen.blit(black_rook, (3 * 90 + 293.5, 3 * 90 + 13))
            screen.blit(black_bishop, (2 * 90 + 293.5, 4 * 90 + 13))
            screen.blit(black_knight, (3 * 90 + 293.5, 4 * 90 + 13))

    #genere un dictionnaire contenant toute les positions possibles

    #endregion
            

            




    #Main game loop
    white = king_danger_place(black_pieces, black_location, 'black')
    black = king_danger_place(white_pieces, white_location, 'white')
    black_options = check_options(black_pieces, black_location, 'black')
    white_options = check_options(white_pieces, white_location, 'white')
    for i in white:
        if white_king_place in white[i]:
            white_options = check_options_update()
    for i in black:
        if black_king_place in black[i]:
            black_options = check_options_update()

    run = True
    play = False
    game = 0
    one_player = False
    two_players = False
    while run:
        check = False
        main_menu()

        
        if play == True:
            check = check_for_checks()
            if check == False:
                start = time.time()
            elif check == True:
                if  time.time() - start <= WAITING_INTERVAL:
                    pass
                else:
                    play = False
                    white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', "knight", 'rook',
                                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    white_location = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), 
                                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                    black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', "knight", 'rook',
                                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    black_location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), 
                                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                    white = king_danger_place(black_pieces, black_location, 'black')
                    black = king_danger_place(white_pieces, white_location, 'white')
                    black_options = check_options(black_pieces, black_location, 'black')
                    white_options = check_options(white_pieces, white_location, 'white')
                    for i in white:
                        if white_king_place in white[i]:
                            white_options = check_options_update()
                    for i in black:
                        if black_king_place in black[i]:
                            black_options = check_options_update()
            white_king_place = white_location[white_pieces.index('king')]
            black_king_place = black_location[black_pieces.index('king')]
            timer.tick(fps)
            screen.fill('dark gray')
            draw_board()
            draw_pieces()
            check_for_checks()
            afficher_score()
            if selection != 100:
                valid_moves = check_valid_moves()
                draw_valid(valid_moves)
            if white_king_place != (4, 7):
                white_king_moved = True
            if white_pieces[0] != 'rook' or white_location[0] != (0, 7):
                white_rook1_moved = True
            if white_pieces[7] != 'rook' or white_location[7] != (7, 7):
                white_rook2_moved = True
            if black_king_place != (4, 0):
                black_king_moved = True
            if black_pieces[0] != 'rook' or black_location[0] != (0, 0):
                black_rook1_moved = True
            if black_pieces[7] != 'rook' or black_location[7] != (7, 0):
                black_rook2_moved = True
            white_rook_index = []
            index = 0
            for i in white_pieces:
                if i == 'rook':
                    white_rook_index.append(index)
                index += 1
            black_rook_index = []
            index = 0
            for i in black_pieces:
                if i == 'rook':
                    black_rook_index.append(index)
                index += 1
            for i in white_location:
                if i[1] == 0 and white_pieces[white_location.index(i)] == 'pawn':
                    afficher_promotion('white')
            for i in black_location:
                if i[1] == 7 and black_pieces[black_location.index(i)] == 'pawn':
                    afficher_promotion('black')



            #event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    x = int((x - 280)/90)
                    y = int(y/90)
                    click_coord = (x, y)
                    for i in white_location:
                        if i[1] == 0 and white_pieces[white_location.index(i)] == 'pawn':
                            promotion_location = [(2, 3), (3, 3), (2, 4), (3, 4)]
                            promotion_piece = ['queen', 'rook', 'bishop', 'knight']
                            for a in promotion_location:
                                if a == click_coord:
                                    white_pieces[white_location.index(i)] = promotion_piece[promotion_location.index(a)]
                    for i in black_location:
                        if i[1] == 7 and black_pieces[black_location.index(i)] == 'pawn':
                            promotion_location = [(2, 3), (3, 3), (2, 4), (3, 4)]
                            promotion_piece = ['queen', 'rook', 'bishop', 'knight']
                            for a in promotion_location:
                                if a == click_coord:
                                    black_pieces[black_location.index(i)] = promotion_piece[promotion_location.index(a)]
                    if turn_step <= 1:
                        if click_coord in white_location:
                            selection = white_location.index(click_coord)
                            if turn_step == 0:
                                turn_step = 1
                        if click_coord in valid_moves and selection != 100:
                            white_location[selection] = click_coord
                            white_roque = [(2, 7), (6, 7)]
                            black_roque = [(2, 0), (6, 0)]
                            for i in white_roque:
                                if i in white_options[white_pieces.index('king')] and white_king_moved == False:
                                    if click_coord == i:
                                        if i == (2, 7):
                                            white_location[white_rook_index[white_roque.index(i)]] = (3, 7)
                                        if i == (6, 7):
                                            white_location[white_rook_index[white_roque.index(i)]] = (5, 7)
                            for i in black_roque:
                                if i in black_options[black_pieces.index('king')] and black_king_moved == False:
                                    if click_coord == i:
                                        if i == (2, 0):
                                            black_location[black_rook_index[black_roque.index(i)]] = (3, 0)
                                        if i == (6, 0):
                                            black_location[black_rook_index[black_roque.index(i)]] = (5, 0)
                            if click_coord in black_location:
                                black_piece = black_location.index(click_coord)
                                captured_pieces_white.append(black_pieces[black_piece])
                                black_pieces.pop(black_piece)
                                black_location.pop(black_piece)
                            white = king_danger_place(black_pieces, black_location, 'black')
                            black = king_danger_place(white_pieces, white_location, 'white')
                            black_options = check_options(black_pieces, black_location, 'black')
                            white_options = check_options(white_pieces, white_location, 'white')
                            for i in white:
                                if white_king_place in white[i]:
                                    white_options = check_options_update()
                            for i in black:
                                if black_king_place in black[i]:
                                    black_options = check_options_update()
                            turn_step = 2
                            selection = 100
                            valid_moves = []
                    if turn_step >= 2:
                        if click_coord in black_location:
                            selection = black_location.index(click_coord)
                            if turn_step == 2:
                                turn_step = 3
                        if click_coord in valid_moves and selection != 100:
                            black_location[selection] = click_coord
                            white_roque = [(2, 7), (6, 7)]
                            black_roque = [(2, 0), (6, 0)]
                            for i in white_roque:
                                if i in white_options[white_pieces.index('king')] and white_king_moved == False:
                                    if click_coord == i:
                                        if i == (2, 7):
                                            white_location[white_rook_index[white_roque.index(i)]] = (3, 7)
                                        if i == (6, 7):
                                            white_location[white_rook_index[white_roque.index(i)]] = (5, 7)
                            for i in black_roque:
                                if i in black_options[black_pieces.index('king')] and black_king_moved == False:
                                    if click_coord == i:
                                        if i == (2, 0):
                                            black_location[black_rook_index[black_roque.index(i)]] = (3, 0)
                                        if i == (6, 0):
                                            black_location[black_rook_index[black_roque.index(i)]] = (5, 0)
                            if click_coord in white_location:
                                white_piece = white_location.index(click_coord)
                                captured_pieces_black.append(white_pieces[white_piece])
                                white_pieces.pop(white_piece)
                                white_location.pop(white_piece)
                            white = king_danger_place(black_pieces, black_location, 'black')
                            black = king_danger_place(white_pieces, white_location, 'white')
                            black_options = check_options(black_pieces, black_location, 'black')
                            white_options = check_options(white_pieces, white_location, 'white')
                            for i in white:
                                if white_king_place in white[i]:
                                    white_options = check_options_update()
                            for i in black:
                                if black_king_place in black[i]:
                                    black_options = check_options_update()
                            turn_step = 0
                            selection = 100
                            valid_moves = []
                    x, y = pygame.mouse.get_pos()
                    x = int(x/90)
                    y = int(y/90)
                    click_coord = (x, y)
                    forfeit_place = [(0, 7), (1, 7), (2, 7)]
                    if click_coord in forfeit_place:
                        play = False
                        two_players = False
                        white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', "knight", 'rook',
                                        'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                        white_location = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), 
                                        (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                        black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', "knight", 'rook',
                                        'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                        black_location = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), 
                                        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                        white = king_danger_place(black_pieces, black_location, 'black')
                        black = king_danger_place(white_pieces, white_location, 'white')
                        black_options = check_options(black_pieces, black_location, 'black')
                        white_options = check_options(white_pieces, white_location, 'white')
                        for i in white:
                            if white_king_place in white[i]:
                                white_options = check_options_update()
                        for i in black:
                            if black_king_place in black[i]:
                                black_options = check_options_update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if (x >= 360 and x <= 640) and (y >= 285 and y <= 355):
                        two_players = True
                    elif (x >= 360 and x <= 640) and (y >= 435 and y <= 505):
                        one_player = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if (x >= 360 and x <= 640) and (y >= 285 and y <= 355):
                    play = True
                elif (x >= 360 and x <= 640) and (y >= 435 and y <= 505):
                    run = False


        pygame.display.flip()
        await asyncio.sleep(0)
        
    pygame.quit
    exit()

asyncio.run(main())