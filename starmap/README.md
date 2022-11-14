# StarMap

You've been attacked by space pirates!  You were able to teleport away,  but you
had to make the jump at random, and now you're... somewhere.  But where?

Fortunately, you have a StarMap. You can get your spaceship's coordinates within
the galaxy from IgPS (the Intergalactic Positioning System) and enter those into
your StarMap.  It'll tell you the locations of some nearby star systems, and you
can head to a suitable  star for repairs.  Now if you could just  get this thing
working...


## Your Assignment

- Implement the `StarMap` class described in `StarMap.h`.
- You **may** use container classes from the standard library.
- Make sure you don't print anything that isn't explicitly allowed.
- Make sure you don't have any memory leaks.
- Make your program run as fast as possible.


### Star Data

When your StarMap starts,  it reads in star data  from a TSV file.  Each line of
this file contains three floating-point values, separated by tabs. These are the
X, Y, and Z coordinates of a star.  Each star also has an implicit ID: the first
star in the file has ID 1, the second star has ID 2, and so on. There is no star
with ID 0, and there are no stars with negative IDs.

There will never be more than one billion (1,000,000,000) stars in any file, and
the overwhelming majority of the star coordinates will be between -1.0 and 1.0.


### Functions

Implement the required `StarMap` functions in `StarMap.cpp`.

- `create(stream)` creates a `StarMap` from an input file stream.  It will
  probably just call your constructor.
- `find(n, x, y, z)` returns a vector containing the `n` closest stars to the
  point `(x, y, z)`.  This vector is sorted, with the star at index zero being
  the closest star to the input point.


## Challenge Labs

This is a challenge lab, and the rules are a little different:

- You may work in pairs if you choose to.  If you do, make sure you add both
  partners' names every time you submit to Gradescope.
- To get full credit, you need to generate the correct output and also run at
  least as fast as the "baseline" solution.
- The three fastest solutions will get extra credit: fifteen points for first
  place, ten points for second place, and five points for third place.  All
  group members get the full bonus.


## Hints

- First make it work.  Then make it fast.
- Space is big.  You just won't believe how vastly, hugely, mind-bogglingly big
  it is.  I mean, you may think it's a long way down the road to the chemist's,
  but that's just peanuts to space.
