from tkinter import *

DIGITS_MAP = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

start_point = (16, 16)
color_outline = "violetred1"
color_fill = "purple4"


def vertical_line(offset_x=0, offset_y=0):
    if offset_x != 0:
        offset_x *= 70
    if offset_y != 0:
        offset_y *= 70
    return (start_point[0] + offset_x, start_point[1] + offset_y,
            start_point[0] + 5 + offset_x, start_point[1] + 5 + offset_y,
            start_point[0] + 5 + offset_x, start_point[1] + 65 + offset_y,
            start_point[0] + offset_x, start_point[1] + 70 + offset_y,
            start_point[0] - 5 + offset_x, start_point[1] + 65 + offset_y,
            start_point[0] - 5 + offset_x, start_point[1] + 5 + offset_y)


def horizontal_line(offset_x=0, offset_y=0):
    if offset_x != 0:
        offset_x *= 70
    if offset_y != 0:
        offset_y *= 70
    return (start_point[0] + offset_x, start_point[1] + offset_y,
            start_point[0] + 5 + offset_x, start_point[1] - 5 + offset_y,
            start_point[0] + 65 + offset_x, start_point[1] - 5 + offset_y,
            start_point[0] + 70 + offset_x, start_point[1] + offset_y,
            start_point[0] + 65 + offset_x, start_point[1] + 5 + offset_y,
            start_point[0] + 5 + offset_x, start_point[1] + 5 + offset_y)


def digit_handler(event):
    print("pressed")
    print(event.char)
    display.itemconfig("all", state="hidden")
    try:
        display.itemconfig(DIGITS_MAP[int(event.char)], state="normal")
    except ValueError:
        print("Please press a digit.")


root = Tk()

display = Canvas(root, bg="black", width=100, height=170)
display.pack()

h1 = display.create_polygon(horizontal_line(),
                            outline=color_outline,
                            width=1,
                            fill=color_fill,
                            tags=("two", "three", "five", "six", "seven", "eight", "nine", "zero"))

h2 = display.create_polygon(horizontal_line(0, 1),
                            outline=color_outline,
                            width=1,
                            fill=color_fill,
                            tags=("two", "three", "four", "five", "six", "eight", "nine"))

h3 = display.create_polygon(horizontal_line(0, 2),
                            outline=color_outline,
                            width=1,
                            fill=color_fill,
                            tags=("two", "three", "five", "six", "eight", "zero"))

v1 = display.create_polygon(vertical_line(),
                            outline=color_outline,
                            width=1,
                            fill=color_fill,
                            tags=("four", "five", "six", "eight", "nine", "zero"))

v2 = display.create_polygon(vertical_line(1, 0),
                            outline=color_outline,
                            width=1,
                            fill=color_fill,
                            tags=("one", "two", "three", "four", "seven", "eight", "nine", "zero"))

v3 = display.create_polygon(vertical_line(0, 1),
                            outline=color_outline,
                            width=1,
                            fill=color_fill,
                            tags=("two", "six", "eight", "zero"))

v4 = display.create_polygon(vertical_line(1, 1),
                            outline=color_outline,
                            width=1,
                            fill=color_fill,
                            tags=("one", "three", "four", "five", "six", "seven", "eight", "nine", "zero"))

# display.itemconfig("all", state="hidden")
display.bind_all("<Key>", digit_handler)

root.mainloop()