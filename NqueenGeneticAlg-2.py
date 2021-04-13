import random
from time import *
from time import process_time

list_of_boards = []
attack = 0


class EmptyBoard(object): # Makes an empty board the size of queen x queen
    def __init__(self):
        self.Board = []
        for i in range(Nqueen):
            self.Board.append([0] * Nqueen)


class Board(object):
    def __init__(self):
        self.Board = []


def make_board(size):
    for i in range(size):
        list_of_boards.append(EmptyBoard())


def random_board(board, row, nqueen): # randomize the location of the queens in the board
    for i in range(row):
        rd = random.randrange(0, nqueen)
        board.Board[i][rd] = 1


def check_fittest(board): # check how many queens are attacking each other
    global attack

    for i in board:
        for j in range(len(i.Board)):
            for k in range(len(i.Board[j])):
                queen_attacked(i.Board, j, k)
        i.Board.append(attack)
        attack = 0


def sort_list(board):
    board.sort(key=lambda board: board.Board[Nqueen])


def crossover(board): # Taking 2 parents and crossing their queens placement
    child_list = []
    for i in range(population):
        p1 = random.randrange(1, int(population / 2))
        p2 = random.randrange(1, int(population / 2))
        rd = random.randrange(1, len(board[0].Board) - 1)
        # print(rd)
        child_list.append(Board())
        for j in range(rd):
            child_list[i].Board.append(board[p1].Board[j])
        for j in range(rd, len(board[p2].Board) - 1):
            child_list[i].Board.append(board[p2].Board[j])
    return child_list


def mutation(board): # introducing some mutation to the board so there's a new variable
    random_picker = random.randrange(0, len(board))
    random_col = random.randrange(0, len(board[random_picker].Board) - 1)
    random_row = random.randrange(0, len(board[random_picker].Board) - 1)
    for i in range(len(board[random_picker].Board[random_row])):
        board[random_picker].Board[random_row][i] = 0
    for i in range(len(board[random_picker].Board[random_row])):
        board[random_picker].Board[random_row][random_col] = 1


def queen_attacked(board, row, col): # the actual calculation of checking which queen is attacking which queen
    global attack
    if board[row][col] == 1:
        for i in range(row, -1, -1):
            if board[i][col] == 1 and (i != row):
                attack += 1
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1 and (i != row and j != col):
                attack += 1
        for i, j in zip(range(row, -1, -1), range(col, len(board[col]), 1)):
            if board[i][j] == 1 and (i != row and j != col):
                attack += 1

print("This program is not yet optimized so the bigger the input the longer it takes to calculate")
BxB=input("Enter the amount of queens in the board (min:4) :")
print("number of population ↑ time to process ↓")
print("number of population ↓ time to process ↑")
Pop =input("How many population would you like in 1 generation (min:4) :")
Nqueen=int(BxB)
population=int(Pop)

make_board(population)
for i in range(population):
    random_board(list_of_boards[i], Nqueen, Nqueen)
check_fittest(list_of_boards)
j = 10
sort_list(list_of_boards)
crossover(list_of_boards)
gen = 0
t1_start = process_time()
while j != 0:

    list_of_boards = crossover(list_of_boards)
    check_fittest(list_of_boards)
    for i in list_of_boards:
        if i.Board[Nqueen] == 0:
            sort_list(list_of_boards)
            j = 0
        else:
            mutation(list_of_boards)
            mutation(list_of_boards)
            sort_list(list_of_boards)

    gen += 1
t1_stop = process_time()
print("the visualisation of the chessboard:")
print("-------------------------------------")
for i in range(len(list_of_boards[0].Board)-1):
    print(list_of_boards[0].Board[i])
print("-------------------------------------")
output=[]
for i in range(len(list_of_boards[0].Board)-1):
    for j in range(len(list_of_boards[0].Board[0])):
        if list_of_boards[0].Board[j][i]==1:
            output.append(j+1)
print("The desired output:",output)
print("answer found on generation:", gen)
print("Elapsed time:", t1_stop, t1_start)
if (t1_stop - t1_start) <59.99:
    print("Elapsed time during the whole program in seconds:", t1_stop - t1_start)
elif (t1_stop - t1_start) >=60.00 and (t1_stop - t1_start) < 3599.99:
    res = (t1_stop - t1_start)/60
    print("Elapsed time during the whole program in minutes: {:.2f}".format(res))
else:
    res = (t1_stop - t1_start) / 3600
    print("Elapsed time during the whole program in hours:{:.2f}".format(res))
sleep(10)

