import random
import pygame
import json

from grid import Grid
from blocks import *

pygame.font.init()

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.game_over = False
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.score = 0
        self.high_score = json.loads(open('Tetris/data.json', 'r').read())
        self.next_block = self.get_random_block()
        
    def reset(self):
        self.grid.reset()
        self.high_score_update()
        file = open('Tetris/data.json', 'r')
        self.high_score = json.loads(file.read())
        self.score = 0
        file.close()
    
    def high_score_update(self):
        if self.score >= self.high_score:
            file = open('Tetris/data.json', 'w')
            file.write(json.dumps(self.score))
            file.close()
        
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock(), AngelBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 0, 0)
        
        if self.next_block.id == 3:
            self.next_block.draw(screen, 270, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 285, 280)
        elif self.next_block.id == 8:
            self.next_block.draw(screen, 300, 295)
        else:
            self.next_block.draw(screen, 285, 270)
        self.draw_score(screen)
    
    def draw_score(self, screen):
        text_surface = self.font.render("Score: " + str(self.score), False, (0, 0, 0))
        screen.blit(text_surface, (325,100))
        text_surface = self.font.render("High Score: " + str(self.high_score), False, (0, 0, 0))
        screen.blit(text_surface, (325,75))
        
    # def draw_next_block(self):
        
    
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)
        
    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)
            
    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()
        
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        
        completed = self.grid.clear_full_rows(self.current_block)
        if completed > 0:
            self.score += completed
        if self.score > self.high_score:
            self.high_score = self.score
            
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        if self.block_fits() == False:
            self.game_over = True
        
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True
        
        
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
        
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    # def draw_rect_for_score_and_block(self):
        