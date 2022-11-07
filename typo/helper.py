#! /usr/bin/env python3
import random
import sys

# This program reads words from standard input, one per line.
# It then converts each letter to a key location with added Gaussian noise.
# It prints the key locations in the format expected by main.cpp.

QWERTY = (
    (0.25, 1.00), # A
    (4.75, 2.00), # B
    (2.75, 2.00), # C
    (2.25, 1.00), # D
    (2.00, 0.00), # E
    (3.25, 1.00), # F
    (4.25, 1.00), # G
    (5.25, 1.00), # H
    (7.00, 0.00), # I
    (6.25, 1.00), # J
    (7.25, 1.00), # K
    (8.25, 1.00), # L
    (6.75, 2.00), # M
    (5.75, 2.00), # N
    (8.00, 0.00), # O
    (9.00, 0.00), # P
    (0.00, 0.00), # Q
    (3.00, 0.00), # R
    (1.25, 1.00), # S
    (4.00, 0.00), # T
    (6.00, 0.00), # U
    (3.75, 2.00), # V
    (1.00, 0.00), # W
    (1.75, 2.00), # X
    (5.00, 0.00), # Y
    (0.75, 2.00)  # Z
)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sigma', type=float, default=0.25)
    parser.add_argument('input-file', nargs='?')
    args = parser.parse_args()

    for line in sys.stdin:
        line = line.lower().strip()
        for c in line:
            if 'a' <= c <= 'z':
                point = QWERTY[ord(c) - 97]
                x = point[0] + random.gauss(0, args.sigma)
                y = point[1] + random.gauss(0, args.sigma)
                print('%.5f %.5f ' % (x, y), end=' ')
        print('', flush=True)
