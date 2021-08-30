def compact(iterable):
    if len(iterable) == 0:
        return []
    result = [iterable[0]]
    previous_val = result[0]
    for val in iterable[1:]:
        if val != previous_val:
            result.append(val)
            previous_val = val
    return result
