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

  def get_epsilon_reaches(self, state):
    queue = [state]
    visited = set()
    visited.add(state)
    reachable = set()

    while queue:
      p = queue.pop(0)
      #print("Full state string: {}".format(p))
      for current_state in p:
       # print("state string: {}".format(current_state))
       #current_state = queue.pop(0)
        if "epsilon" in self.nfa.transitions[current_state]:
          ereach = self.nfa.transitions[current_state]["epsilon"]
          #print("within epsilon reach: {}".format(ereach))
          for e in ereach:
            if e not in visited:
              queue.append(e)
              visited.add(e)
            reachable.add(e)
    
    self.epsilon_reaches[state] = reachable
    #print("Generated epsilon reaches for state [{}]: {}".format(state, reachable))


  def incremental_subset_algo(self):
    queue = [self.nfa.start_state]
    visited = set()
    visited.add(self.nfa.start_state)

    while queue:
      state = queue.pop(0)
      #print("CURRENT STATE: {}".format(state))
      
      self.dfa_q.append(state)

      if state not in self.epsilon_reaches:
        self.get_epsilon_reaches(state)
      epsilon_reach = self.epsilon_reaches[state]
      self.dfa_epsilon_reach.append(epsilon_reach)

      zero_reachable = set()
      for e in epsilon_reach:
        if "0" in self.nfa.transitions[e]:
          for zero_reach in self.nfa.transitions[e]["0"]: 
            zero_reachable.add(zero_reach)
      self.dfa_transition_0.append(zero_reachable)

      one_reachable = set()
      for e in epsilon_reach:
        if "1" in self.nfa.transitions[e]:
          for one_reach in self.nfa.transitions[e]["1"]: 
            one_reachable.add(one_reach)
      self.dfa_transition_1.append(one_reachable)

      zero_state =  "".join(zero_reachable) 
      if zero_state not in visited and zero_state is not '':
        queue.append(zero_state)
        visited.add(zero_state)

      one_state =  "".join(one_reachable) 
      if one_state not in visited and one_state is not '':
        queue.append(one_state)
        visited.add(one_state)






      
      

      


    
