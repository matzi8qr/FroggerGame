import code
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
    NEXT = []
    SAFE = 0
    ROAD = 1
    RIVER = 2

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        self.NEXT = self.init_map()

    def on_draw(self):
        self.clear()
        self.draw_rows()

    def on_update(self, delta_time):
        #shh
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.cycle_map()

    #Boil down the attribute of the map into simplest form: a list of rows.
    def init_map(self):
        for i in range(3):
            self.generate_row([self.SAFE])
        self.generate_row([self.ROAD])
        next = self.generate_row([self.ROAD])
        for i in range(5):
            next = self.generate_row(next)
        return next

    # Generates the next row based off of the passed possibilities, and returning the next possibilities.
    def generate_row(self, possibilities):
        #generate row based on colors possibilities
        random_code = random.choice(possibilities)
        self.ROWS.append(random_code)
        
        #return possibilities for next row
        if random_code == self.SAFE: # prevent 2 safe rows in a row
            return [self.ROAD, self.RIVER]
        if possibilities == [self.ROAD]: # prevent road from running into river, 
                                         # allowing for safe row if it was forced to be a road (below)
            return [self.SAFE, self.SAFE, self.ROAD]
        if random_code == self.ROAD:     # insure roads generate in pairs
            return [self.ROAD]
        if random_code == self.RIVER:    # prevent river from running into road
            return [self.SAFE, self.RIVER, self.SAFE, self.RIVER, self.SAFE]

    #draw the map onto the screen
    def draw_rows(self):
        y_interval = SCREEN_HEIGHT/20.
        color_dict = {self.SAFE: arcade.color.AMAZON, self.ROAD: arcade.color.ARSENIC, self.RIVER: arcade.color.WATERSPOUT}
        for row in range(10):
            y_coord = y_interval * (2 * row + 1)
            arcade.draw_rectangle_filled(SCREEN_WIDTH/2, y_coord, SCREEN_WIDTH, 2 * y_interval, color_dict[self.ROWS[row]])

    #cycle_map handles the "infinite" map
    def cycle_map(self):
        self.NEXT = self.generate_row(self.NEXT)
        self.ROWS.pop(0)
        



if __name__ == "__main__":
    main()