import pygame

WI = pygame.display.set_mode((1120, 720))
pygame.display.set_caption("Chess!")
sidemenu = pygame.image.load('menu.png')

boardPurple = pygame.image.load('boardpurp.png')
boardGreen = pygame.image.load('boardgreen.png')
boardBrown = pygame.image.load('boardbrown.png')
board_color = 0
d = 0

playing = True

# pieces

b_rook1 = pygame.image.load('pieceBr.png')
b_rook2 = pygame.image.load('pieceBr.png')
b_knight1 = pygame.image.load('pieceBn.png')
b_knight2 = pygame.image.load('pieceBn.png')
b_bishop1 = pygame.image.load('pieceBb.png')
b_bishop2 = pygame.image.load('pieceBb.png')
b_queen = pygame.image.load('pieceBq.png')
b_king = pygame.image.load('pieceBk.png')
b_pawn1 = pygame.image.load('pieceBp.png')
b_pawn2 = pygame.image.load('pieceBp.png')
b_pawn3 = pygame.image.load('pieceBp.png')
b_pawn4 = pygame.image.load('pieceBp.png')
b_pawn5 = pygame.image.load('pieceBp.png')
b_pawn6 = pygame.image.load('pieceBp.png')
b_pawn7 = pygame.image.load('pieceBp.png')
b_pawn8 = pygame.image.load('pieceBp.png')

w_rook1 = pygame.image.load('pieceWr.png')
w_rook2 = pygame.image.load('pieceWr.png')
w_knight1 = pygame.image.load('pieceWn.png')
w_knight2 = pygame.image.load('pieceWn.png')
w_bishop1 = pygame.image.load('pieceWb.png')
w_bishop2 = pygame.image.load('pieceWb.png')
w_queen = pygame.image.load('pieceWq.png')
w_king = pygame.image.load('pieceWk.png')
w_pawn1 = pygame.image.load('pieceWp.png')
w_pawn2 = pygame.image.load('pieceWp.png')
w_pawn3 = pygame.image.load('pieceWp.png')
w_pawn4 = pygame.image.load('pieceWp.png')
w_pawn5 = pygame.image.load('pieceWp.png')
w_pawn6 = pygame.image.load('pieceWp.png')
w_pawn7 = pygame.image.load('pieceWp.png')
w_pawn8 = pygame.image.load('pieceWp.png')

no_piece = 0

pieces = [b_rook1, b_knight1, b_bishop1, b_queen, b_king, b_bishop2, b_knight2, b_rook2, b_pawn1, b_pawn2, b_pawn3, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, no_piece, w_pawn1, w_pawn2, w_pawn3, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8, w_rook1, w_knight1, w_bishop1, w_queen, w_king, w_bishop2, w_knight2, w_rook2]

def movement():
    global d
    if event.type == pygame.MOUSEBUTTONDOWN:
        mx, my = pygame.mouse.get_pos()
        if mx > 0 and mx < 90 and my > 0 and my < 90:
            d = pieces[0]
        if mx > 90 and mx < 180 and my > 0 and my < 90:
            d = pieces[1]
        if mx > 180 and mx < 270 and my > 0 and my < 90:
            d = pieces[2]
        if mx > 270 and mx < 360 and my > 0 and my < 90:
            d = pieces[3]
        if mx > 360 and mx < 450 and my > 0 and my < 90:
            d = pieces[4]
        if mx > 450 and mx < 540 and my > 0 and my < 90:
            d = pieces[5]
        if mx > 540 and mx < 630 and my > 0 and my < 90:
            d = pieces[6]
        if mx > 630 and mx < 720 and my > 0 and my < 90:
            d = pieces[7]
        
        if mx > 0 and mx < 90 and my > 90 and my < 180:
            d = pieces[8]
        if mx > 90 and mx < 180 and my > 90 and my < 180:
            d = pieces[9]
        if mx > 180 and mx < 270 and my > 90 and my < 180:
            d = pieces[10]
        if mx > 270 and mx < 360 and my > 90 and my < 180:
            d = pieces[11]
        if mx > 360 and mx < 450 and my > 90 and my < 180:
            d = pieces[12]
        if mx > 450 and mx < 540 and my > 90 and my < 180:
            d = pieces[13]
        if mx > 540 and mx < 630 and my > 90 and my < 180:
            d = pieces[14]
        if mx > 630 and mx < 720 and my > 90 and my < 180:
            d = pieces[15]
        
        if mx > 0 and mx < 90 and my > 180 and my < 270:
            d = pieces[16]
        if mx > 90 and mx < 180 and my > 180 and my < 270:
            d = pieces[17]
        if mx > 180 and mx < 270 and my > 180 and my < 270:
            d = pieces[18]
        if mx > 270 and mx < 360 and my > 180 and my < 270:
            d = pieces[19]
        if mx > 360 and mx < 450 and my > 180 and my < 270:
            d = pieces[20]
        if mx > 450 and mx < 540 and my > 180 and my < 270:
            d = pieces[21]
        if mx > 540 and mx < 630 and my > 180 and my < 270:
            d = pieces[22]
        if mx > 630 and mx < 720 and my > 180 and my < 270:
            d = pieces[23]

        if mx > 0 and mx < 90 and my > 270 and my < 360:
            d = pieces[24]
        if mx > 90 and mx < 180 and my > 270 and my < 360:
            d = pieces[25]
        if mx > 180 and mx < 270 and my > 270 and my < 360:
            d = pieces[26]
        if mx > 270 and mx < 360 and my > 270 and my < 360:
            d = pieces[27]
        if mx > 360 and mx < 450 and my > 270 and my < 360:
            d = pieces[28]
        if mx > 450 and mx < 540 and my > 270 and my < 360:
            d = pieces[29]
        if mx > 540 and mx < 630 and my > 270 and my < 360:
            d = pieces[30]
        if mx > 630 and mx < 720 and my > 270 and my < 360:
            d = pieces[31]

    if event.type == pygame.MOUSEBUTTONUP:
            d = 0

