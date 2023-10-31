import readchar

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

# Define the player's position
player_x = 1
player_y = 1

# Define the exit position
exit_x = 5
exit_y = 5

# Game loop
while True:
    # Clear the screen
    print("\033c", end="")

    # Display the labyrinth
    for y, row in enumerate(labyrinth):
        for x, cell in enumerate(row):
            if x == player_x and y == player_y:
                print("P", end="")
            else:
                print(cell, end="")
        print()

    # Check if the player has reached the exit
    if player_x == exit_x and player_y == exit_y:
        print("Congratulations! You've reached the exit!")
        break

    # Read the player's input
    move = readchar.readchar()

    # Update the player's position based on input
    if move == 'w' and labyrinth[player_y - 1][player_x] != '#':
        player_y -= 1
    elif move == 's' and labyrinth[player_y + 1][player_x] != '#':
        player_y += 1
    elif move == 'a' and labyrinth[player_y][player_x - 1] != '#':
        player_x -= 1
    elif move == 'd' and labyrinth[player_y][player_x + 1] != '#':
        player_x += 1
