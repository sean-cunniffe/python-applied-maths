import random


def generate_set():
    result = set()
    for i in range(random.randint(10, 15)):
        result.add(random.randint(0, 20))
    return result


def print_sets(local_sets: dict):
    value: str = ''
    for set_value in local_sets.values():
        value += str(set_value) + '\n'
    return value


def union(local_sets: dict):
    temp_set: set = set()
    for set_value in local_sets.values():
        temp_set = temp_set.union(set_value)
    return temp_set


def intersection(local_sets: dict):
    temp_set: set = next(iter(local_sets.items()))[1]
    for set_value in local_sets.values():
        temp_set = temp_set.intersection(set_value)
    return temp_set


def main2():
    print('Random Set Generator')
    a = generate_set()
    b = generate_set()
    c = generate_set()
    the_sets = {'A': a, 'b': b, 'c': c}
    print(print_sets(the_sets))
    print('Union ', str(union(the_sets)))
    print('Intersection ', str(intersection(the_sets)))
    a.clear()
    b.clear()
    c.clear()


if __name__ == '__main__':
    main2()
