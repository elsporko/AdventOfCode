# --- Day 2: I Was Told There Would Be No Math ---
# 
# The elves are running low on wrapping paper, and so they need to submit an
# order for more. They have a list of the dimensions (length l, width w, and
# height h) of each present, and only want to order exactly as much as
# they need.
# 
# Fortunately, every present is a box (a perfect right rectangular prism), which
# makes calculating the required wrapping paper for each gift a little easier:
# find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves
# also need a little extra paper for each present: the area of the smallest
# side.
# 
# For example:
# 
# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of
# wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
# 
# A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of
# wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
# 
# All numbers in the elves' list are in feet. How many total square feet of
# wrapping paper should they order?

paper=0
dim = {
    'l': 0,
    'w': 1,
    'h': 2
}

data_file = 'data/day2.txt'
with open(data_file, 'r') as file:
    data = file.readlines()

for d in data:
    lwh = d.split('x')
    lwh = list(map(int, lwh))

    lw = lambda : 2 * lwh[dim['l']] * lwh[dim['w']]
    wh = lambda : 2 * lwh[dim['w']] * lwh[dim['h']]
    hl = lambda : 2 * lwh[dim['h']] * lwh[dim['l']]
    min_area = lambda x, y: x * y

    sides = sorted(lwh)
    paper += lw() + wh() + hl() + min_area(sides[0], sides[1])

print(paper)
