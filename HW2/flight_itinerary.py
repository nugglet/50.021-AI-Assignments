# find a sequence of flights that departs from the starting city at the starting 
# time or later, and arrive at the destination city before the deadline time.

from cmath import inf
from utils import *
from search import *

class Flight():
    def __init__(self, start_city, start_time, end_city, end_time):
        self.start_city = start_city
        self.start_time = start_time
    
        self.end_city = end_city
        self.end_time = end_time

    def __str__(self):
        return str((self.start_city, self.start_time))+' -> ' + str((self.end_city, self.end_time))

    def matches(self, city, time):
        return (self.start_city == city and self.start_time >= time)

    __repr__ = __str__


flightDB = [Flight('Rome', 1, 'Paris', 4),
            Flight('Rome', 3, 'Madrid', 5),
            Flight('Rome', 5, 'Istanbul', 10),
            Flight('Paris', 2, 'London', 4),
            Flight('Paris', 5, 'Oslo', 7),
            Flight('Paris', 5, 'Istanbul', 9),
            Flight('Madrid', 7, 'Rabat', 10),
            Flight('Madrid', 8, 'London', 10),
            Flight('Istanbul', 10, 'Constantinople', 10)]

class FlightProblem(Problem):
    def __init__(self, initial, goal):
        # initial and goal are states which are a tuple of (city, time)
        self.initial = initial; self.goal = goal

    def actions(self, state):
        # check if there is a flight from current state at current time
        flights = []
        city = state[0]
        time = state[1]

        for i in range(len(flightDB)):
            f = flightDB[i]
            if f.matches(city, time):
                flights.append((f.end_city, f.end_time))
        return flights

    def result(self, state, action):
        return action

    def goal_test(self, state):
        return (state[0] == self.goal[0] and state[1] <= self.goal[1])

    def path_cost(self, c, state1, action, state2):
        # Calculates total flight time from state1 to state2
        return state2[1] - state1[1] + c

    def h():
        # specifies heuristic for A* search
        return
        
    
def find_itinerary(start_city, start_time, end_city, deadline):
    # uses iterative deepening search (dls with cutoff)
    # returns a list of cities and times, otherwise returns a string
    problem = FlightProblem((start_city, start_time), (end_city, deadline))

    try:
        path = iterative_deepening_search(problem).solution() # returns list of states
        path.insert(0, problem.initial)
    except AttributeError:
        return 'No flights found.'    
    return path

def find_shortest_itinerary(start_city, start_time, end_city):
    deadline = 1
    while True:
        path = find_itinerary(start_city, start_time, end_city, deadline)
        if type(path) == list:
            return path

        deadline += 1

def challenge(start_city, start_time, end_city):
    # get list of flights to end city
    valid_end =  [f for f in flightDB if f.end_city == end_city]
    for f in valid_end:
        # find a path to the end city at diff times
        path = find_itinerary(start_city, start_time, end_city, f.end_time)
        if type(path) == list:
            return path


if __name__=='__main__':
    print('Part 3: ' + str(find_itinerary('Rome', 1, 'Constantinople', 15)))
    print('Part 4: ' + str(find_shortest_itinerary('Rome', 1, 'Constantinople')))
    print('Part 5: ' + str(challenge('Rome', 1, 'London')))


##################################### Outputs: ########################################
# Part 3: [('Rome', 1), ('Istanbul', 10), ('Constantinople', 10)]
# Part 4: [('Rome', 1), ('Istanbul', 10), ('Constantinople', 10)]
# Part 5: [('Rome', 1), ('Madrid', 5), ('London', 10)]
#######################################################################################