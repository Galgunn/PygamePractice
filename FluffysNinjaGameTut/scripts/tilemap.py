'''
There is 2 types of positions
- grid pos:String = 3;10
- pixel pos:tuple = (50, 50)

to get grid pos you must divide and turn into an int
    (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))

to get pixel pos you must multiply
    (gridpos[0] * TILE_SIZE, gridpos[1] * TILE_SIZE)
'''

import pygame

# tiles around the player or entity
NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
# a set of tiles that have physics 
PHYSICS_TILES = {'grass', 'stone'}

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}

    '''
    Finds tiles around pos 

    Returns:
        List of dicts corresponding to a tile that are near a pos
    '''
    def tiles_around(self, pos) -> list:
        tiles = [] # list of tiles dict that are around the players pos
        # Turn the player pixel pos into a tuple thats easy to work with a grid pos
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS: # Get the tuple in NEIGHBOR_OFFSETS
            # Adds tuples tile_loc and offset and turns it to a str to get grid pos
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            # Check to see if check_loc(grid pos) is equal to a key in self.tilemap (grid pos)
            if check_loc in self.tilemap:
                # Adds the value (tile dict) corresponding to the key (grid pos), to tiles list
                tiles.append(self.tilemap[check_loc])
        return tiles
    
    '''
    Get rects near a pos

    Returns:
        A list of rects
    '''
    def physics_rects_around(self, pos) -> list:
        rects = [] # Rects that with collision
        # Check to see if theres a tile dict in the list
        for tile in self.tiles_around(pos):
            # Check to see if the tile is a part of the PHYSICS_TILE set
            if tile['type'] in PHYSICS_TILES:
                # Create and add a rect object of the tile to rects
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects

    def render(self, surf, offset=(0, 0)):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))
            
        # loc is the key or grid pos in tilemap dict: {'3;10': {'type': 'grass', 'variant': 1, 'pos': (3, 10)}
        for loc in self.tilemap:
            # Get the value and return a dict of a tile: {'type': 'grass', 'variant': 1, 'pos': (3, 10)}
            tile = self.tilemap[loc]
            # We can use those keys and values in tile to find the specific asset we want to use and where to place it
            # For example: surf.blit(self.game.assets[tile['grass']][tile[1]], (tile['pos'][0]=3 * self.tile_size, tile['pos'][1]=10 * self.tile_size))
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))