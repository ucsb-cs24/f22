#! /usr/bin/env python3

import math
import random

# A lot of values are hard-coded for simplicity...
# You can edit the most interesting ones at the bottom of the file.

STATION_ID = 0
def station_id():
    global STATION_ID
    STATION_ID += 1
    return STATION_ID

LINE_ID = 0
def line_id():
    global LINE_ID
    LINE_ID += 1
    return LINE_ID

class Line:
    def __init__(self, name, train):
        self.name  = name
        self.train = train
        self.stops = []


def loop(number, train, times, stations):
    name = 'Train ' if train else 'Bus '
    line = Line(name + str(number), train)
    time = 0

    for station in stations:
        time += random.choice(times)
        line.stops.append((time, station))
    time += random.choice(times)
    line.stops.append((time, stations[0]))
    return line


def braid(N, K):
    stations = ['Station %d' % i for i in range(1, N + 1)]

    for i in range(1, K + 1):
        line = Line('Train %d' % i, True)
        time = 0

        random.shuffle(stations)
        for station in stations:
            time += random.randrange(150, 251)
            line.stops.append((time, station))
        time += random.randrange(150, 251)
        line.stops.append((time, stations[0]))

        yield line


def chess(M, N):
    if M > 26:
        raise Exception('M must be 26 or smaller.')

    for m in range(M):
        time = 0
        c    = chr(65 + m)
        line = Line('Line ' + c, True)
        for n in range(1, N + 1):
            station = c + str(n)
            time   += random.randrange(7, 14)
            line.stops.append((time, station))
        yield line

    for n in range(1, N + 1):
        time = 0
        line = Line('Bus ' + str(n), False)
        for m in range(M):
            station = chr(65 + m) + str(n)
            time   += random.randrange(7, 14)
            line.stops.append((time, station))
        yield line


def cities(ncities, nstops, nlines):
    allstations = []

    for c in range(1, ncities + 1):
        stations = ['Station %d-%d' % (c, s) for s in range(1, nstops + 1)]
        visited  = set()

        for l in range(1, nlines + 1):
            random.shuffle(stations)
            train  = random.random() >= 0.25
            number = '%d-%d' % (c, l)
            yield loop(number, train, range(20, 40), stations[::5])
            visited.update(stations[::5])

        allstations.append(sorted(visited))

    for c1 in range(ncities):
        for c2 in range(c1):
            if random.random() < 0.5:
                continue

            line  = Line('Express ' + str(line_id()), True)

            stop  = random.choice(allstations[c1])
            time  = random.randrange(700, 1300)
            line.stops.append((time, stop))

            stop  = random.choice(allstations[c2])
            time += random.randrange(700, 1300)
            line.stops.append((time, stop))

            yield line


def grid(M, N):
    for m in range(1, M + 1):
        time = 0
        line = Line('Train ' + str(m), True)
        for n in range(1, N + 1):
            station = 'Station %d-%d' % (m, n)
            time   += random.randrange(75, 126)
            line.stops.append((time, station))
        yield line

    for n in range(1, N + 1):
        time = 0
        line = Line('Bus ' + str(n), False)
        for m in range(1, M + 1):
            station = 'Station %d-%d' % (m, n)
            time   += random.randrange(75, 126)
            line.stops.append((time, station))
        yield line


def loops(M, N, n, p):
    time = 0
    def station(i, j):
        return 'Station %d-%d' % (i, j)

    for l in range(1, n + 1):
        train = random.random() >= p
        stops = []

        imin, imax = sorted(random.sample(range(M), k=2))
        jmin, jmax = sorted(random.sample(range(N), k=2))

        for i in range(imin, imax):
            stops.append(station(i, jmin))
        for j in range(jmin, jmax):
            stops.append(station(imax, j))
        for i in range(imax, imin, -1):
            stops.append(station(i, jmax))
        for j in range(jmax, jmin, -1):
            stops.append(station(imin, j))

        yield loop(l, train, range(80, 121), stops)


def p2p(npoints, nlines, p):
    def point(i):
        return (
            i,
            100 * random.random(),
            100 * random.random(),
        )

    points = [point(i) for i in range(1, npoints + 1)]
    for i in range(1, nlines + 1):
        train = random.random() >= p
        type  = 'Train ' if train else 'Bus '
        line  = Line(type + str(i), train)

        src, dst = random.sample(points, k=2)
        line.stops.append((0, 'Station ' + str(src[0])))

        dx = src[1] - dst[1]
        dy = src[2] - dst[2]
        t  = int(10 * math.sqrt(dx*dx + dy*dy)) + 4
        line.stops.append((t, 'Station ' + str(dst[0])))

        yield line

def perc(width, height, p, q):
    line  = None
    time  = 0
    index = 1

    def magic(x1, y1, x2, y2):
        nonlocal line
        nonlocal index

        r = random.random()
        if r < q:
            # No connection
            if line:
                yield line
                line  = None
            return
        elif r < p + q:
            # Bus connection
            if line and line.train is False:
                line.stops.append((time, 'Station %d-%d' % (x2, y2)))
                return
            elif line:
                yield line
        else:
            # Train connection
            if line and line.train is True:
                line.stops.append((time, 'Station %d-%d' % (x2, y2)))
                return
            elif line:
                yield line

        index += 1
        train  = r >= p + q
        ltype  = 'Train ' if train else 'Bus '
        line   = Line(ltype + str(index), train)
        line.stops.append((0,    'Station %d-%d' % (x1, y1)))
        line.stops.append((time, 'Station %d-%d' % (x2, y2)))

    for x in range(1, width + 1):
        for y in range(1, height):
            time += random.choice(range(80, 121))
            yield from magic(x, y, x, y + 1)

    for y in range(1, height + 1):
        for x in range(1, width):
            time += random.choice(range(80, 121))
            yield from magic(x, y, x + 1, y)


def subtree(parent, current, branches, level):
    if parent:
        train = random.random() < 0.9 ** level
        name  = 'Train ' if train else 'Bus '
        line  = Line(name + str(line_id()), train)

        delta = 50 * level
        time  = random.randrange(100, delta + 100)
        line.stops.append((time, parent))

        time += random.randrange(100, delta + 100)
        line.stops.append((time, current))

        yield line

    if level <= 1:
        return

    for i in range(1, branches + 1):
        child = current + '.' + str(i)
        yield from subtree(current, child, branches, level - 1)


def tree(branches, levels):
    yield from subtree(None, 'Station 1', branches, levels)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--method', required=True, help='generation method')
    parser.add_argument('-o', '--outfile',               help='write output to a file')
    parser.add_argument('-s', '--seed',   type=int,      help='random seed')
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    if args.method == 'braid':
        generator = braid(100, 3)
    elif args.method == 'chess':
        generator = chess(8, 8)
    elif args.method == 'cities':
        generator = cities(88, 444, 6)
    elif args.method == 'grid':
        # Used for the Chessboard test
        generator = grid(160, 160)
    elif args.method == 'loops':
        generator = loops(222, 222, 222, 0.22)
    elif args.method == 'p2p':
        generator = p2p(10000, 50000, 0.1)
    elif args.method == 'perc':
        generator = perc(200, 200, 0.4, 0.1)
    elif args.method == 'tree':
        generator = tree(8, 6)
    else:
        raise Exception('Unknown generation method: ' + args.method)

    for route in generator:
        print('%s: %s' % (('TRAIN' if route.train else 'BUS'), route.name))
        for time, station in route.stops:
            print('- %d\t%s' % (time, station))
        print('')
