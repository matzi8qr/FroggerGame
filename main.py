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

    def setup(self):
        self.init_map()

    def on_draw(self):
        self.clear()
        for row in self.ROWS:
            row.draw()

    def on_update(self, delta_time):
        #shh
        pass

    def on_key_press(self, key, modifiers):
        pass

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
        y_interval = SCREEN_HEIGHT/20.
        random_color = random.choice(possibilities)
        y_coord = y_interval * (2 * self.ROWS.__len__() + 1)
        row_rect = arcade.create_rectangle_filled(SCREEN_WIDTH/2., y_coord, SCREEN_WIDTH, 2 * y_interval, random_color)
        self.ROWS.append(row_rect)
        
        #return possibilities for next row
        if random_color == self.SAFE:
            return [self.ROAD, self.RIVER]
        if possibilities == [self.ROAD]:
            return [self.SAFE, self.ROAD]
        if random_color == self.ROAD:
            return [self.ROAD]
        if random_color == self.RIVER:
            return [self.RIVER, self.SAFE]




if __name__ == "__main__":
    main()