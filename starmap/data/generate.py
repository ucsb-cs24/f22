#! /usr/bin/env python3

import random
import math


def central(n):
    for _ in range(n):
        x = random.gauss(0.0, 0.25)
        y = random.gauss(0.0, 0.25)
        z = random.gauss(0.0, 0.25)
        yield x, y, z

def disk(n, axis=0):
    for _ in range(n):
        x = random.gauss(0.0, 0.03)
        y = random.gauss(0.0, 0.25)
        z = random.gauss(0.0, 0.25)

        coords = [x, y, z]
        yield tuple(coords[axis:] + coords[:axis])

def shell(n):
    # Generate random Gaussians, then normalize
    # https://math.stackexchange.com/a/1585996
    for _ in range(n):
        x = random.gauss(0.0, 1.0)
        y = random.gauss(0.0, 1.0)
        z = random.gauss(0.0, 1.0)

        d  = math.sqrt(x*x + y*y + z*z)
        d += random.gauss(0.0, 0.01)

        yield x/d, y/d, z/d

def uniform(n):
    for _ in range(n):
        x = 1.0 - 2.0 * random.random()
        y = 1.0 - 2.0 * random.random()
        z = 1.0 - 2.0 * random.random()
        yield x, y, z


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--axis',   default=0,     type=int)
    parser.add_argument('-n', '--number', required=True, type=int)
    parser.add_argument('-m', '--method', required=True)
    parser.add_argument('-s', '--seed',   type=int)
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    if args.method == 'central':
        stars = central(args.number)
    elif args.method == 'disk':
        stars = disk(args.number, args.axis)
    elif args.method == 'shell':
        stars = shell(args.number)
    elif args.method == 'uniform':
        stars = uniform(args.number)
    else:
        print('Unknown method: ' + args.method)

    for star in stars:
        print('%f\t%f\t%f' % star)
