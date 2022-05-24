import random
import numpy as np
import pygame

class Game2048:

    def __init__(self,):
       
        self.__mat = np.zeros((4, 4))
        self.new_number(2)

        self.make_move = {
            pygame.K_LEFT: self.__toLeft,
            pygame.K_RIGHT: self.__toRight,
            pygame.K_UP: self.__toUp,
            pygame.K_DOWN: self.__toDown
        }
        

    def __iter__(self):
        self.i = 0
        self.j = 0
        return self

    def __next__(self):
        if self.i < 4:
            if self.i < 4:
                res = self.__mat[self.i, self.j]
                self.j += 1
                if(self.j == 4):
                    self.j = 0
                    self.i += 1
                return res
            else:
                raise StopIteration

    def new_number(self, k=1):
        free_pos = list(zip(*np.where(self.__mat == 0)))
        for _ in range(k):
            pos =random.choice(free_pos)
            if np.random.random() > 0.9:
                self.__mat[pos] = 4
            else:
                self.__mat[pos] = 2

    def __str__(self):
        return str(self.__mat)

    def available_moves(self):
        mat = self.__mat
        for i in range(4):
            for j in range(3):
                if mat[i,j] == mat[i, j+1] and mat[i, j] != 0:
                    return True
        for i in range(4):
            for j in range(3):
                if mat[j,i] == mat[j+1, i] and mat[i, j] != 0:
                    return True
        return False
        
    def shift_row(self, i):
        m = 0
        for j in range(4):
            if self.__mat[i, j] != 0:
                self.__mat[i, m], self.__mat[i, j] = self.__mat[i, j], self.__mat[i, m]
                m += 1

    def __toLeft(self):
        mat = self.__mat
        for i in range(4):
            self.shift_row(i)
            for j in range(3):
                if mat[i, j] == mat[i, j+1]:
                    mat[i, j] *= 2
                    mat[i, j+1] = 0
            
            self.shift_row(i)
        self.new_number()

    def __toRight(self):
        self.__mat = self.__mat[:, ::-1]
        self.__toLeft()
        self.__mat = self.__mat[:, ::-1]

    def __toUp(self):
        self.__mat = np.transpose(self.__mat)
        self.__toLeft()
        self.__mat = np.transpose(self.__mat)
        
    def __toDown(self):
        self.__mat = np.transpose(self.__mat)
        self.__toRight()
        self.__mat = np.transpose(self.__mat)