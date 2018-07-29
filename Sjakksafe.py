def make_board(x,y):
    board = []
    temp = []
    for i in range(x):
        for j in range(y):
            temp.append('.')
        board.append(temp)
        temp = []
    return (board)

a = make_board(8,8)

def print_board(board):
    print ('-------------------------------------')
    print ('    a   b   c   d   e   f   g   h')
    print ('8 |',board[0][0],'|',board[0][1],'|',board[0][2],'|',board[0][3],'|',board[0][4],'|',board[0][5],'|',board[0][6],'|',board[0][7],'| 8')
    print('7 |',board[1][0],'|',board[1][1],'|',board[1][2],'|',board[1][3],'|',board[1][4],'|',board[1][5],'|',board[1][6],'|',board[1][7],'| 7')
    print('6 |',board[2][0],'|',board[2][1],'|',board[2][2],'|',board[2][3],'|',board[2][4],'|',board[2][5],'|',board[2][6],'|',board[2][7],'| 6')
    print('5 |',board[3][0],'|',board[3][1],'|',board[3][2],'|',board[3][3],'|',board[3][4],'|',board[3][5],'|',board[3][6],'|',board[3][7],'| 5')
    print('4 |',board[4][0],'|',board[4][1],'|',board[4][2],'|',board[4][3],'|',board[4][4],'|',board[4][5],'|',board[4][6],'|',board[4][7],'| 4')
    print('3 |',board[5][0],'|',board[5][1],'|',board[5][2],'|',board[5][3],'|',board[5][4],'|',board[5][5],'|',board[5][6],'|',board[5][7],'| 3')
    print('2 |',board[6][0],'|',board[6][1],'|',board[6][2],'|',board[6][3],'|',board[6][4],'|',board[6][5],'|',board[6][6],'|',board[6][7],'| 2')
    print('1 |',board[7][0],'|',board[7][1],'|',board[7][2],'|',board[7][3],'|',board[7][4],'|',board[7][5],'|',board[7][6],'|',board[7][7],'| 1')
    print('    a   b   c   d   e   f   g   h')
    print('-------------------------------------')

def reset_board(board):
    temp = 0
    for i in range(len(board)):
        board[1][temp] = 'b'
        temp += 1
    board[0][0] = 't'
    board[0][1] = 'h'
    board[0][2] = 'l'
    board[0][3] = 'k'
    board[0][4] = 'd'
    board[0][5] = 'l'
    board[0][6] = 'h'
    board[0][7] = 't'
    temp = 0
    for i in range(len(board)):
        board[6][temp] = 'B'
        temp += 1
    board[7][0] = 'T'
    board[7][1] = 'H'
    board[7][2] = 'L'
    board[7][3] = 'D'
    board[7][4] = 'K'
    board[7][5] = 'L'
    board[7][6] = 'H'
    board[7][7] = 'T'

def convert_coord(x,y):
    listx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    new_x = 0
    for element in listx:
        if element == x:
            new_x = listx.index(element)
            print(new_x)
    new_y = 0
    listy = [8, 7, 6, 5, 4, 3, 2, 1]
    for element in listy:
        if element == y:
            new_y = listy.index(element)
    new_coord = [new_y,new_x]
    return new_coord

