import curses
import random

# Initialize the screen
screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
screen.keypad(1)
curses.curs_set(0)  # Hide cursor

scrSize = screen.getmaxyx()  # Get screen size

# Starting position of the snake
headY = scrSize[0] // 4
headX = scrSize[1] // 2

# Initial food position
foodPos = [scrSize[0] // 2, scrSize[1] // 2]

# Initial snake position and size
snakePos = [
    [headY, headX],  # Head
    [headY, headX + 1],  # Body
    [headY, headX + 2]  # Tail
]

snakeLength = len(snakePos)
lives = 3

def exchange(snake):
    """Shift snake body forward"""
    for i in range(len(snake) - 1, 0, -1):
        snake[i][0] = snake[i - 1][0]
        snake[i][1] = snake[i - 1][1]

def grow_snake(snake):
    """Add a new segment at the tail of the snake"""
    tail = snake[-1]
    new_tail = [tail[0], tail[1]]
    snake.append(new_tail)

def displaySnake(snakePos, snakeLength,lives):
    """Display the snake on the screen"""
    if lives != 0:
        for i in range(snakeLength):
            if 0 <= snakePos[i][0] < scrSize[0] - 1 and 0 <= snakePos[i][1] < scrSize[1] - 1:
                screen.addch(snakePos[i][0], snakePos[i][1], curses.ACS_BLOCK, curses.color_pair(2))
    else:
        screen.clear()
        quit()

def reset_snake():
    """Reset the snake's position for the next life"""
    headY = scrSize[0] // 4
    headX = scrSize[1] // 2
    return [
        [headY, headX],  # head
        [headY, headX + 1],  # body
        [headY, headX + 2]  # tail
    ]

while True:
    screen.clear()
    screen.addch(foodPos[0], foodPos[1], curses.ACS_DIAMOND, curses.color_pair(1))
    
    screen.addch(1, scrSize[1] - 7, curses.ACS_LANTERN, curses.color_pair(1))
    screen.addstr(1, scrSize[1] - 5, str(lives))

    # Snake eats food
    if snakePos[0] == foodPos:
        foodPos = [random.randint(1, scrSize[0] - 2), random.randint(1, scrSize[1] - 2)]
        screen.addch(foodPos[0], foodPos[1], curses.ACS_DIAMOND, curses.color_pair(1))
        grow_snake(snakePos)

    else:
        # Erase the old tail
        tailY, tailX = snakePos[-1]
        if 0 <= tailY < scrSize[0] and 0 <= tailX < scrSize[1]:
            screen.addch(tailY, tailX, ' ')  # Erase old tail

    # Display the snake
    displaySnake(snakePos, snakeLength,lives)
    
    key = screen.getch()
    if key == ord('q'):
        quit()

    # Check for game-over conditions (snake collides with itself or wall)
    if snakePos[0] in snakePos[1:] or snakePos[0][0] in (0, scrSize[0] - 1) or snakePos[0][1] in (0, scrSize[1] - 1):
        if lives==0:
            quit()
            
        else:
            lives -= 1
            snakePos = reset_snake()  # Reset snake position for new life
            snakeLength = len(snakePos)  # Reset snake length

    # Move snake based on key input
    if key == 450:  # Up
        exchange(snakePos)
        snakePos[0][0] -= 1
    elif key == 456:  # Down
        exchange(snakePos)
        snakePos[0][0] += 1
    elif key == 454:  # Right
        exchange(snakePos)
        snakePos[0][1] += 1
    elif key == 452:  # Left
        exchange(snakePos)
        snakePos[0][1] -= 1

    screen.refresh()

# End the curses window when the game is over
curses.endwin()
