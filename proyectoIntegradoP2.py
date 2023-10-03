import readchar

while True:
    key = readchar.readkey()
    if key == readchar.key.UP:
        print('up arrow key pressed')
        break
    else:
        print(key)
        