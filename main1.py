from enviroment import Enviroment
from rover import Rover
import time


env = Enviroment(width=10, height=10, obstacle_ratio=0.2)
rover = Rover(env, rover_x=0, rover_y=0, battery=100)
while True:
    target_x, target_y, is_moved = rover.next_move()

    if is_moved:
       print(f"  -> BAŞARILI: ({target_x}, {target_y}) konumuna geçildi.")
    else:
        print(
        f"  -> REDDEDİLDİ: ({target_x}, {target_y}) konumuna hamle denendi ama"
        " engel/sınır var!"
    )
    if env.grid[rover.y][rover.x] == "T":
        print("Rover has reached the target!")
        break
    if rover.battery <= 0:
        print("Rover has run out of battery!")
        break
    print("* " * 15)
    time.sleep(0.2)
rover.print_stats()



    





