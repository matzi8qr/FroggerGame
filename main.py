import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 760

def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Frogger")
    window.setup()
    arcade.run()


class Window(arcade.Window):

    ROWS = []

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.ROWS = self.create_rows()

    def on_draw(self):
        self.clear()
        for row in self.ROWS:
            row.draw()

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        pass

    #Boil down the attribute of the map into simplest form: a list of rows.
    def create_rows(self):
        rows = []
        colors = [arcade.color.RED, arcade.color.BLUE, arcade.color.GREEN]
        y_interval = SCREEN_HEIGHT/20
        for row_num in range(10):
            myColor = random.choice(colors)
            row_rect = arcade.create_rectangle_filled(SCREEN_WIDTH/2, y_interval * (2 * row_num + 1), 
                                                        SCREEN_WIDTH, 2 * y_interval, myColor)
            rows.append(row_rect)
        return rows


if __name__ == "__main__":
    main()