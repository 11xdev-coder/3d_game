from settings import *

text_map = [
    'WWWWWWWWWWWW',
    'W.........WW',
    'W..W.......W',
    'W....W.....W',
    'W......W...W',
    'W...W...W..W',
    'W....WW....W',
    'W....WWWWWWW',
    'W.......WW.W',
    'W.WWW....WWW',
    'W.WWW..W...W',
    'W......W...W',
    'W....WW....W',
    'WW.........W',
    'W....WW....W',
    'W.W....WWW.W',
    'WWWWWWWWWWWW'
]

world_map = set()
mini_map = set()
for j,row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE,j * TILE))
            mini_map.add((i * MAP_TILE, j * MAP_TILE))