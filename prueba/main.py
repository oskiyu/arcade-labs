import arcade

WindowWidth = 800
WindowHeight = 600
WindowName = "xd"

class Game(arcade.Window):

    def __init__(self):
        super.__init__(WindowWidth, WindowHeight, WindowName)

    def on_draw(self):
        arcade.start_render()