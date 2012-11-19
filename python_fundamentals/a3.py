'''A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
'''


def is_valid_word(wordlist, word):
    ''' (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    '''
    for i in wordlist:
        if word == i:
            return True
    return False    


def make_str_from_row(board, row_index):
    ''' (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    '''
    word = ''
    for i in board[row_index] :
        word += i
    return word
        


def make_str_from_column(board, column_index):
    ''' (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    '''
    word = ''
    for i in board:
        word += i[column_index]
    return word


def board_contains_word_in_row(board, word):
    
   
    for i in range(len(board)):
       if make_str_from_row(board,i) == word:
           return True
    return False

    
   
def board_contains_word_in_column(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    '''
    for i in range(len(board[0])):
        if make_str_from_column(board,i) == word:
            return True
    return False


def board_contains_word(board, word):
    '''(list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    '''
    if board_contains_word_in_row(board, word) or board_contains_word_in_column(board, word):
        return True
    return False

def word_score(word):
    '''(str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character in word
                 7-9: 2 points per character in word
                 10+: 3 points per character in word

    >>> word_score('DRUDGERY')
    16
    '''
    k=len(word)
    if k < 3:
        return 0
    elif k>=3 and k<=6:
        return k
    elif k>=7 and k<=9:
        return k*2
    else:
        return k*3
    


def update_score(player_info, word):
    '''([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    '''
    return player_info[1]+word_score(word)

def num_words_on_board(board, words):
    '''(list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    '''
    count = 0
    for i in words:
        if board_contains_word(board,i):
            count += 1
    return count

def read_words(words_file):
    ''' (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    '''
    f = open("wordlist.txt",'r')
    board = []
    lines = f.readlines()
    for i in lines:
        line = i.strip('\n')
        board.append(line)
    f.close()
    
    return board
    

    


def read_board(board_file):
    ''' (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    '''
    f = open('board.txt','r')
    board1 = []
    lines = f.readlines()
    for i in lines:
        line = i.strip('\n')
        board1.append(line)
    f.close()

    board = []
    for j in range(len(board1)):
        temp = []
        for i in range(len(board1[j])):
            temp.append(board1[j][i])
            board.append(temp)

    return board
