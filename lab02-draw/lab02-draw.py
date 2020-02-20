"""

Dibujo to wapo xd

"""

import arcade

arcade.open_window(800, 600, "XD")

arcade.set_background_color(arcade.color.FRESH_AIR)


arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 80, 0, arcade.color.GREEN_YELLOW)
arcade.draw_rectangle_filled(100, 100, 50, 50, arcade.color.RED)
arcade.draw_rectangle_filled(100, 100, 50, 20, arcade.color.YELLOW)
arcade.draw_text("XD", 300, 200, arcade.color.AMETHYST, 30)

arcade.draw_triangle_filled(250 + 40, 350, 250, 350 - 100, 250 + 80, 350 - 100, arcade.color.GO_GREEN)
arcade.draw_triangle_outline(250 + 40, 350, 250, 350 - 100, 250 + 80, 350 - 100, arcade.color.GREEN)

arcade.draw_ellipse_filled(290, 285, 50, 20, arcade.color.BLACK)
arcade.draw_circle_filled(290, 285, 10, arcade.color.WHITE)
arcade.draw_circle_filled(290, 285, 5, arcade.color.BLACK)

arcade.draw_circle_filled(200, 200, 25, arcade.color.BLUE)

arcade.finish_render()

arcade.run()
