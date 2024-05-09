import random
import pygame
import json

from grid import Grid
from blocks import *
from leaderboard import Leaderboard
from textbox import TextInputBox

pygame.font.init()

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.game_over = False
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.score = 0
        self.leaderboard = Leaderboard().leaderboard_json
        self.current_player = Leaderboard().current_player
        self.high_score = Leaderboard().high_score
        self.next_block = self.get_random_block()
        
    def reset(self):
        self.grid.reset()
        self.high_score_update()
        file = open('Tetris/data.json', 'r')
        self.high_score = Leaderboard().high_score
        self.score = 0
        file.close()
    
    def high_score_update(self):
        if self.current_player not in self.leaderboard:
            self.leaderboard[self.current_player] = self.score
        else:
            if self.score > self.leaderboard[self.current_player]:
                self.leaderboard[self.current_player] = self.score
        Leaderboard().update(self.leaderboard)
        self.leaderboard = Leaderboard().leaderboard_json
        
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
            self.next_block.draw(screen, 270, 200)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 285, 190)
        elif self.next_block.id == 8:
            self.next_block.draw(screen, 300, 205)
        else:
            self.next_block.draw(screen, 285, 180)
        self.draw_score(screen)
        self.high_score_update()
        Leaderboard().draw(screen)
    
    def draw_score(self, screen):
        text_surface = self.font.render("Player: " + self.current_player, False, (0, 0, 0))
        screen.blit(text_surface, (325,10))
        text_surface = self.font.render("High Score: " + str(self.high_score), False, (0, 0, 0))
        screen.blit(text_surface, (325,65))
        text_surface = self.font.render("Score: " + str(self.score), False, (0, 0, 0))
        screen.blit(text_surface, (325,90))
        
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
            self.high_score_update()
            
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
    
    def get_nickname(self, screen):
        text_input_box = TextInputBox(50, 50, 400, self.font)
        group = pygame.sprite.Group(text_input_box)
        
        run = True
        while run:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        run = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                        
            text = text_input_box.text
            group.update(event_list)

            screen.fill(0)
            group.draw(screen)
            pygame.display.flip()
        
        self.current_player = text