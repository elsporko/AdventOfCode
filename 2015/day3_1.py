# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
#
# Santa is delivering presents to an infinite two-dimensional grid of houses.
#
# He begins by delivering a present to the house at his starting location, and
# then an elf at the North Pole calls him via radio and tells him where to move
# next. Moves are always exactly one house to the north (^), south (v), east (>),
# or west (<). After each move, he delivers another present to the house at his
# new location.
#
# However, the elf back at the north pole has had a little too much eggnog, and
# so his directions are a little off, and Santa ends up visiting some houses more
# than once. How many houses receive at least one present?
#
# For example:
#
# > delivers presents to 2 houses: one at the starting location, and one to the
# east.
#
# ^>v< delivers presents to 4 houses in a square, including twice to the house at
# his starting/ending location.
#
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2
# houses.

location = (0,0)
visited = []

# Add initial location to the list of visited homes
visited.append(location)

data_file = 'data/day3.txt'
with open(data_file, 'r') as file:
    data = file.read().rstrip()
    

# orientation defines which tuple value is affected (east/west vs north/south)
# value is the direction
loc_map = {
            '>' : {
                'orientation': 'eastwest',
                'value': 1,
            },
            '^' : {
                'orientation': 'northsouth',
                'value': 1,
            },
            '<' : {
                'orientation': 'eastwest',
                'value': -1,
            },
            'v' : {
                'orientation': 'northsouth',
                'value': -1,
            }
        }

eastwest = 0
northsouth = 0
# Locations are represented as a list of tuples. 
for d in data[::]:
    if loc_map[d]['orientation'] == 'eastwest':
        eastwest += loc_map[d]['value']
    else:
        northsouth += loc_map[d]['value']

    location = (northsouth, eastwest)
    #location[loc_map[d]['orientation']] += loc_map[d]['value']

    if location not in visited:
        visited.append(location)

print (len(visited))
