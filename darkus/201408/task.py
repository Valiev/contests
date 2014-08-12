from itertools import izip

symbols = {
    0 : [[1, 1, 1],
         [1, 0, 1],
         [1, 0, 1],
         [1, 0, 1],
         [1, 1, 1]],

    1 : [[1, 1, 0],
         [0, 1, 0],
         [0, 1, 0],
         [0, 1, 0],
         [1, 1, 1]],

    2 : [[1, 1, 1],
         [0, 0, 1],
         [1, 1, 1],
         [1, 0, 0],
         [1, 1, 1]],

    3 : [[1, 1, 1],
         [0, 0, 1],
         [1, 1, 1],
         [0, 0, 1],
         [1, 1, 1]],

    4 : [[1, 0, 1],
         [1, 0, 1],
         [1, 1, 1],
         [0, 0, 1],
         [0, 0, 1]],

    5 : [[1, 1, 1],
         [1, 0, 0],
         [1, 1, 1],
         [0, 0, 1],
         [1, 1, 1]],

    6 : [[1, 1, 1],
         [1, 0, 0],
         [1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]],

    7 : [[1, 1, 1],
         [0, 0, 1],
         [0, 1, 1],
         [0, 1, 0],
         [0, 1, 0]],

    8 : [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]],

    9 : [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 1],
         [0, 0, 1],
         [1, 1, 1]],
}

ROWS_NUM = len(symbols[0])


def process_line(line, line_number, processed_data):
    """ Processed data is a list (start_x, start_y, num) """
    for pos, (a, b, c) in enumerate(izip(line, line[1:], line[2:])):
        # check whether given number continue matching in current row
        for start_x, start_y, num in processed_data:
            if start_x != pos:
                continue

            line_to_check = line_number - start_y
            if [a, b, c] == symbols[num][line_to_check]:
                yield (start_x, start_y, num)

        # May be there is a new matching starts in this row
        for num in symbols:
            if [a, b, c] == symbols[num][0]:
                yield (pos, line_number, num)


def find_numbers_in_file(fp):
    results = []
    for y, row in enumerate(fp):
        line = map(int, row.strip())
        res_collection = []
        for start_x, start_y, num in process_line(line, y, results):
            # Found the number
            if y - start_y >= ROWS_NUM - 1:
                yield start_x, start_y, num
            # Continue processing
            else:
                res_collection.append((start_x, start_y, num))
        results = res_collection


if __name__ == "__main__":
    with open('input.txt') as fp:
        for x, y, n in find_numbers_in_file(fp):
            print n, '@', '(%d, %d)' % (x, y)
