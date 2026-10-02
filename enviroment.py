import random
class Enviroment:
    def __init__(self, width=10 , height=10 , obstacle_ratio=0.2):
        self.width = width
        self.height = height
        self.obstacle_ratio = obstacle_ratio
        self.grid = [["." for _ in range(width)] for _ in range(height)]
        self.place_obstacles()
        self.place_target()
    def place_obstacles(self):
        num_obstacles = int(self.width * self.height * self.obstacle_ratio)
        placed = 0
        while placed < num_obstacles:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.grid[y][x] == "." and (x,y) != (0,0):
                self.grid[y][x]= "X"
                placed += 1
    def place_target(self):
        min_x = self.width // 2
        min_y = self.height // 2
        while True:
            x = random.randint(min_x, self.width -1)
            y = random.randint(min_y, self.height -1)
            if self.grid[y][x] == ".":
                self.grid[y][x] = "T"
                break
    def is_valid_move(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height and self.grid[y][x] != "X":
            return True
        return False
    def is_valid_motion(self, x, y , next_x , next_y):
        is_neighbor = (
        (next_x == x + 1 and next_y == y)
        or (next_x == x - 1 and next_y == y)
        or (next_x == x and next_y == y + 1)
        or (next_x == x and next_y == y - 1)
    )
        is_safe = self.is_valid_move(next_x, next_y)
        if is_neighbor and is_safe:
            return True
        return False
    



        

    

  
        

        
    


