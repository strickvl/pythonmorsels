def add(m1: list[list], m2: list[list]) -> list[list]:
    result = []
    for idx1, val1 in enumerate(m1):
        sub_val = [val2 + m2[idx1][idx2] for idx2, val2 in enumerate(val1)]
        result.append(sub_val)
    return result
