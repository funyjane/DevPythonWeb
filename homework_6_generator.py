#generator

def num_generator(start):
    while start > 0:
        yield start
        start = start + 1
        if start % 3 == 0:
            yield 'Vasily'

num_generator(1)