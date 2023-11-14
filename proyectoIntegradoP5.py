
import readchar

class LabyrinthGame:
    def __init__(self, labyrinth, player_x, player_y, exit_x, exit_y):
        self.labyrinth = labyrinth
        self.player_x = player_x
        self.player_y = player_y
        self.exit_x = exit_x
        self.exit_y = exit_y

    def display(self):
        # Clear the screen
        print("\033c", end="")

        # Display the labyrinth
        for y, row in enumerate(self.labyrinth):
            for x, cell in enumerate(row):
                if x == self.player_x and y == self.player_y:
                    print("P", end="")
                else:
                    print(cell, end="")
            print()

    def check_win(self):
        # Check if the player has reached the exit
        return self.player_x == self.exit_x and self.player_y == self.exit_y

    def move_player(self, move):
        # Update the player's position based on input
        if move == 'w' and self.labyrinth[self.player_y - 1][self.player_x] != '#':
            self.player_y -= 1
        elif move == 's' and self.labyrinth[self.player_y + 1][self.player_x] != '#':
            self.player_y += 1
        elif move == 'a' and self.labyrinth[self.player_y][self.player_x - 1] != '#':
            self.player_x -= 1
        elif move == 'd' and self.labyrinth[self.player_y][self.player_x + 1] != '#':
            self.player_x += 1

def main():
    # Define the labyrinth as a list of strings
    labyrinth = [
        '..###################',
        '....#...............#',
        '#.#.#####.#########.#',
        '#.#...........#.#.#.#',
        '#.#####.#.###.#.#.#.#',
        '#...#.#.#.#.....#...#',
        '#.#.#.#######.#.#####',
        '#.#...#.....#.#...#.#',
        '#####.#####.#.#.###.#',
        '#.#.#.#.......#...#.#',
        '#.#.#.#######.#####.#',
        '#...#...#...#.#.#...#',
        '###.#.#####.#.#.###.#',
        '#.#...#.......#.....#',
        '#.#.#.###.#.#.###.#.#',
        '#...#.#...#.#.....#.#',
        '###.#######.###.###.#',
        '#.#.#.#.#.#...#.#...#',
        '#.#.#.#.#.#.#.#.#.#.#',
        '#.....#.....#.#.#.#.#',
        '###################..'
    ]

    # Create a LabyrinthGame instance
    game = LabyrinthGame(labyrinth, player_x=1, player_y=1, exit_x=5, exit_y=5)

    # Game loop
    while True:
        # Display the game
        game.display()

        # Check if the player has won
        if game.check_win():
            print("Congratulations! You've reached the exit!")
            break

        # Read the player's input
        move = readchar.readchar()

        # Update the player's position based on input
        game.move_player(move)

if __name__ == "__main__":
    main()

