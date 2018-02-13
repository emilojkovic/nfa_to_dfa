class DFA_Generator:
  def __init__(self, graph):
    self.nfa = graph
    self.epsilon_reaches = {}

    # representing dfa table as 5 independent lists for each column
    self.dfa_q = []
    self.dfa_epsilon_reach = []
    self.dfa_transition_0 = []
    self.dfa_transition_1 = []
    self.dfa_accepting = []

  '''
  Input:      a state in our DFA (representing a set of NFA states)
  Output:     None

  Uses BFS to find every node within a node's epsilon reach
  (including itself and nodes that are more than one epsilon
  transition away)
  '''
  def get_epsilon_reaches(self, dfa_state):
    queue = [dfa_state]
    visited = set()
    visited.add(dfa_state)
    reachable = set()

    while queue:
      nfa_states = queue.pop(0)
     
      # iterates through set of NFA states that represents a DFA state
      for state in nfa_states:
        if "epsilon" in self.nfa.transitions[state]:
          # get all states reachable via epsilon transitions
          ereach = self.nfa.transitions[state]["epsilon"]
          for reachable_state in ereach:
            if reachable_state not in visited:
              queue.append(reachable_state)
              visited.add(reachable_state)
            reachable.add(reachable_state)
    
    self.epsilon_reaches[dfa_state] = reachable
    #print("Generated epsilon reaches for state [{}]: {}".format(dfa_state, reachable))


  '''
  Input:      None
  Output:     None

  Uses Incremental Subset Algorithm to generate all DFA states 
  and transision given an NFA
  '''
  def incremental_subset_algo(self):
    queue = [self.nfa.start_state]
    visited = set()
    visited.add(self.nfa.start_state)

    while queue:
      state = queue.pop(0)
      self.dfa_q.append(state)

      if state not in self.epsilon_reaches: 
        self.get_epsilon_reaches(state)
      epsilon_reach = self.epsilon_reaches[state]
      self.dfa_epsilon_reach.append(epsilon_reach)

      # finding all nodes reachable with "0" transition from NFA nodes in DFA state
      zero_reachable = set()
      for e in epsilon_reach:
        if "0" in self.nfa.transitions[e]:
          for zero_reach in self.nfa.transitions[e]["0"]: 
            zero_reachable.add(zero_reach)
      self.dfa_transition_0.append(zero_reachable)

      # finding all nodes reachable with "1" transition from NFA nodes in DFA state 
      one_reachable = set()
      for e in epsilon_reach:
        if "1" in self.nfa.transitions[e]:
          for one_reach in self.nfa.transitions[e]["1"]: 
            one_reachable.add(one_reach)
      self.dfa_transition_1.append(one_reachable)

      # creates new DFA state with string of all NFA nodes from zero reach
      zero_state =  "".join(zero_reachable) 
      if zero_state not in visited and zero_state is not '':
        queue.append(zero_state)
        visited.add(zero_state)
      
      # creates new DFA state with string of all NFA nodes from one reach
      one_state =  "".join(one_reachable) 
      if one_state not in visited and one_state is not '':
        queue.append(one_state)
        visited.add(one_state)