# Omnibus

Alice hates trains.  She travels a lot,  and always takes public transportation,
but she really hates trains.  This makes her trip planning rather unusual: she's
not concerned with  how long the trip takes  or how much it costs.  Instead, she
always picks a route that will get her to her destination having spent as little
time as possible on trains.

Right now, Alice plans out all her routes by hand.  But as her travels grow more
and more ambitious,  this ends up taking a significant amount of time.  Help her
out by writing an Atlas program that finds low-train-time routes automatically.


## Your Assignment

- Implement the `Atlas` class described in `Atlas.h`.
- You **may** use container classes from the standard library.
- Make sure you don't print anything that isn't explicitly allowed.
- Make sure you don't have any memory leaks.
- Make your program run as fast as possible.


### Functions

Implement the following Atlas functions in `Atlas.cpp`.

- The `create(stream)` function reads in transit line data and creates an Atlas.
  The input file format is described below.
- The `route(src, dst)` function returns a `Trip` describing the best way to
  get from station `src` to station `dst` along the lines listed in the Atlas.
  The "best" route is one that spends the least total time on trains.  If many
  routes tie for the least train time, all of them are acceptable outputs.  If
  there is no route, throw a `std::runtime_error` with the message `No route.`


### Input Format

Your Atlas should read route data from text files.  These files will always be
formatted as follows:

- Some input lines will be empty, or start with a `#` character.  Ignore these.
- Some input lines will start with either `BUS: ` or `TRAIN: `, followed by the
  name of a bus or train.  These define new public transit lines.
- Each of the previous input lines will be followed by two or more input lines
  listing the stations along the transit line.  Each of these input lines will
  start with `- `, followed by a non-negative integer, followed by whitespace,
  followed by the name of a station.  The numbers themselves don't matter; the
  differences between them tell you how long it takes to get between stations.

```
BUS: Line 15X
# This route is a loop!
- 7   North Hall
- 16  Santa Catalina Hall
- 21  Storke & Hollister
- 50  SBCC
- 69  North Hall

TRAIN: Pacific Surfliner
- 11  San Luis Obispo
- 169 Santa Barbara
- 370 Los Angeles
- 544 San Diego
```

You can get on a line at any stop and get off at any stop. In the example above,
you can go from North Hall to Santa Catalina Hall in 9 minutes.  You can go from
Santa Barbara to San Diego in 375 minutes.

All routes are bidirectional.  You can get from Storke & Hollister to North Hall
in 14 minutes.

Some lines form loops. You can go from SBCC to Santa Catalina Hall in 28 minutes
via North Hall; it would take 34 minutes via Storke & Hollister. Loop lines will
always have the same first and last station.  This is the only case in which the
same station will appear multiple times on a line.

All transit line names are unique.


### Output Format

The `Trip.h` file defines the `Trip` structure you'll use to represent a result.

- The `start` variable holds the name of the station you start at.
- The `legs` variable holds a vector describing each leg of the trip, in order:
  - The `line` variable holds the name of the transit line you take.
  - The `stop` variable holds the name of the station you get off at. The `stop`
    of the final leg should be the name of your destination station.

The same `line` should never appear on two consecutive legs.  If you take a line
through multiple stations, only list the final station:

```
Start at San Luis Obispo
 - Pacific Surfliner to San Diego
```

The same line may appear on multiple legs in other situations:

```
Start at San Luis Obispo
 - Pacific Surfliner to Santa Barbara
 - Coast Starlight to Los Angeles
 - Pacific Surfliner to San Diego
```


## Challenge Labs

This is a challenge lab, and the rules are a little different:

- You may work in pairs if you choose to.  If you do, make sure you add both
  partners' names every time you submit to Gradescope.
- To get full credit, you need to generate correct output and also run at least
  as fast as the "baseline" solution.
- The three fastest solutions will get extra credit: fifteen points for first
  place, ten points for second place, and five points for third place.  All
  group members get the full bonus.


## Hints

- You can use the `std::ws` helper from the `iomanip` header to consume extra
  whitespace from `std::istream`s.
- Although intermediate stations aren't allowed in the final output, they can be
  very helpful when debugging.
