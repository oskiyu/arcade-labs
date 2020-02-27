"""

Dibujo to wapo xd

"""

import arcade

x = 0
y = 0
izquierda = True
arriba = True


def on_update(delta_time):
    global x
    global y
    global izquierda
    global arriba
    if izquierda:
        x += 5 * 30 * delta_time
        if x > 800 - 25:
            izquierda = False
    else:
        x -= 5 * 30 * delta_time
        if x < 0 + 25:
            izquierda = True

    if arriba:
        y += 5 * 30 * delta_time
        if y > 600 - 25:
            arriba = False
    else:
        y -= 5 * 30 * delta_time
        if y < 0 + 25:
            arriba = True


def on_draw(delta_time):
    arcade.start_render()

    arcade.draw_circle_filled(800, 600, 120, arcade.color.YELLOW)
    arcade.draw_line(800, 600, 400, 600, arcade.color.YELLOW, 5)
    arcade.draw_line(800, 600, 800, 200, arcade.color.YELLOW, 5)

    arcade.draw_line(800, 600, 600, 400, arcade.color.YELLOW, 5)
    arcade.draw_line(800, 600, 700, 400, arcade.color.YELLOW, 5)
    arcade.draw_line(800, 600, 500, 400, arcade.color.YELLOW, 5)

    arcade.draw_line(800, 600, 600, 500, arcade.color.YELLOW, 5)
    arcade.draw_line(800, 600, 600, 600, arcade.color.YELLOW, 5)
    arcade.draw_line(800, 600, 600, 400, arcade.color.YELLOW, 5)

    arcade.draw_circle_filled(775, 575, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(725, 575, 5, arcade.color.BLACK)

    arcade.draw_lrtb_rectangle_filled(0, 800, 80, 0, arcade.color.GREEN_YELLOW)
    arcade.draw_rectangle_filled(100, 100, 50, 50, arcade.color.RED)
    arcade.draw_rectangle_filled(100, 100, 50, 20, arcade.color.YELLOW)
    arcade.draw_text("XD " + str(int(1 / delta_time)), 300, 200, arcade.color.AMETHYST, 30)

    arcade.draw_triangle_filled(250 + 40, 350, 250, 350 - 100, 250 + 80, 350 - 100, arcade.color.GO_GREEN)
    arcade.draw_triangle_outline(250 + 40, 350, 250, 350 - 100, 250 + 80, 350 - 100, arcade.color.GREEN)

    arcade.draw_ellipse_filled(290, 285, 50, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(290, 285, 10, arcade.color.WHITE)
    arcade.draw_circle_filled(290, 285, 5, arcade.color.BLACK)

    arcade.draw_arc_filled(750, 575, 15, 20, arcade.color.BLACK, 180, 360)

    arcade.draw_circle_filled(x, y, 25, arcade.color.BLUE)


def main():
    arcade.open_window(800, 600, "XD")
    arcade.set_background_color(arcade.color.FRESH_AIR)

    arcade.schedule(on_update, 1 / 60)
    arcade.schedule(on_draw, 1 / 60)

    arcade.run()


main()
