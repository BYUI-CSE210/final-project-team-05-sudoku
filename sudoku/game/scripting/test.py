from random import randint, shuffle

class Board_Creation:

    def __init__(self):
        #initialise empty 9 by 9 self._grid
        self._num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.third = 0

        self._finished_grid = []
        self._columns = []
        self._rows = []
        for i in range(0, 9):
            self._columns.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
            self._rows.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    
    def _remover(self, column_group):
        column = column_group
        for i in range(1, 14):
            #Select a random cell that is not already empty
            row = randint(0, 8)
            col = randint((column-1)*3, (column*3)-1)
            while self._columns[col][row] == 0:
                row = randint(0, 8)
                col = randint((column-1)*3, (column*3)-1)
            self._columns[col][row] = 0
            self._rows[row][col] = 0
    
    def _column_one(self, counter = 0):
        loop = 1
        while loop > 0:
            count = counter
            is_good = True
            shuffle(self._num_list)
            for num in self._num_list:
                if num in self._columns[count%3] or num in self._rows[count//3]:
                    is_good = False
                    loop+=1
                    break
                count+=1

            loop -= 1

        if is_good:
            count = counter
            for num in self._num_list:
                self._columns[count%3][count//3] = num
                self._rows[count//3][count%3] = num
                count+=1
        
        if counter < 18:
            self._column_one(counter + 9)
        else: self._remover(1)
    
    def _column_two(self, counter = 0):
        loop = 1
        while loop > 0:
            count = counter
            is_good = True
            shuffle(self._num_list)
            for num in self._num_list:
                if num in self._columns[(count%3)+3] or num in self._rows[count//3]:
                    is_good = False
                    loop+=1
                    break
                count+=1

            loop -= 1

        if is_good:
            count = counter
            for num in self._num_list:
                self._columns[(count%3)+3][count//3] = num
                self._rows[count//3][(count%3)+3] = num
                count+=1

        if counter < 18:
            self._column_two(counter + 9)
        else: self._remover(2)
    
    def _column_three(self, counter = 0):
        loop = 1
        while loop > 0:
            count = counter
            is_good = True
            shuffle(self._num_list)
            for num in self._num_list:
                if num in self._columns[(count%3)+6] or num in self._rows[count//3]:
                    is_good = False
                    loop+=1
                    break
                count+=1

            loop -= 1

        if is_good:
            count = counter
            for num in self._num_list:
                self._columns[(count%3)+6][count//3] = num
                self._rows[count//3][(count%3)+6] = num
                count+=1

        print(self._columns)
        print()
        print(self._rows)

        if counter < 18:
            self._column_three(counter + 9)
        else: self._remover(3)

    def board_state(self):
        print("Starting first!")
        self._column_one()
        print("Starting the second!")
        self._column_two()
        print("Starting the third!")
        self._column_three()
        print("finished!")
        return self._columns

# board = Board_Creation()
# board.board_state()
# print(board._columns)
