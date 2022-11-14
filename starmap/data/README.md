# StarMap Data

This folder contains sample data that you can feed into your StarMap, as well as
a generator script that you can use to create large test cases of your own.

Generated files can get big.  Don't check them into Git!


## Simple Test Cases

- **Eight**  Eight stars, one at the center of each 1x1 octant.

- **Cube**  Twenty-seven stars: all possible cobimations of coordinates +1, 0, and -1.


## Generated Test Cases

- **Central**  All coordinates are normally distributed, resulting in a star
  cluster that's densest around the origin.

- **Disk**  Coordinates are normally distributed, but one axis has a much
  smaller standard distribution than the others, resulting in a disk shape.

- **Shell**  Stars are uniformly distributed on the surface of a sphere with
  radius 1.0.

- **Uniform**  Coordinates are uniformly distributed in the interval (-1, +1).
