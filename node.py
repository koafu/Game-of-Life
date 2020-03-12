import pygame
import random

class Node():
    
    def __init__(self, x, y, node_width, node_height, cols, rows):
        self.alive = False
        
        self.cols = cols
        self.rows = rows

        self.x = x
        self.y = y
        self.node_width = node_width
        self.node_height = node_height
        
        self.color = (0,0,0)

        if random.uniform(0,1) < 0.2:
            self.alive = True
    
    def __repr__(self):
        return "Node({}; {})".format(self.x, self.y)

    def show(self, screen):
        if self.alive:
            screen.fill(self.color, rect=[(self.x * self.node_width) + 1, (self.y * self.node_height) + 1,
                self.node_width - 1, self.node_height - 1])

    def check_neighbours(self, grid):
        self.live_cells = []

        if self.x < self.cols - 1:
            if grid[self.x + 1][self.y].alive:
                self.live_cells.append(grid[self.x + 1][self.y])
        if self.x > 0:
            if grid[self.x - 1][self.y].alive:
                self.live_cells.append(grid[self.x - 1][self.y])
        if self.y < self.rows - 1:
            if grid[self.x][self.y + 1].alive:
                self.live_cells.append(grid[self.x][self.y + 1])
        if self.y > 0:
            if grid[self.x][self.y - 1].alive:
                self.live_cells.append(grid[self.x][self.y - 1])

        if self.x < self.cols - 1 and self.y > 0:
            if grid[self.x + 1][self.y - 1].alive:
                self.live_cells.append(grid[self.x + 1][self.y - 1])
        if self.x < self.cols - 1 and self.y < self.rows - 1:
            if grid[self.x + 1][self.y + 1].alive:
                self.live_cells.append(grid[self.x + 1][self.y + 1])
        if self.x > 0 and self.y > 0:
            if grid[self.x - 1][self.y - 1].alive:
                self.live_cells.append(grid[self.x - 1][self.y - 1])
        if self.x > 0 and self.y < self.rows - 1:
            if grid[self.x - 1][self.y + 1].alive:
                self.live_cells.append(grid[self.x - 1][self.y + 1])
