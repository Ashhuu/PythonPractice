import pygame
listXY = [240, 240]
goalXY = [100, 100]


def add_cube(w, rows, surface, list_XY):
    size = rows//w
    if list_XY[0] == goalXY[0] and list_XY[1] == goalXY[1]:
        pygame.font.init()
        my_font = pygame.font.SysFont('Arial', 50)
        text_surface = my_font.render('You Won!', False, (255, 0, 255))
        surface.blit(text_surface, (w/2-50, w/2-50))
        pygame.draw.rect(surface, (255, 255, 0), ((goalXY[0] + 1, goalXY[1] + 1), (rows - 1, rows - 1)), 0)
        redraw()
        pygame.time.delay(10000)
        pygame.time.delay(10)
    else:
        pygame.draw.rect(surface, (255, 0, 0), ((list_XY[0] + 1, list_XY[1] + 1), (rows - 1, rows - 1)), 0)


def draw_goal(w, rows, surface, goalXY):
    size = rows//w
    pygame.draw.rect(surface, (0, 255, 0), ((goalXY[0] + 1, goalXY[1] + 1), (rows - 1, rows - 1)), 0)


def draw_grid(w, rows, surface):
    size = rows//w
    for i in range(0, w, rows):
        pygame.draw.line(surface, (255, 255, 255), [i, 0], [i, w], 1)
        pygame.draw.line(surface, (255, 255, 255), [0, i], [w, i], 1)
        draw_goal(w, rows, surface, goalXY)


def move_down(run, surface):
    for i in range(1, run):
        listXY[1] = listXY[1] + 20
        add_cube(400, 20, surface, listXY)
        redraw()
        pygame.time.delay(40)


def move_up(run, surface):
    for i in range(1, run):
        listXY[1] = listXY[1] - 20
        add_cube(400, 20, surface, listXY)
        redraw()
        pygame.time.delay(40)


def move_right(run, surface):
    for i in range(1, run):
        listXY[0] = listXY[0] + 20
        add_cube(400, 20, surface, listXY)
        redraw()
        pygame.time.delay(40)


def move_left(run, surface):
    for i in range(1, run):
        listXY[0] = listXY[0] - 20
        add_cube(400, 20, surface, listXY)
        redraw()
        pygame.time.delay(40)


def find_goal(w, rows, surface, listXY, inc):
    while inc < 40:
        move_down(inc, surface)
        move_right(inc, surface)
        move_up(inc+1, surface)
        move_left(inc+1, surface)
        find_goal(w, rows, surface, listXY, inc+2)
        pygame.display.update()
        pygame.time.wait(25)
    start(w, rows)


def start(w, r):

    window = pygame.display.set_mode((w, w))
    window.fill((0, 0, 0))
    draw_grid(w, r, window)
    add_cube(w, r, window, listXY)

    pygame.display.update()
    pygame.time.delay(100)

    return window


def redraw():
    pygame.display.update()


def main():
    play = 'true'
    width = 500
    rows = 20
    window = start(width, rows)
    while play:

        draw_grid(width, rows, window)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    while 1:
                        if event.key == pygame.K_UP:
                            goalXY[1] = goalXY[1] - rows
                            draw_goal(width, rows, window, goalXY)
                            redraw()
                        if event.key == pygame.K_DOWN:
                            goalXY[1] = goalXY[1] + rows
                            draw_goal(width, rows, window, goalXY)
                            redraw()
                        if event.key == pygame.K_LEFT:
                            goalXY[0] = goalXY[0] - rows
                            draw_goal(width, rows, window, goalXY)
                            redraw()
                        if event.key == pygame.K_RIGHT:
                            goalXY[0] = goalXY[0] + rows
                            draw_goal(width, rows, window, goalXY)
                            redraw()
                        if event.key == pygame.K_g:
                            break
                if event.key == pygame.K_UP:
                    listXY[1] = listXY[1] - rows
                    add_cube(width, rows, window, listXY)
                    redraw()
                if event.key == pygame.K_DOWN:
                    listXY[1] = listXY[1] + rows
                    add_cube(width, rows, window, listXY)
                    redraw()
                if event.key == pygame.K_LEFT:
                    listXY[0] = listXY[0] - rows
                    add_cube(width, rows, window, listXY)
                    redraw()
                if event.key == pygame.K_RIGHT:
                    listXY[0] = listXY[0] + rows
                    add_cube(width, rows, window, listXY)
                    redraw()
                if event.key == pygame.K_SPACE:
                    find_goal(width, rows, window, listXY, 1)



main()