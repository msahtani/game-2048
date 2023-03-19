import os
import random
import numpy as np
import pygame

from db.database import DBConnection

class Game2048:

    def __init__(self, id: int=0):
        self.__old_grid = None
        self.__grid = None
        self.__id = id
        self.__score = 0
        self.__best_score = 0
        self.__mvt_checked = False
        self.__game_over = False
        self.__reached_2048 = False
        self.__init_grid(id)

    def __init_grid(self, id: int):
        db = DBConnection()
        if id == 0:
            self.__grid = np.zeros((4, 4))
            self.__new_number(2)
            self.__score = 0
            self.__best_score = db.get_best_score()
            
        else:
            self.__grid, self.__score, self.__best_score = db.load(id)
            self.won
        db.close()
        
    @property
    def won(self):
        if not self.__reached_2048:
            self.__reached_2048 = np.any(self.__grid == 2048)
            return self.__reached_2048
        else:
            return False
    
    @property
    def score(self):
        return self.__score

    @property
    def id(self):
        return self.__id

    @property
    def largest_tile(self):
        return np.amax(self.__grid)

    @property
    def best_score(self):
        return self.__best_score

    @property
    def encoded(self):
        np.save('tmp', self.__grid)
        with open('tmp.npy', 'rb') as f:
            data = f.read()
        os.remove('tmp.npy')
        return data

    @property
    def game_over(self):
        return self.__game_over

    def save(self):
        db = DBConnection()
        db.save(self)
        if self.__id == 0:
            self.__id = db.get_last_id()
            print('new id:', self.__id)
        db.close()
        print('saved successfully')

    def __iter__(self):
        self.i = 0
        self.j = 0
        return self

    def __next__(self):
        if self.i < 4:
            if self.i < 4:
                res = self.__grid[self.i, self.j]
                self.j += 1
                if(self.j == 4):
                    self.j = 0
                    self.i += 1
                return res
            else:
                raise StopIteration

    def __new_number(self, k: int=1):
        free_pos = list(zip(*np.where(self.__grid == 0)))
        for _ in range(k):
            pos =random.choice(free_pos)
            if np.random.random() > 0.9:
                self.__grid[pos] = 4
            else:
                self.__grid[pos] = 2
        
    def __shift_row(self, i: int):
        m = 0
        for j in range(4):
            if self.__grid[i, j] != 0:
                self.__grid[i, m], self.__grid[i, j] = self.__grid[i, j], self.__grid[i, m]
                m += 1

    def __check_mvt(self):

        for i in range(4):
            for j in range(3):
                if self.__grid[i, j] == self.__grid[i, j+1]:
                    return True
                elif self.__grid[j, i] == self.__grid[j+1, i]:
                    return True
        return False

    def __verify(self):
        for i in range(4):
            self.__shift_row(i)
            for j in range(3):
                if self.__grid[i, j] == self.__grid[i, j+1]:
                    self.__grid[i, j] *= 2
                    self.__grid[i, j+1] = 0
                    self.__score += self.__grid[i, j]
                    self.__best_score = max(self.__score, self.__best_score)

            self.__shift_row(i)

    def __play(self):
        self.__old_grid = np.copy(self.__grid)

        self.__verify()

        # GAME OVER
        if not np.all(self.__grid == self.__old_grid):
            self.__new_number()

        if not(np.any(self.__grid == 0)):
            if self.__check_mvt() and not(self.__mvt_checked):
                self.__mvt_checked = True
                return
            elif not self.__check_mvt():
                self.__game_over = True

            if self.__mvt_checked:
                self.__game_over = True
        else:
            self.__mvt_checked = False
            
    def make_move(self, key):
        if key == pygame.K_LEFT:
            self.__play()
        if key == pygame.K_UP:
            self.__grid = np.transpose(self.__grid)
            self.__play()
            self.__grid = np.transpose(self.__grid)
        if key == pygame.K_RIGHT:
            self.__grid = self.__grid[:, ::-1]
            self.__play()
            self.__grid = self.__grid[:, ::-1]
        if key == pygame.K_DOWN:
            self.__grid = np.transpose(self.__grid)
            self.__grid = self.__grid[:, ::-1]
            self.__play()
            self.__grid = self.__grid[:, ::-1]
            self.__grid = np.transpose(self.__grid)