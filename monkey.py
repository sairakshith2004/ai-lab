
class State:
    def __init__(self, monkey, box, banana):
        self.monkey = monkey  # Position of the monkey
        self.box = box        # Position of the box
        self.banana = banana  # Position of the banana

    def __str__(self):
        return f"Monkey: {self.monkey}, Box: {self.box}, Banana: {self.banana}"

def push_box(state):
    if not state.box and not state.monkey:
        return State(state.monkey, True, state.banana)
    return state

def climb_box(state):
    if state.box and not state.monkey:
        return State(True, state.box, state.banana)
    return state

def grab_banana(state):
    if state.monkey and state.banana:
        print("Banana grabbed!")
        return State(state.monkey, state.box, True)
    return state

def monkey_banana_problem():
    initial_state = State(False, False, False)
    print("Initial State:", initial_state)

    state = push_box(initial_state)
    print("After pushing the box:", state)

    state = climb_box(state)
    print("After climbing the box:", state)

    state = grab_banana(state)

if __name__ == "__main__":
    monkey_banana_problem()
        
