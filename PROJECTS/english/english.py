import random
import pygame
import pygame.font


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Set up the game
pygame.init()

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Maze Game")
font = pygame.font.Font(None, 15)

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.Font(None, 36)


para2 = "Thesis: Orwell displays many forms in which propaganda is used by various characters in the story to achieve their overall intentions. \nSuch an example is the character Squeaker, as he uses his persuasive speaking abilities to manipulate the other animals’ thinkings and make the animals believe his lies. \nAccording to the story, Squealer states “Do not imagine, comrades, that leadership is a pleasure…. \nBut sometimes you might make the wrong decisions, comrades, and then where should we be” (Orwell, Chapter 9)?\nOften, Squealer uses forms of fear and doubt for the animals to confuse themselves and question their own beliefs. \nThis changes their way of thinking and leads them to believe that Napoleon’s decisions determine their benefits. \nPropaganda is used by Squealer’s language to achieve his goal of making the rest of the animals side with Napoleon’s authority."
para1 = "The story was written in 1945 and is based on the historical event known as the Russian Revolution.\nA variety of animals are presented in the story to display the situations and history of Soviet Communism. \nOne instance in the story is the character Old Major. \nIn the story he quotes, “What then must we do? Why, work night and day, body and soul, for the overthrow of the human race! That is my message to you, comrades: Rebellion (Orwell, Chapter 1)! \nThe character Old Major presents to the other animals about the idea of “Animalism” and persuades them to create a revolution/rebellion against the humans in the fight for equality and justice. \nOld Major’s motives correlate to an important figure in the Russian Revolution, Karl Max, as he also makes a speech about Communist Manifesto that initiated a rebellion against the Russian tsar.\nBoth speeches discuss the corruption and unfairness in their governments. \nThe animal, Old Major, is seen as Karl Max to show how Animal Farm is influenced by specific people and events from the Russian Revolution."
para3 = "The book Animal Farm uses many Rhetorical devices to show symbolism and relevance to other context and topics.\nHowever one rhetorical device that stands out compared to others is Allegory.\nThe use of allegory in the book Animal farm makes many connections to the past.\nFor example, the book mentions “'They dashed straight for Snowball, who only sprang from his place just in time to escape their snapping jaws.'(Orwell, Chapter 5).\nThe quote shows the resemblance of the power shifting during the times of the Russian Revolution, as Napoleon uses his military power to chase Snowball out of the farm.\nThis changes the lives of the animals on the farm the same way the shift in power changed the lives of the citizens in Russia during that time."
para4 = "The book Animal Farm by George Orwell covers an important topic about the corruption and cycle of power.\nSpecifically, those in authority will use their position to exploit those in lower positions to obtain their wants, varying through power consolidation in forms of propaganda or control.\nThese changes in power eventually lead to a never-ending cycle of corruption and oppression in which the only solution is by thinking critically and being attentive of the outcomes. \nAround the end of the book, it states that 'All animals are equal, but some animals are more equal than others' (Orwell, Chapter 10). \nThe change in the commandment shows a shift in power amongst animals. \nPreviously, it was “All Animals are equal”, however it has changed into only “some” having more power.\nThis new commandment shows how the animals have changed their previous beliefs to justify their unique privileges and oppression/inequality amongst other animals."
# Generate the maze
def generate_maze(attempts):
    # Set up the maze
    maze_width = 20
    maze_height = 15
    maze = []
    for row in range(maze_height):
        if row == 0 or row == maze_height-1:
            # Add a border at the top and bottom of the maze
            maze.append([1] * maze_width)
        else:
            maze.append([0] * maze_width)
            maze[row][0] = 1  # Add a border on the left side of the maze
            maze[row][maze_width-1] = 1  # Add a border on the right side of the maze

    # Add a path through the maze
    for x in range(1, maze_width-1):
        maze[maze_height//2][x] = 0

    # Add a key to the maze
    key_x = random.randint(1, maze_width-2)
    key_y = random.randint(1, maze_height-2)
    maze[key_y][key_x] = 2

    # Add some obstacles to the maze
    for i in range(5):
        obstacle_x = random.randint(1, maze_width-2)
        obstacle_y = random.randint(1, maze_height-2)
        maze[obstacle_y][obstacle_x] = 1

    return maze, key_x, key_y


# Initialize the maze
maze, key_x, key_y = generate_maze(1)


# Set up the player
player_x = 1
player_y = len(maze) // 2

# Set up the game loop
game_over = False
has_key = False
attempts = 1
printed = []

while attempts < 5:
    # Process events

    if attempts == 1 and 1 not in printed:
        print(para1)
        print("---------------------------------------------------------------------")
        printed.append(1)
    elif attempts == 2 and 2 not in printed:
        print(para2)
        print("---------------------------------------------------------------------")
        printed.append(2)
    elif attempts == 3 and 3 not in printed:
        print(para3)
        print("---------------------------------------------------------------------")
        printed.append(3)
    elif attempts == 4 and 4 not in printed:
        print(para4)
        printed.append(4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if maze[player_y-1][player_x] != 1:
                    player_y -= 1
            elif event.key == pygame.K_s:
                if maze[player_y+1][player_x] != 1:
                    player_y += 1
            elif event.key == pygame.K_a:
                if maze[player_y][player_x-1] != 1:
                    player_x -= 1
            elif event.key == pygame.K_d:
                if maze[player_y][player_x+1] != 1:
                    player_x += 1

    # Check if the player has reached the key
    if player_x == key_x and player_y == key_y:
        attempts += 1
        maze, key_x, key_y = generate_maze(attempts)
        has_key = True


    # Draw the screen
    screen.fill(WHITE)

    # Draw the maze
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, BLACK, [x*20, y*20, 20, 20])
            elif maze[y][x] == 2:
                pygame.draw.rect(screen, (255, 255, 0), [x*20, y*20, 20, 20])

    # Draw the player
    pygame.draw.rect(screen, (0, 0, 255), [player_x*20, player_y*20, 20, 20])

    # Draw the text

    # Update the screen
    pygame.display.flip()

    # Set the game over condition
    if player_x == len(maze[0])-2 and player_y == len(maze)//2:
        game_over = True

    # Set the clock speed
    clock.tick(60)



# Quit the game
pygame.quit()

   
