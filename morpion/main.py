import asyncio
import pygame
import random
import time
import threading

pygame.init()



SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

icon = pygame.image.load('assets/icon-morpion.png').convert_alpha()
pygame.display.set_icon(icon)

square_height = screen.get_height()/3
square_width = screen.get_width()/3

async def main():
    grille = pygame.image.load('assets/grille.jpg').convert()
    size_grille = pygame.transform.scale(grille, (SCREEN_WIDTH, SCREEN_HEIGHT))
    cercle = pygame.image.load('assets/cercle.png').convert_alpha()
    size_cercle = pygame.transform.scale(cercle, (square_width - 10, square_height - 10))
    croix = pygame.load('assets/croix.png').convert_alpha()
    size_croix = pygame.transform.scale(croix, (square_width - 10, square_height - 10))

    square1 = pygame.Rect(0, 0, square_width, square_height)
    square2 = pygame.Rect(square_width, 0, square_width, square_height)
    square3 = pygame.Rect(2*square_width, 0, square_width, square_height)
    square4 = pygame.Rect(0, square_height, square_width, square_height)
    square5 = pygame.Rect(square_width, square_height, square_width, square_height)
    square6 = pygame.Rect(2*square_width, square_height, square_width, square_height)
    square7 = pygame.Rect(0, 2*square_height, square_width, square_height)
    square8 = pygame.Rect(square_width, 2*square_height, square_width, square_height)
    square9 = pygame.Rect(2*square_width, 2*square_height, square_width, square_height)

    sub1 = screen.subsurface(square1)
    sub2 = screen.subsurface(square2)
    sub3 = screen.subsurface(square3)
    sub4 = screen.subsurface(square4)
    sub5 = screen.subsurface(square5)
    sub6 = screen.subsurface(square6)
    sub7 = screen.subsurface(square7)
    sub8 = screen.subsurface(square8)
    sub9 = screen.subsurface(square9)

    screen.blit(size_grille, (0, 0))
    pygame.display.update()

    Liste = [sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9]

    case1 = ''
    case2 = ''
    case3 = ''
    case4 = ''
    case5 = ''
    case6 = ''
    case7 = ''
    case8 = ''
    case9 = ''

    winp = False
    wini = False
    turn = 0

    player_turn = True
    player1_win = 0
    player2_win = 0
    playing = False
    egalite = 0

    def init():
        screen.fill("black")
        font=pygame.font.Font(None, 24)
        text = font.render("Joueur 1 : " + str(player1_win), 1, (255,255,255))
        color = ("blue")
        square = pygame.draw.rect(screen, color, pygame.Rect(30, 10, 120, 30),  0, 3)
        text_rect = text.get_rect(center = square.center)
        screen.blit(text, text_rect)
        
        texte = font.render("Joueur 2 : " + str(player2_win), 1, (255,255,255))
        couleur = ("red")
        carré = pygame.draw.rect(screen, couleur, pygame.Rect(160, 10, 120, 30),  0, 3)
        texte_rect = texte.get_rect(center = carré.center)
        screen.blit(texte, texte_rect)
        pygame.display.flip()

    def start():
        screen.blit(size_grille, (0, 0))
        pygame.display.update()

    run = True
    while run:
        
        font=pygame.font.Font(None, 24)
        text = font.render("Joueur 1 : " + str(player1_win), 1, (255,255,255))
        color = ("blue")
        square = pygame.draw.rect(screen, color, pygame.Rect(40, 10, 120, 30),  0, 3)
        text_rect = text.get_rect(center = square.center)
        screen.blit(text, text_rect)
        
        egalité = font.render("Egalité : " + str(egalite), 1, (255,255,255))
        colora = ("green")
        cube = pygame.draw.rect(screen, colora, pygame.Rect(240, 10, 120, 30),  0, 3)
        egalite_rect = egalité.get_rect(center = cube.center)
        screen.blit(egalité, egalite_rect)
        
        texte = font.render("Joueur 2 : " + str(player2_win), 1, (255,255,255))
        couleur = ("red")
        carré = pygame.draw.rect(screen, couleur, pygame.Rect(440, 10, 120, 30),  0, 3)
        texte_rect = texte.get_rect(center = carré.center)
        screen.blit(texte, texte_rect)
        pygame.display.flip()
        
        for event in pygame.event.get():
                            
            if event.type == pygame.QUIT:
                run = False
            
            if player_turn:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if square1.collidepoint(pos):
                        if sub1 in Liste:
                            sub1.blit(size_croix, (5, 5))
                            case1 = 'p'
                            player_turn = False
                            Liste.remove(sub1)
                            turn += 1
                    elif square2.collidepoint(pos):
                        if sub2 in Liste:
                            sub2.blit(size_croix, (5, 5))
                            case2 = 'p'
                            player_turn = False
                            Liste.remove(sub2)
                            turn += 1
                    elif square3.collidepoint(pos):
                        if sub3 in Liste:
                            sub3.blit(size_croix, (5, 5))
                            case3 = 'p'
                            player_turn = False
                            Liste.remove(sub3)
                            turn += 1
                    elif square4.collidepoint(pos):
                        if sub4 in Liste:
                            sub4.blit(size_croix, (5, 5))
                            case4 = 'p'
                            player_turn = False
                            Liste.remove(sub4)
                            turn += 1
                    elif square5.collidepoint(pos):
                        if sub5 in Liste:
                            sub5.blit(size_croix, (5, 5))
                            case5 = 'p'
                            player_turn = False
                            Liste.remove(sub5)
                            turn += 1
                    elif square6.collidepoint(pos):
                        if sub6 in Liste:
                            sub6.blit(size_croix, (5, 5))
                            case6 = 'p'
                            player_turn = False
                            Liste.remove(sub6)
                            turn += 1
                    elif square7.collidepoint(pos):
                        if sub7 in Liste:
                            sub7.blit(size_croix, (5, 5))
                            case7 = 'p'
                            player_turn = False
                            Liste.remove(sub7)
                            turn += 1
                    elif square8.collidepoint(pos):
                        if sub8 in Liste:
                            sub8.blit(size_croix, (5, 5))
                            case8 = 'p'
                            player_turn = False
                            Liste.remove(sub8)
                            turn += 1
                    elif square9.collidepoint(pos):
                        if sub9 in Liste:
                            sub9.blit(size_croix, (5, 5))
                            case9 = 'p'
                            player_turn = False
                            Liste.remove(sub9)
                            turn += 1  
                if case1 == 'p' and case4 == 'p' and case7 == 'p':
                    winp = True
                if case2 == 'p' and case5 == 'p' and case8 == 'p':
                    winp = True
                if case3 == 'p' and case6 == 'p' and case9 == 'p':
                    winp = True
                if case1 == 'p' and case2 == 'p' and case3 == 'p':
                    winp = True
                if case4 == 'p' and case5 == 'p' and case6 == 'p':
                    winp = True
                if case7 == 'p' and case8 == 'p' and case9 == 'p':
                    winp = True
                if case1 == 'p' and case5 == 'p' and case9 == 'p':
                    winp = True
                if case3 == 'p' and case5 == 'p' and case7 == 'p':
                    winp = True
            
            if player_turn == False:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if square1.collidepoint(pos):
                        if sub1 in Liste:
                            sub1.blit(size_cercle, (5, 5))
                            case1 = 'i'
                            player_turn = True
                            Liste.remove(sub1)
                            turn += 1
                    elif square2.collidepoint(pos):
                        if sub2 in Liste:
                            sub2.blit(size_cercle, (5, 5))
                            case2 = 'i'
                            player_turn = True
                            Liste.remove(sub2)
                            turn += 1
                    elif square3.collidepoint(pos):
                        if sub3 in Liste:
                            sub3.blit(size_cercle, (5, 5))
                            case3 = 'i'
                            player_turn = True
                            Liste.remove(sub3)
                            turn += 1
                    elif square4.collidepoint(pos):
                        if sub4 in Liste:
                            sub4.blit(size_cercle, (5, 5))
                            case4 = 'i'
                            player_turn = True
                            Liste.remove(sub4)
                            turn += 1
                    elif square5.collidepoint(pos):
                        if sub5 in Liste:
                            sub5.blit(size_cercle, (5, 5))
                            case5 = 'i'
                            player_turn = True
                            Liste.remove(sub5)
                            turn += 1
                    elif square6.collidepoint(pos):
                        if sub6 in Liste:
                            sub6.blit(size_cercle, (5, 5))
                            case6 = 'i'
                            player_turn = True
                            Liste.remove(sub6)
                            turn += 1
                    elif square7.collidepoint(pos):
                        if sub7 in Liste:
                            sub7.blit(size_cercle, (5, 5))
                            case7 = 'i'
                            player_turn = True
                            Liste.remove(sub7)
                            turn += 1
                    elif square8.collidepoint(pos):
                        if sub8 in Liste:
                            sub8.blit(size_cercle, (5, 5))
                            case8 = 'i'
                            player_turn = True
                            Liste.remove(sub8)
                            turn += 1
                    elif square9.collidepoint(pos):
                        if sub9 in Liste:
                            sub9.blit(size_cercle, (5, 5))
                            case9 = 'i'
                            player_turn = True
                            Liste.remove(sub9)
                            turn += 1  
                if case1 == 'i' and case4 == 'i' and case7 == 'i':
                    wini = True
                if case2 == 'i' and case5 == 'i' and case8 == 'i':
                    wini = True
                if case3 == 'i' and case6 == 'i' and case9 == 'i':
                    wini = True
                if case1 == 'i' and case2 == 'i' and case3 == 'i':
                    wini = True
                if case4 == 'i' and case5 == 'i' and case6 == 'i':
                    wini = True
                if case7 == 'i' and case8 == 'i' and case9 == 'i':
                    wini = True
                if case1 == 'i' and case5 == 'i' and case9 == 'i':
                    wini = True
                if case3 == 'i' and case5 == 'i' and case7 == 'i':
                    wini = True
            
            if winp:
                player1_win += 1
                S = threading.Timer(0.1, start)  
                S.start()
                Liste = [sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9]

                case1 = ''
                case2 = ''
                case3 = ''
                case4 = ''
                case5 = ''
                case6 = ''
                case7 = ''
                case8 = ''
                case9 = ''

                winp = False
                wini = False
                turn = 0
                player_turn = True
                
            if wini:
                player2_win += 1
                S = threading.Timer(0.1, start)  
                S.start()
                Liste = [sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9]

                case1 = ''
                case2 = ''
                case3 = ''
                case4 = ''
                case5 = ''
                case6 = ''
                case7 = ''
                case8 = ''
                case9 = ''

                winp = False
                wini = False
                turn = 0
                player_turn = True
                
            if turn == 9:
                egalite += 1
                S = threading.Timer(0.1, start)  
                S.start()
                Liste = [sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9]

                case1 = ''
                case2 = ''
                case3 = ''
                case4 = ''
                case5 = ''
                case6 = ''
                case7 = ''
                case8 = ''
                case9 = ''

                winp = False
                wini = False
                turn = 0
                player_turn = True
        
        
        pygame.display.flip()
        await asyncio.sleep(0)
        
    pygame.quit
    exit()
    
asyncio.run(main())