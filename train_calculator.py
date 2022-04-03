import re
from collections import defaultdict
from xml.sax.handler import all_properties

class TrainCalculator:

    def __init__(self, graph: str):
        """
        Generate a 2-dimensional dictionary, where every `dict[stationA][stationB]`
        represents the distance between stationA and stationB.
        """
        self.graph = defaultdict(dict)
        for start, end, distance in re.findall(r'([A-Z])([A-Z])(\d+)', graph):
            self.graph[start][end] = int(distance)
    
    def distance_between_stops(self, stops):
        """
        Method to calculate the distance between a list of stops.
        """
        # If only one station remains, return 0.
        if len(stops) <= 1:
            return 0
        
        # Check if `next_station` is reachable from `current_station`.
        current_station = stops[0]; next_station = stops[1]
        if next_station in self.graph[current_station]:
            output = self.distance_between_stops(stops=stops[1:])

            # Check if an error or value should be returned.
            return output if isinstance(output, str) else self.graph[current_station][next_station] + output
        else:
            return 'NO SUCH ROUTE'

    def shortest_distance(self, start, end, visited=set()):
        """
        Method to calculate the distance between the station `start` and the station `end`.
        """
        # If there exists a path between `start` and `end`, return the distance between them.
        if end in self.graph[start]:
            return self.graph[start][end]

        # If no path exists, return -1.
        if start in visited:
            return -1

        # Generate all the possible path lengths recursively, performing a breadth-first
        # search of all possible stations reachable from `start`.
        possible_lengths = [ self.graph[start][new_start] + self.shortest_distance(new_start, end, visited | {start}) 
                             for new_start in self.graph[start] ]
        return min(possible_lengths) if possible_lengths else -1

    def all_paths(self, start, max_length, diff):
        """
        Method to generate a list of all paths from a starting point.
        `diff` is used as a difference function such that the method can be reused for multiple purposes.
        """
        # Add all the stations reachable of the current station to the list `all_paths`.`
        all_paths = []
        for new_start in self.graph[start]:
            if max_length >= diff(start, new_start):
                # Add all the paths reachable from the next station to `all_paths`.
                all_paths.append(new_start)
                all_paths.extend(self.all_paths(new_start, max_length-diff(start, new_start), diff))

        # For every path, add the current station to the representation.
        return [ start + path for path in all_paths ]

    def paths_of_max_stops(self, start, end, max_stops):
        """
        Method to generate all possible paths from a start station to an end station, with a maximum number of stops.
        The difference function is `lambda *_: 1` such that the number of stops decreases by one w/ every iteration.
        """
        return [ path for path in self.all_paths(start, max_stops, lambda *_: 1)
                 if path[0] == start and path[-1] == end ]
    
    def paths_of_exactly_stops(self, start, end, max_stops):
        """
        Method to generate all possible paths from a start station to an end station, with a maximum number of stops.
        The difference function is `lambda *_: 1` such that the number of stops decreases by one w/ every iteration.
        """
        return [ path for path in self.all_paths(start, max_stops, lambda *_: 1)
                 if path[0] == start and path[-1] == end and len(path) == max_stops+1 ]

    def paths_of_max_length(self, start, end, max_length):
        """
        Method to generate all possible paths from a start station to an end station, with a distance less than `max_length`.
        The difference function is `lambda x, y:self.graph[x][y]` such that the maximum distance decreases by
        the distance between the current station and the next station.
        """
        return [ path for path in self.all_paths(start, max_length-1, lambda x, y:self.graph[x][y])
                 if path[0] == start and path[-1] == end ]