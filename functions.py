def convert_to_binary(num):
    binary = bin(num).split('b')[1]
    binary = (8 - len(binary)) * '0' + binary
    return binary


def calculate_state(prev, state, next, rule):
    binary = prev + state + next
    rule_set = convert_to_binary(rule)[::-1]

    return rule_set[int(binary, 2)]


def step(current_state, rule):
    next_state = []

    for i in range(0, len(current_state)):
        if i == 0:
            prev = current_state[len(current_state) - 1]
            state = current_state[i]
            next = current_state[i + 1]
        elif i == len(current_state) - 1:
            prev = current_state[i - 1]
            state = current_state[i]
            next = current_state[0]
        else:
            prev = current_state[i - 1]
            state = current_state[i]
            next = current_state[i + 1]

        next_state.append(calculate_state(prev, state, next, rule))

    return next_state