def convert_list_coord_back(list):
    listx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    listy = [8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(len(list)):
        list[i][1] = listx[list[i][1]]
        list[i][0] = listy[list[i][0]]
    temp = []
    for i in range(len(list)):
        temp = list[i][0]
        list[i][0] = list[i][1]
        list[i][1] = temp
        temp = []

    return list

def choice_piece(board,x,y):
    new_coord = convert_coord(x,y)
    if board[new_coord[0]][new_coord[1]] == '.':
        return (False)
    else:
        return (board[new_coord[0]][new_coord[1]])



def get_legal_moves(spiller,board,x,y):
    print('halla',board[x][y])
    leg_x = 0
    leg_y = 0
    leg_list = [leg_x,leg_y]
    print(x,y)
    fin_leg_moves = []
    if board[x][y] == 'B':
        leg_list = [[leg_x-1,leg_y]]

    if board[x][y] == 'b':
        leg_list = [[leg_x+1,leg_y]]

    if board[x][y] == 'T':
        leg_list = [[leg_x - 1, leg_y], [leg_x - 2, leg_y], [leg_x - 3, leg_y], [leg_x - 4, leg_y], [leg_x - 5, leg_y],
                    [leg_x - 6, leg_y], [leg_x - 7, leg_y], [leg_x + 1, leg_y], [leg_x + 2, leg_y], [leg_x + 3, leg_y],
                    [leg_x + 4, leg_y], [leg_x + 5, leg_y], [leg_x + 6, leg_y], [leg_x + 7, leg_y], [leg_x, leg_y - 1],
                    [leg_x, leg_y - 2], [leg_x, leg_y - 3], [leg_x, leg_y - 4], [leg_x, leg_y - 5], [leg_x, leg_y - 6],
                    [leg_x, leg_y - 7], [leg_x, leg_y + 1], [leg_x, leg_y + 2], [leg_x, leg_y + 3], [leg_x, leg_y + 4],
                    [leg_x, leg_y + 5], [leg_x, leg_y + 6], [leg_x, leg_y + 7]]


    if board[x][y] == 't':
        leg_list = [[leg_x - 1, leg_y], [leg_x - 2, leg_y], [leg_x - 3, leg_y], [leg_x - 4, leg_y], [leg_x - 5, leg_y],
                    [leg_x - 6, leg_y], [leg_x - 7, leg_y], [leg_x + 1, leg_y], [leg_x + 2, leg_y], [leg_x + 3, leg_y],
                    [leg_x + 4, leg_y], [leg_x + 5, leg_y], [leg_x + 6, leg_y], [leg_x + 7, leg_y], [leg_x, leg_y - 1],
                    [leg_x, leg_y - 2], [leg_x, leg_y - 3], [leg_x, leg_y - 4], [leg_x, leg_y - 5], [leg_x, leg_y - 6],
                    [leg_x, leg_y - 7], [leg_x, leg_y + 1], [leg_x, leg_y + 2], [leg_x, leg_y + 3], [leg_x, leg_y + 4],
                    [leg_x, leg_y + 5], [leg_x, leg_y + 6], [leg_x, leg_y + 7]]

    if board[x][y] == 'L':
        leg_list = [[leg_x - 1, leg_y -1], [leg_x - 2, leg_y - 2], [leg_x - 3, leg_y - 3], [leg_x - 4, leg_y - 4], [leg_x - 5, leg_y - 5],
                    [leg_x - 6, leg_y - 6], [leg_x - 7, leg_y - 7], [leg_x + 1, leg_y + 1], [leg_x + 2, leg_y + 2], [leg_x + 3, leg_y + 3],
                    [leg_x + 4, leg_y + 4], [leg_x + 5, leg_y + 5], [leg_x + 6, leg_y + 6], [leg_x + 7, leg_y + 7], [leg_x + 1, leg_y - 1],
                    [leg_x + 2, leg_y - 2], [leg_x + 3, leg_y - 3], [leg_x + 4, leg_y - 4], [leg_x + 5, leg_y - 5], [leg_x + 6, leg_y - 6],
                    [leg_x + 7, leg_y - 7], [leg_x - 1, leg_y + 1], [leg_x - 2, leg_y + 2], [leg_x - 3, leg_y + 3], [leg_x - 4, leg_y + 4],
                    [leg_x - 5, leg_y + 5], [leg_x - 6, leg_y + 6], [leg_x - 7, leg_y + 7]]

    if board[x][y] == 'l':
        leg_list = [[leg_x - 1, leg_y -1], [leg_x - 2, leg_y - 2], [leg_x - 3, leg_y - 3], [leg_x - 4, leg_y - 4], [leg_x - 5, leg_y - 5],
                    [leg_x - 6, leg_y - 6], [leg_x - 7, leg_y - 7], [leg_x + 1, leg_y + 1], [leg_x + 2, leg_y + 2], [leg_x + 3, leg_y + 3],
                    [leg_x + 4, leg_y + 4], [leg_x + 5, leg_y + 5], [leg_x + 6, leg_y + 6], [leg_x + 7, leg_y + 7], [leg_x + 1, leg_y - 1],
                    [leg_x + 2, leg_y - 2], [leg_x + 3, leg_y - 3], [leg_x + 4, leg_y - 4], [leg_x + 5, leg_y - 5], [leg_x + 6, leg_y - 6],
                    [leg_x + 7, leg_y - 7], [leg_x - 1, leg_y + 1], [leg_x - 2, leg_y + 2], [leg_x - 3, leg_y + 3], [leg_x - 4, leg_y + 4],
                    [leg_x - 5, leg_y + 5], [leg_x - 6, leg_y + 6], [leg_x - 7, leg_y + 7]]

    if board[x][y] == 'H':
        leg_list = [[leg_x + 2, leg_y - 1], [leg_x + 2, leg_y + 1], [leg_x - 2, leg_y - 1], [leg_x - 2, leg_y + 1],
                    [leg_x - 1, leg_y + 2], [leg_x + 1, leg_y + 2], [leg_x - 1, leg_y - 2], [leg_x + 1, leg_y - 2]]

    if board[x][y] == 'h':
        leg_list = [[leg_x + 2, leg_y - 1], [leg_x + 2, leg_y + 1], [leg_x - 2, leg_y - 1], [leg_x - 2, leg_y + 1],
                    [leg_x - 1, leg_y + 2], [leg_x + 1, leg_y + 2], [leg_x - 1, leg_y - 2], [leg_x + 1, leg_y - 2]]

    if board[x][y] == 'd':
        leg_list = [[leg_x - 1, leg_y], [leg_x - 2, leg_y], [leg_x - 3, leg_y], [leg_x - 4, leg_y], [leg_x - 5, leg_y],
                    [leg_x - 6, leg_y], [leg_x - 7, leg_y], [leg_x + 1, leg_y], [leg_x + 2, leg_y], [leg_x + 3, leg_y],
                    [leg_x + 4, leg_y], [leg_x + 5, leg_y], [leg_x + 6, leg_y], [leg_x + 7, leg_y], [leg_x, leg_y - 1],
                    [leg_x, leg_y - 2], [leg_x, leg_y - 3], [leg_x, leg_y - 4], [leg_x, leg_y - 5], [leg_x, leg_y - 6],
                    [leg_x, leg_y - 7], [leg_x, leg_y + 1], [leg_x, leg_y + 2], [leg_x, leg_y + 3], [leg_x, leg_y + 4],
                    [leg_x, leg_y + 5], [leg_x, leg_y + 6], [leg_x, leg_y + 7],[leg_x - 1, leg_y -1], [leg_x - 2, leg_y - 2], [leg_x - 3, leg_y - 3], [leg_x - 4, leg_y - 4], [leg_x - 5, leg_y - 5],
                    [leg_x - 6, leg_y - 6], [leg_x - 7, leg_y - 7], [leg_x + 1, leg_y + 1], [leg_x + 2, leg_y + 2], [leg_x + 3, leg_y + 3],
                    [leg_x + 4, leg_y + 4], [leg_x + 5, leg_y + 5], [leg_x + 6, leg_y + 6], [leg_x + 7, leg_y + 7], [leg_x + 1, leg_y - 1],
                    [leg_x + 2, leg_y - 2], [leg_x + 3, leg_y - 3], [leg_x + 4, leg_y - 4], [leg_x + 5, leg_y - 5], [leg_x + 6, leg_y - 6],
                    [leg_x + 7, leg_y - 7], [leg_x - 1, leg_y + 1], [leg_x - 2, leg_y + 2], [leg_x - 3, leg_y + 3], [leg_x - 4, leg_y + 4],
                    [leg_x - 5, leg_y + 5], [leg_x - 6, leg_y + 6], [leg_x - 7, leg_y + 7]]

    if board[x][y] == 'D':
        leg_list = [[leg_x - 1, leg_y], [leg_x - 2, leg_y], [leg_x - 3, leg_y], [leg_x - 4, leg_y], [leg_x - 5, leg_y],
                    [leg_x - 6, leg_y], [leg_x - 7, leg_y], [leg_x + 1, leg_y], [leg_x + 2, leg_y], [leg_x + 3, leg_y],
                    [leg_x + 4, leg_y], [leg_x + 5, leg_y], [leg_x + 6, leg_y], [leg_x + 7, leg_y], [leg_x, leg_y - 1],
                    [leg_x, leg_y - 2], [leg_x, leg_y - 3], [leg_x, leg_y - 4], [leg_x, leg_y - 5], [leg_x, leg_y - 6],
                    [leg_x, leg_y - 7], [leg_x, leg_y + 1], [leg_x, leg_y + 2], [leg_x, leg_y + 3], [leg_x, leg_y + 4],
                    [leg_x, leg_y + 5], [leg_x, leg_y + 6], [leg_x, leg_y + 7], [leg_x - 1, leg_y - 1],
                    [leg_x - 2, leg_y - 2], [leg_x - 3, leg_y - 3], [leg_x - 4, leg_y - 4], [leg_x - 5, leg_y - 5],
                    [leg_x - 6, leg_y - 6], [leg_x - 7, leg_y - 7], [leg_x + 1, leg_y + 1], [leg_x + 2, leg_y + 2],
                    [leg_x + 3, leg_y + 3],[leg_x + 4, leg_y + 4], [leg_x + 5, leg_y + 5], [leg_x + 6, leg_y + 6], [leg_x + 7, leg_y + 7],
                    [leg_x + 1, leg_y - 1],[leg_x + 2, leg_y - 2], [leg_x + 3, leg_y - 3], [leg_x + 4, leg_y - 4], [leg_x + 5, leg_y - 5],
                    [leg_x + 6, leg_y - 6],[leg_x + 7, leg_y - 7], [leg_x - 1, leg_y + 1], [leg_x - 2, leg_y + 2], [leg_x - 3, leg_y + 3],
                    [leg_x - 4, leg_y + 4],[leg_x - 5, leg_y + 5], [leg_x - 6, leg_y + 6], [leg_x - 7, leg_y + 7]]

    if board[x][y] == 'k':
        leg_list = [[leg_x,leg_y + 1],[leg_x,leg_y - 1],[leg_x + 1,leg_y],[leg_x - 1,leg_y],[leg_x + 1,leg_y + 1],[leg_x - 1,leg_y - 1],[leg_x - 1,leg_y + 1],[leg_x + 1,leg_y - 1]]

    if board[x][y] == 'K':
        leg_list = [[leg_x,leg_y + 1],[leg_x,leg_y - 1],[leg_x + 1,leg_y],[leg_x - 1,leg_y],[leg_x + 1,leg_y + 1],[leg_x - 1,leg_y - 1],[leg_x - 1,leg_y + 1],[leg_x + 1,leg_y - 1]]

    for element in leg_list:
        if x + element[0] > 7:
            #print('feil trekk')
            #print(x + element[0])
            pass
        elif y + element[1] > 7:
            #print('feil trekk')
            #print(y + element[1])
            pass
        elif x + element[0] < 0:
            #print('feil trekk')
            #print(x + element[0])
            pass
        elif y + element[1] < 0:
            #print('feil trekk')
            #print(y + element[1])
            pass
        else:
            #print('riktig trekk')
            fin_leg_moves.append(element)
            #print(fin_leg_moves)

    for i in range(len(fin_leg_moves)):
        fin_leg_moves[i][0] += x
        fin_leg_moves[i][1] += y

    temp = []
    for i in range(len(fin_leg_moves)):
        temp.append(fin_leg_moves[i])

    if spiller == 1:
        #her er tårn spiller 1
        if board[x][y] == 'T':
            try:
                for i in range(7):
                    if board[x-i-1][y] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x-i-count2-1, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x-i-1][y] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x-i-count2-2, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x+i+1][y] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x+i+count2+1, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x+i+1][y] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x+i+count2+2, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y+i+1] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y+i+count2+1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y+i+1] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y+i+count2+2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y-i-1] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y-i-count2-1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y-i-1] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y-i-count2-2])
                            count2 += 1
            except:
                pass

        #her er løperspiller 1
        elif board[x][y] == 'L':
            try:
                for i in range(7):
                    if board[x-i-1][y+i+1] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x-i-count2-1, y+i+count2+1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x-i-1][y+i+1] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x-i-count2-2, y+i+count2+2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x+i+1][y-i-1] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x+i+count2+1, y-i-count2-1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x+i+1][y-i-1] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x+i+count2+2, y-i-count2-2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x+i+1][y+i+1] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x+i+count2+1, y+i+count2+1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x+i+1][y+i+1] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x+i+count2+2, y+i+count2+2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x-i-1][y-i-1] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x-i-count2-1, y-i-count2-1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x-i-1][y-i-1] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x-i-count2-2, y-i-count2-2])
                            count2 += 1
            except:
                pass

        elif board[x][y] == 'D': #Dronning spiller 1
            try:
                for i in range(7):
                    if board[x-i-1][y] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x-i-count2-1, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x-i-1][y] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x-i-count2-2, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x+i+1][y] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x+i+count2+1, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x+i+1][y] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x+i+count2+2, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y+i+1] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y+i+count2+1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y+i+1] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y+i+count2+2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y-i-1] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y-i-count2-1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y-i-1] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y-i-count2-2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x-i-1][y+i+1] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x-i-count2-1, y+i+count2+1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x-i-1][y+i+1] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x-i-count2-2, y+i+count2+2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x+i+1][y-i-1] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x+i+count2+1, y-i-count2-1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x+i+1][y-i-1] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x+i+count2+2, y-i-count2-2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x+i+1][y+i+1] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x+i+count2+1, y+i+count2+1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x+i+1][y+i+1] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x+i+count2+2, y+i+count2+2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x-i-1][y-i-1] in ['T','H','L','D','K','B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x-i-count2-1, y-i-count2-1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x-i-1][y-i-1] in ['t','h','l','d','k','b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x-i-count2-2, y-i-count2-2])
                            count2 += 1
            except:
                pass




        else:
            for i in range(len(temp)):
                if board[temp[i][0]][temp[i][1]] in ['T','H','L','D','K','B']:
                    fin_leg_moves.remove(temp[i])

    if spiller == 2:
        if board[x][y] == 't':
            try:
                for i in range(7):
                    if board[x - i - 1][y] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x - i - count2 - 1, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x - i - 1][y] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x - i - count2 - 2, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x + i + 1][y] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x + i + count2 + 1, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x + i + 1][y] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x + i + count2 + 2, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y + i + 1] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y + i + count2 + 1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y + i + 1] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y + i + count2 + 2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y - i - 1] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y - i - count2 - 1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y - i - 1] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y - i - count2 - 2])
                            count2 += 1
            except:
                pass

        # her er løperspiller 2
        elif board[x][y] == 'l':
            try:
                for i in range(7):
                    if board[x - i - 1][y + i + 1] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x - i - count2 - 1, y + i + count2 + 1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x - i - 1][y + i + 1] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x - i - count2 - 2, y + i + count2 + 2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x + i + 1][y - i - 1] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x + i + count2 + 1, y - i - count2 - 1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x + i + 1][y - i - 1] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x + i + count2 + 2, y - i - count2 - 2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x + i + 1][y + i + 1] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x + i + count2 + 1, y + i + count2 + 1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x + i + 1][y + i + 1] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x + i + count2 + 2, y + i + count2 + 2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x - i - 1][y - i - 1] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x - i - count2 - 1, y - i - count2 - 1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x - i - 1][y - i - 1] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x - i - count2 - 2, y - i - count2 - 2])
                            count2 += 1
            except:
                pass

        elif board[x][y] == 'd':  # Dronning spiller 2
            try:
                for i in range(7):
                    if board[x - i - 1][y] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x - i - count2 - 1, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x - i - 1][y] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x - i - count2 - 2, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x + i + 1][y] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x + i + count2 + 1, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x + i + 1][y] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x + i + count2 + 2, y])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y + i + 1] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y + i + count2 + 1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y + i + 1] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y + i + count2 + 2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y - i - 1] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y - i - count2 - 1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x][y - i - 1] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x, y - i - count2 - 2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x - i - 1][y + i + 1] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x - i - count2 - 1, y + i + count2 + 1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x - i - 1][y + i + 1] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x - i - count2 - 2, y + i + count2 + 2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x + i + 1][y - i - 1] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x + i + count2 + 1, y - i - count2 - 1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x + i + 1][y - i - 1] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x + i + count2 + 2, y - i - count2 - 2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x + i + 1][y + i + 1] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x + i + count2 + 1, y + i + count2 + 1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x + i + 1][y + i + 1] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x + i + count2 + 2, y + i + count2 + 2])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x - i - 1][y - i - 1] in ['t', 'h', 'l', 'd', 'k', 'b']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x - i - count2 - 1, y - i - count2 - 1])
                            count2 += 1
            except:
                pass
            try:
                for i in range(7):
                    if board[x - i - 1][y - i - 1] in ['T', 'H', 'L', 'D', 'K', 'B']:
                        count2 = 0
                        while True:
                            fin_leg_moves.remove([x - i - count2 - 2, y - i - count2 - 2])
                            count2 += 1
            except:
                pass




        else:
            for i in range(len(temp)):
                if board[temp[i][0]][temp[i][1]] in ['t', 'h', 'l', 'd', 'k', 'b']:
                    fin_leg_moves.remove(temp[i])


    return fin_leg_moves

