import pygame
import json

class Leaderboard:
    def __init__(self):
        file = open("Tetris/data.json", "r")
        self.leaderboard_json = dict(sorted(json.loads(file.read()).items(), key=lambda item: item[1], reverse=True))
        self.high_score = self.leaderboard_json[max(self.leaderboard_json, key=self.leaderboard_json.get)]
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        file.close()
        
    def draw(self, screen):
        self.leaderboard_json = dict(sorted(self.leaderboard_json.items(), key=lambda item: item[1], reverse=True))
        counter = 0
        offset_y = 30
        while(True):
            if(counter == 0):
                for key, value in self.leaderboard_json.items():
                    text_surface = self.font.render(f'{key}: {value}', False, (0, 0, 0))
                    screen.blit(text_surface, (350, 250 + offset_y * counter))
                    counter += 1
                    if counter > 10:
                        break
            if(counter <= 10):
                text_surface = self.font.render('...: ...', False, (0, 0, 0))
                screen.blit(text_surface, (350, 250 + offset_y * counter))
                counter += 1
            else:
                break
            
    def update(self, leaderboard):
        file = open("Tetris/data.json", "w")
        file.write(json.dumps(leaderboard))
        file.close()
        self.high_score = self.leaderboard_json[max(self.leaderboard_json, key=self.leaderboard_json.get)]