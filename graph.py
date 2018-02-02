class Graph:
  def __init__(self, in_start_state, in_end, in_transitions):
    self.start_state = in_start_state
    self.end_states = in_end
    self.transitions = in_transitions