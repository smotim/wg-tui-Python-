import time
import curses


def draw(canvas):
    row, column = (4, 20)
    button_row = 3

    # Отрисовка кнопок
    canvas.addstr(button_row, column, 'Button 1', curses.A_REVERSE)
    canvas.addstr(button_row, column + 10, 'Button 2', curses.A_REVERSE)
    canvas.addstr(button_row, column + 20, 'Button 3', curses.A_REVERSE)

    # Отрисовка бокса
    text_win = curses.newwin(row - 2, canvas.getmaxyx()[1] - 2, 1, 1)
    text_win.box()

    # Добавление текста в бокс
    text_win.addstr(1, 1, 'Hello, World!')

    # Отключение курсора
    curses.curs_set(False)

    # Обновление экрана
    canvas.refresh()
    time.sleep(100)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
