from graph import Graph
from dfa_generator import DFA_Generator
import json

data = json.load(open('nfa_2b.json'))
start = data["start"]
accepting = data["accepting"]
transitions = data["transitions"]

nfa = Graph(start, accepting, transitions)
dfa = DFA_Generator(nfa)

#dfa.get_epsilon_reaches("fq")
dfa.incremental_subset_algo()
print("DFA generated from NFA using incremental subset algorithm.")
print("DFA states: {}".format(dfa.dfa_q))
print("The number of reachable DFA states is {}.".format(len(dfa.dfa_q)))