"""
if x + element[0] and y + element[1] < 7 and x + element[0] and y + element[1] > -7:
    print('du kan flytte', x + element[0])
    print (element)
"""

def choose_move(board,list,xnew,ynew,x,y):
    print(xnew,ynew,x,y)
    print ('happy')
    new_coords = convert_coord(xnew,ynew)
    print(new_coords)
    print(board[x][y])
    board[new_coords[0]][new_coords[1]] = board[x][y]
    board[x][y] = '.'
    print_board(board)
    return board


    




def main():
    board = make_board(8,8)
    reset_board(board)
    print('Velkommen til sjakk! her er brettet:')
    print_board(board)
    while True:
        while True:
            print('Spiller 1: hvilken brikke vil du flytte? x, y koordinat')
            x_coord = input()
            y_coord = int(input())


            piece = choice_piece(board,x_coord,y_coord)
            if piece == '.':
                print ('ingen brikke på gitt koordinat')
            elif piece not in ['B','B','B','B','B','B','B','B','T','T','H','H','L','L','K','D']:
                print ('feil brikke')
            else:
                break
            print (piece)

        print ('du vil flytte:',x_coord,y_coord)
        print('dette er lovlige trekk for gitt brikke:')
        new_coords = convert_coord(x_coord,y_coord)
        fin_leg_moves = get_legal_moves(1,board,new_coords[0],new_coords[1])
        print(convert_list_coord_back(fin_leg_moves))
        print('her er lovlige trekk',fin_leg_moves)
        x_coord = input('tast inn koord til valgt posisjon')
        y_coord = int(input())
        while True:
            if [x_coord,y_coord] not in fin_leg_moves:
                print('tast gyldig koord')
                x_coord = input('tast inn koord til valgt posisjon')
                y_coord = int(input())
            else:
                board = choose_move(board,fin_leg_moves,x_coord,y_coord,new_coords[0],new_coords[1])
                break
        print(board)
        while True:
            print('Spiller 2: hvilken brikke vil du flytte? x, y koordinat')
            x_coord = input()
            y_coord = int(input())


            piece = choice_piece(board,x_coord,y_coord)
            if piece == '.':
                print ('ingen brikke på gitt koordinat')
            elif piece not in ['b','b','b','b','b','b','b','b','t','t','h','h','l','l','k','d']:
                print ('feil brikke')
            else:
                break
            print (piece)
        print ('du vil flytte:',x_coord,y_coord)
        print('dette er lovlige trekk for gitt brikke:')
        new_coords = convert_coord(x_coord,y_coord)
        fin_leg_moves = get_legal_moves(2,board,new_coords[0],new_coords[1])
        print(convert_list_coord_back(fin_leg_moves))
        print('her er lovlige trekk',fin_leg_moves)
        x_coord = input('tast inn koord til valgt posisjon')
        y_coord = int(input())
        while True:
            if [x_coord, y_coord] not in fin_leg_moves:
                print('tast gyldig koord')
                x_coord = input('tast inn koord til valgt posisjon')
                y_coord = int(input())
            else:
                board = choose_move(board, fin_leg_moves, x_coord, y_coord, new_coords[0], new_coords[1])
                break
        print(board)




main()


