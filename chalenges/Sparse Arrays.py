def matchingStrings(strings, queries):
    results = []
    for q in queries:
        arr = []
        for x in strings:
            if x == q:
                arr.append(x)
        results.append(len(arr))
    return results


matchingStrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc'])
