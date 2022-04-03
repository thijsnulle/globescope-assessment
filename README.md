# GlobeScope Assessment
This repository contains the solution for both programming problems given
to me to solve. I know, it says in the first line that I could one of the problems
but chaotic me assumed both problems needed to be solved and I was enjoying it
so I just did both.

## Problem 1: Trains
For this problem, I created the `TrainCalculator` class which would handle all the
information given for this problem, structure it correctly and perform the actions in
the most concise way possible. I opted for not using classes for the stations as a 
graph can be nicely represented in a Python using a 2-dimensional dictionary, where
every station-station keys pair represents the distance between the given stations.
As more than half of the functions needed a function to generate all paths and filter
them based on some conditions, I wrote the method `all_paths` that generates all paths
from a given starting station. This method takes a lambda that represents a difference
function such that the method can be used for generating paths with a maximum length
and a maximum number of stops.

I assumed that all inputs were valid representations of a graph, thus I did not do any
input vaidation.

### Running the code
The code can be run by creating an instance of the `TrainCalculator` class, which takes
a string of stations and their distance, represented as `[A-Z][A-Z]\d+`. Once you created
this instance, you can call all the function according with their parameters and it returns
a distance for the distance functions and a list of all the possible paths with the path
functions.

There are also tests associated with the class, which can be found in `train_calculator_test.py`,
which can be run using Python3.10 (and I think lower versions but I don't really know).

## Problem 2: Mars Rovers
For this problem, I created two classes; the `MarsMission` and the `MarsRover` object. As the
input can be a list of mars rovers, I created a class that handles all instances of the
`MarsRover` objects. The `MarsMission` only parses the input data and creates the `MarsRover`
objects and it contains a method to execute the instruction for every `MarsRover`. For the
`MarsRover` object, I created an enum which represents the current direction of the `MarsRover`
and its movement if the move function gets called, besides that, the class contains an `_update_direction`
method which will update the direction based on the next rotation and its current direction.
Then it contains the method `perform_instructions`, which performs all the instructions which
were provided for the given `MarsRover`.

I assumed that all inputs were valid representation of a list mars rovers and their given
instructions list. Also, I assumed that all inputs would not cause the `MarsRover` to leave
the grid, so I disregarded the input grid, as no information was given about what should
happen in that given case.

### Running the code
The code can be run by creating an instance of the `MarsMission` class, which takes
a string of mars rovers and their instructions, represented as `\d+ \d+ [NESW]\n[LRM]+`.
Once you created this instance, you can call the `execute_instructions` method, which will
return the final positions of all `MarsRover` objects of the current mars mission.

There are also tests associated with the class, which can be found in `mars_rover_test.py`,
which can be run using Python3.10 (and I think lower versions but I don't really know).
