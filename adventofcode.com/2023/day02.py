class Game:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def check_input_line(self, line):
        # Game ID: X color, Y color; Z color
        game_prefix, rest = line.split(': ')
        game_id = int(game_prefix[len('Game')+1:])
        print(game_prefix)
        for color_string in rest.split('; '):
            r, g, b = (0, 0, 0)
            for colorlet in color_string.split(', '):
                num, color = colorlet.split(' ')
                color = color.strip()
                num = int(num)
                if color == 'red':
                    r = num
                if color == 'green':
                    g = num
                if color == 'blue':
                    b = num
            print('- checking', r, g, b)
            if any([r > self.red, g > self.green, b > self.blue]):
                print('skipping game', game_id)
                return None
        print(game_prefix, 'ok')
        return game_id


# Determine which games would have been possible if the bag had been loaded with
# only 12 red cubes, 13 green cubes, and 14 blue cubes
def main():
    game = Game(12, 13, 14)
    total = 0
    for line in open('day02.input'):
        id = game.check_input_line(line)
        if id is not None:
            total += id
    print(total)


if __name__ == "__main__":
    main()
