from test_framework import generic_test


def flip_color(x, y, m):
    # TODO - you fill in here.
    def adj(loc):
        x, y = loc
        return [(k,l) for k,l in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)] if 0<=k<height and 0<=l<width]

    def flip_color_helper(loc):
        x, y = loc
        if m[x][y] == color_flip_to:
            return
        m[x][y] = color_flip_to
        for neighbor in adj(loc):
            flip_color_helper(neighbor)

    if not m or not m[0]:
        return

    height = len(m)
    width = len(m[0])
    color_flip_to = not m[x][y]

    flip_color_helper((x,y))


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
