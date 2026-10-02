import random
class Rover:
    def __init__(self, env , rover_x=0 , rover_y=0 , battery=100):
        self.env = env
        self.x = rover_x
        self.y = rover_y
        self.total_attempts = 0  
        self.successful_moves = 0  
        self.failed_moves = 0  
        self.battery = battery
    def move(self, next_x, next_y):
        if self.env.is_valid_motion(self.x, self.y, next_x, next_y) == True:
            self.x = next_x
            self.y = next_y
            return True
        return False
        
    def next_move(self):
        moves = [(self.x + 1, self.y), (self.x - 1, self.y), (self.x, self.y + 1), (self.x, self.y - 1)]
        next_move = random.choice(moves)
        next_x, next_y = ( next_move[0] , next_move[1] )
        self.battery -= 1
        success = self.move(next_x, next_y)
        if success:
            self.successful_moves += 1
        else:
            self.failed_moves += 1
        return next_x, next_y , success
    def print_stats(self):
        """Simulation statistics."""
        print("\n" + "=" * 20)
        print("Simulation Statistics")
        print("=" * 20)
        print(f"Total Moves Attempted: {self.successful_moves + self.failed_moves}")
        print(f"Successful Moves: {self.successful_moves}")
        print(f"Failed Moves: {self.failed_moves}")
        if self.successful_moves + self.failed_moves > 0:
            success_rate = (self.successful_moves / (self.successful_moves + self.failed_moves)) * 100
            print(f"success Rate: {success_rate}%")
        print(f"Battery Level: {self.battery}")
