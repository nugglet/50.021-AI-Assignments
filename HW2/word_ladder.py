
from utils import *
from search import *
import string

## load valid words into set
WORDS = set(i.lower().strip() for i in open('words2.txt'))

def is_valid_word(word):
    return word in WORDS

class WordLadder(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.word_length = len(initial)
    
    def actions(self, state):
        
        if state == self.goal:
            return [self.goal]
        else:
            # get possible changes to next valid word
            # For each letter in word:
            # 1. if letter is the same as goal in that index, skip
            # 2. else replace with a letter in the alphabet iteratively and check validity
            queue = []
            for i in range(self.word_length):
                if state[i] == self.goal[i]:
                    continue
                for letter in string.ascii_lowercase:
                    new_word = state[:i] + letter + state[i+1:]
                    if is_valid_word(new_word):
                        queue.append(new_word)
        return queue

    def result(self, state, action):
        return action
    
    def goal_test(self, state):
        return super().goal_test(state)

    def path_cost(self, c, state1, action, state2):
        return super().path_cost(c, state1, action, state2)


def transform_word(problem, algo):
    try:
        if algo == 'bfts':
            actions = breadth_first_tree_search(problem).solution()        
        elif algo == 'bfs':
            actions = breadth_first_search(problem).solution()
                       
        if actions != "":
            print("initial state:'{}'".format(str(problem.initial)) + " -> "
                      + "actions:{}".format(actions))
            
    except AttributeError:
        print("initial state:'{}'".format(str(problem.initial)) + " -> unable to find any solution")

if __name__ == '__main__':
    
    test_cases = [("cars", "cats"), ("cold", "warm"), ("best", "math")]
    algos = ['bfs', 'bfts']

    for method in algos:
        print("Searching Algorithm: " + str(method))
        for case in test_cases:        
            transform_word(WordLadder(case[0],case[1]), method)


##################################### Outputs: ########################################
# Searching Algorithm: bfs
# initial state:'cars' -> actions:['cats']
# initial state:'cold' -> actions:['cord', 'word', 'ward', 'warm']
# initial state:'best' -> actions:['bast', 'mast', 'mash', 'math']
# Searching Algorithm: bfts
# initial state:'cars' -> actions:['cats']
# initial state:'cold' -> actions:['cord', 'word', 'ward', 'warm']
# initial state:'best' -> actions:['bast', 'mast', 'mash', 'math']
#######################################################################################