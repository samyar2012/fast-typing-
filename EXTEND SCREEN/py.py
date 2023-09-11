import random

class MinecraftLite:
    def __init__(self):
        self.world = [['.' for _ in range(10)] for _ in range(10)]
        self.player_x = 0
        self.player_y = 0

    def print_world(self):
        for row in self.world:
            print(' '.join(row))
        print()

    def mine_block(self):
        x, y = self.player_x, self.player_y
        if self.world[x][y] == 'X':
            print("You've already mined this block.")
        else:
            print("Mining block...")
            self.world[x][y] = 'X'

    def move(self, direction):
        x, y = self.player_x, self.player_y
        if direction == 'w':
            x -= 1
        elif direction == 's':
            x += 1
        elif direction == 'a':
            y -= 1
        elif direction == 'd':
            y += 1

        if 0 <= x < 10 and 0 <= y < 10:
            self.player_x, self.player_y = x, y
        else:
            print("You can't move there. Stay inside the 10x10 world.")

    def play(self):
        while True:
            self.print_world()
            print("Options: (w) Up, (s) Down, (a) Left, (d) Right, (m) Mine, (q) Quit")
            choice = input("Enter your choice: ").lower()

            if choice == 'q':
                print("Thanks for playing!")
                break
            elif choice == 'm':
                self.mine_block()
            elif choice in ['w', 's', 'a', 'd']:
                self.move(choice)
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    game = MinecraftLite()
    game.play()
