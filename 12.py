import random
tasks = random.sample([(x, y) for x in range(2, 9) for y in range(x, 9)], 15)
print('\n'.join('{} * {} = {}'.format(x, y, x*y) for x, y in tasks))