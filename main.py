import pygame
import time
from node import Node

class Simulation():

    def __init__(self):
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False

        self.cols = 80
        self.rows = int(self.height / self.width * self.cols)
        self.node_width = self.width / self.cols
        self.node_height = self.height / self.rows
        self.grid = [[] for n in range(self.cols)]

        for x in range(self.cols):
            for y in range(self.rows):
                self.grid[x].append(Node(x,y,self.node_width, self.node_height, self.cols, self.rows))

    def update_grid(self):
        x, y = 0, 0

        for cols in self.grid:
            pygame.draw.line(self.screen, (0,0,0), (x,0), (x,self.height), 1)
            for rows in cols:
                pygame.draw.line(self.screen, (0,0,0), (0,y), (self.width, y), 1)
            x += self.node_width
            y += self.node_height

        for cols in self.grid:
            for node in cols:
                node.show(self.screen)

    def next_generation(self):
        for cols in self.grid:
            for node in cols:
                node.check_neighbours(self.grid)

        for cols in self.grid:
            for node in cols:
                if node.alive:
                    if len(node.live_cells) < 2 or len(node.live_cells) > 3:
                        node.alive = False
                else:
                    if len(node.live_cells) == 3:
                        node.alive = True

    def run(self):

        while not self.exit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            self.screen.fill((255,255,255))

            #time.sleep(0.05)

            self.next_generation()
            self.update_grid()

            pygame.display.flip()
            self.clock.tick(self.ticks)

        pygame.quit()

if __name__ == '__main__':
    simulation = Simulation()
    simulation.run()
