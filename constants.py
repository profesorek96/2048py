FONT_NAME = 'freesansbold.ttf'
BG_COLOR = '#dedec7'


class TilesColor():
    __TILES_COLOR = {
        0: ('#ffeebc', '#43433c'),
        2: ('#ea9f44', '#43433c'),
        4: ('#76b5c5', '#43433c'),
        8: ('#c8c83b', '#43433c'),
        16: ('#d2b700', '#43433c'),
        32: ('#d8491f', '#43433c'),
        64: ('#08b12c', '#43433c'),
        128: ('#b10808', '#e8e8d8'),
        256: ('#b16108', '#e8e8d8'),
        512: ('#4f08b1', '#e8e8d8'),
        1024: ('#b108a2', '#e8e8d8'),
        2048: ('#790419', '#e8e8d8'),
        4096: ('#047929', '#e8e8d8'),
        8192: ('#013b1d', '#e8e8d8'),
        16384: ('#6b022e', '#e8e8d8')}

    @staticmethod
    def get_tile_color(value):
        if value in TilesColor.__TILES_COLOR:
            return TilesColor.__TILES_COLOR[value][0]
        else:
            return '#43433c'

    @staticmethod
    def get_font_color(value):
        if value in TilesColor.__TILES_COLOR:
            return TilesColor.__TILES_COLOR[value][1]
        else:
            return '#e8e8d8'
