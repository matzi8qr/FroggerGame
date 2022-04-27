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
    SAFE = arcade.color.AMAZON
    ROAD = arcade.color.ARSENIC
    RIVER = arcade.color.WATERSPOUT

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.ROWS = self.create_rows()

    def on_draw(self):
        self.clear()
        for row in self.ROWS:
            arcade.draw_rectangle_filled(row[0], row[1], row[2], row[3], row[4])

    def on_update(self, delta_time):
        #shh
        pass

    def on_key_press(self, key, modifiers):
        pass

    #Boil down the attribute of the map into simplest form: a list of rows.
    def create_rows(self):
        rows = []
        colors = [self.SAFE, self.ROAD, self.RIVER]
        y_interval = SCREEN_HEIGHT/20

        #randomly generate
        for row_num in range(10):
            my_color = random.choice(colors)
            row_rect_params = [SCREEN_WIDTH/2, y_interval * (2 * row_num + 1), 
                                SCREEN_WIDTH, 2 * y_interval, my_color]
            rows.append(row_rect_params)

        
        #"fix" map, make sure to start with 3 safe spaces, make sure roads generate in pairs...
        # start with 3 Safes
        for row_num in range(3):
            rows[row_num][4] = self.SAFE
        # next, go to road
        rows[3][4] = self.ROAD
        # make sure roads generate in pairs
        num_roads = 1
        for row in rows[4:]:
            if row[4] == self.ROAD:
                num_roads += 1
            elif num_roads != 0:    
                row[4] = self.ROAD
                num_roads -= 1

        return rows


if __name__ == "__main__":
    main()