def drawtable():
    mx, my = pygame.mouse.get_pos()
    #board colors
    if board_color == 0:
        WI.blit(pygame.transform.scale(boardPurple, (720, 720)),(0, 0))
    if board_color == 1:
        WI.blit(pygame.transform.scale(boardGreen, (720, 720)),(0, 0))
    if board_color == 2:
        WI.blit(pygame.transform.scale(boardBrown, (720, 720)),(0, 0))

    WI.blit(sidemenu, (720, 0))
    
    #rendering all the pieces on the board
    if playing == True:
        if pieces[0] != no_piece:
            if d == pieces[0]:
                WI.blit(pieces[0], (mx-64, my-64))
            else:
                WI.blit(pieces[0], (0-19, 0-19))
        if pieces[1] != no_piece:
            if d == pieces[1]:
                WI.blit(pieces[1], (mx-64, my-64))
            else:
                WI.blit(pieces[1], (90-19, 0-19))
        if pieces[2] != no_piece:
            if d == pieces[2]:
                WI.blit(pieces[2], (mx-64, my-64))
            else:
                WI.blit(pieces[2], (180-19, 0-19))
        if pieces[3] != no_piece:
            if d == pieces[3]:
                WI.blit(pieces[3], (mx-64, my-64))
            else:
                WI.blit(pieces[3], (270-19, 0-19))
        if pieces[4] != no_piece:
            if d == pieces[4]:
                WI.blit(pieces[4], (mx-64, my-64))
            else:
                WI.blit(pieces[4], (360-19, 0-19))
        if pieces[5] != no_piece:
            if d == pieces[5]:
                WI.blit(pieces[5], (mx-64, my-64))
            else:
                WI.blit(pieces[5], (450-19, 0-19))
        if pieces[6] != no_piece:
            if d == pieces[6]:
                WI.blit(pieces[6], (mx-64, my-64))
            else:
                WI.blit(pieces[6], (540-19, 0-19))
        if pieces[7] != no_piece:
            if d == pieces[7]:
                WI.blit(pieces[7], (mx-64, my-64))
            else:
                WI.blit(pieces[7], (630-19, 0-19))

        if pieces[8] != no_piece:
            if d == pieces[8]:
                WI.blit(pieces[8], (mx-64, my-64))
            else:
                WI.blit(pieces[8], (0-19, 90-19))
        if pieces[9] != no_piece:
            if d == pieces[9]:
                WI.blit(pieces[9], (mx-64, my-64))
            else:
                WI.blit(pieces[9], (90-19, 90-19))
        if pieces[10] != no_piece:
            if d == pieces[10]:
                WI.blit(d, (mx-64, my-64))
            else:
                WI.blit(pieces[10], (180-19, 90-19))
        if pieces[11] != no_piece:
            if d == pieces[11]:
                WI.blit(d, (mx-64, my-64))
            else:
                WI.blit(pieces[11], (270-19, 90-19))
        if pieces[12] != no_piece:
            if d == pieces[12]:
                WI.blit(d, (mx-64, my-64))
            else:
                WI.blit(pieces[12], (360-19, 90-19))
        if pieces[13] != no_piece:
            if d == pieces[13]:
                WI.blit(d, (mx-64, my-64))
            else:
                WI.blit(pieces[13], (450-19, 90-19))
        if pieces[14] != no_piece:
            if d == pieces[14]:
                WI.blit(d, (mx-64, my-64))
            else:
                WI.blit(pieces[14], (540-19, 90-19))
        if pieces[15] != no_piece:
            if d == pieces[15]:
                WI.blit(d, (mx-64, my-64))
            else:
                WI.blit(pieces[15], (630-19, 90-19))

        if pieces[16] != no_piece:
            WI.blit(pieces[16], (0-19, 180-19))
        if pieces[17] != no_piece:
            WI.blit(pieces[17], (90-19, 180-19))
        if pieces[18] != no_piece:
            WI.blit(pieces[18], (180-19, 180-19))
        if pieces[19] != no_piece:
            WI.blit(pieces[19], (270-19, 180-19))
        if pieces[20] != no_piece:
            WI.blit(pieces[20], (360-19, 180-19))
        if pieces[21] != no_piece:
            WI.blit(pieces[21], (450-19, 180-19))
        if pieces[22] != no_piece:
            WI.blit(pieces[22], (540-19, 180-19))
        if pieces[23] != no_piece:
            WI.blit(pieces[23], (630-19, 180-19))

        if pieces[24] != no_piece:
            WI.blit(pieces[24], (0-19, 270-19))
        if pieces[25] != no_piece:
            WI.blit(pieces[25], (90-19, 270-19))
        if pieces[26] != no_piece:
            WI.blit(pieces[26], (180-19, 270-19))
        if pieces[27] != no_piece:
            WI.blit(pieces[27], (270-19, 270-19))
        if pieces[28] != no_piece:
            WI.blit(pieces[28], (360-19, 270-19))
        if pieces[29] != no_piece:
            WI.blit(pieces[29], (450-19, 270-19))
        if pieces[30] != no_piece:
            WI.blit(pieces[30], (540-19, 270-19))
        if pieces[31] != no_piece:
            WI.blit(pieces[31], (630-19, 270-19))

        if pieces[32] != no_piece:
            WI.blit(pieces[32], (0-19, 360-19))
        if pieces[33] != no_piece:
            WI.blit(pieces[33], (90-19, 360-19))
        if pieces[34] != no_piece:
            WI.blit(pieces[34], (180-19, 360-19))
        if pieces[35] != no_piece:
            WI.blit(pieces[35], (270-19, 360-19))
        if pieces[36] != no_piece:
            WI.blit(pieces[36], (360-19, 360-19))
        if pieces[37] != no_piece:
            WI.blit(pieces[37], (450-19, 360-19))
        if pieces[38] != no_piece:
            WI.blit(pieces[38], (540-19, 360-19))
        if pieces[39] != no_piece:
            WI.blit(pieces[39], (630-19, 360-19))

        if pieces[40] != no_piece:
            WI.blit(pieces[40], (0-19, 450-19))
        if pieces[41] != no_piece:
            WI.blit(pieces[41], (90-19, 450-19))
        if pieces[42] != no_piece:
            WI.blit(pieces[42], (180-19, 450-19))
        if pieces[43] != no_piece:
            WI.blit(pieces[43], (270-19, 450-19))
        if pieces[44] != no_piece:
            WI.blit(pieces[44], (360-19, 450-19))
        if pieces[45] != no_piece:
            WI.blit(pieces[45], (450-19, 450-19))
        if pieces[46] != no_piece:
            WI.blit(pieces[46], (540-19, 450-19))
        if pieces[47] != no_piece:
            WI.blit(pieces[47], (630-19, 450-19))

        if pieces[48] != no_piece:
            WI.blit(pieces[48], (0-19, 540-19))
        if pieces[49] != no_piece:
            WI.blit(pieces[49], (90-19, 540-19))
        if pieces[50] != no_piece:
            WI.blit(pieces[50], (180-19, 540-19))
        if pieces[51] != no_piece:
            WI.blit(pieces[51], (270-19, 540-19))
        if pieces[52] != no_piece:
            WI.blit(pieces[52], (360-19, 540-19))
        if pieces[53] != no_piece:
            WI.blit(pieces[53], (450-19, 540-19))
        if pieces[54] != no_piece:
            WI.blit(pieces[54], (540-19, 540-19))
        if pieces[55] != no_piece:
            WI.blit(pieces[55], (630-19, 540-19))

        if pieces[56] != no_piece:
            WI.blit(pieces[56], (0-19, 630-19))
        if pieces[57] != no_piece:
            WI.blit(pieces[57], (90-19, 630-19))
        if pieces[58] != no_piece:
            WI.blit(pieces[58], (180-19, 630-19))
        if pieces[59] != no_piece:
            WI.blit(pieces[59], (270-19, 630-19))
        if pieces[60] != no_piece:
            WI.blit(pieces[60], (360-19, 630-19))
        if pieces[61] != no_piece:
            WI.blit(pieces[61], (450-19, 630-19))
        if pieces[62] != no_piece:
            WI.blit(pieces[62], (540-19, 630-19))
        if pieces[63] != no_piece:
            WI.blit(pieces[63], (630-19, 630-19))
    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    movement()
    drawtable()
pygame.quit()