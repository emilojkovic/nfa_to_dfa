from graph import Graph
from dfa_generator import DFA_Generator
import json
import sys

# sets input and output files
in_file = open(sys.argv[1], 'r')
out_file = open("dfa_output.txt", 'w')

#parses input NFA json to create an NFA graph
data = json.load(in_file)
start = data["start"]
accepting = data["accepting"]
transitions = data["transitions"]
nfa = Graph(start, accepting, transitions)

# creates DFA Generator based on NFA graph
dfa = DFA_Generator(nfa)

# runs Incremental Subset Algorithm on NFA to produce DFA
dfa.incremental_subset_algo()

# writes resulting DFA in output file
out_file.write("DFA generated from NFA in [{}] using incremental subset algorithm.\n\n".format(sys.argv[1]))
states = dfa.dfa_q
num_states = len(dfa.dfa_q)

e_reach = dfa.dfa_epsilon_reach
transition_0 = dfa.dfa_transition_0
transition_1 = dfa.dfa_transition_1

out_file.write("The number of reachable DFA states is {}.\n".format(num_states))
out_file.write("\n")

for i in range(num_states):
  out_file.write("DFA states: {}\n".format(states[i]))
  out_file.write("---------- e reach: {}\n".format(e_reach[i]))
  out_file.write("----- transition 0: {}\n".format(transition_0[i]))
  out_file.write("----- transition 1: {}\n".format(transition_1[i]))
  out_file.write("\n")

