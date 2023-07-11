from itertools import permutations, repeat


def is_stable_matching(men_preferences, women_preferences, current_partner, current_partner_man):
    for woman in current_partner:
        current_man = current_partner[woman]
        for man in women_preferences[woman]:
            if man == current_man:
                break  # No need to continue checking lower preferences
            for woman2 in men_preferences[man]:
                if woman2 == current_partner_man[man]:
                    break
                if woman2 == woman:
                    """print("-----------")
                    print("Better match: " + man + " - " + woman)
                    print("-----------")"""
                    return False  # Unstable matching found
    return True  # All matchings are stable

# Example usage
men_preferences = {
    'x1': ['y1', 'y2', 'y3', 'y4'],
    'x2': ['y2', 'y1', 'y3', 'y4'],
    'x3': ['y2', 'y3', 'y1', 'y4'],
    'x4': ['y4', 'y1', 'y2', 'y3']
}

women_preferences = {
    'y1': ['x4', 'x3', 'x2', 'x1'],
    'y2': ['x1', 'x3', 'x2', 'x4'],
    'y3': ['x4', 'x3', 'x2', 'x1'],
    'y4': ['x2', 'x3', 'x1', 'x4']
}


def print_permutations():
    male = ['x1', 'x2', 'x3', 'x4']
    female = ['y1', 'y2', 'y3', 'y4']
    count = 0
    count2 = 0
    for p in permutations(female):
        count2 += 1
        male_female_dict = dict(zip(male, p))
        female_male_dict = dict(zip(p, male))
        print("Aktuelle Permutation: " + str(count2))
        for m, f in zip(male, p):
            print("{" + m, ",", f + "}")

        result = is_stable_matching(men_preferences, women_preferences, female_male_dict, male_female_dict)
        if result:
            count += 1
            print("Matching is stable.")
        else:
            print("Matching is not stable.")
        print("--------------------------")
    print()
    print("FINAL RESULT:")
    print("Stable Matchings: " + str(count))


print_permutations()

