import collections

def matchingStrings(strings, queries):
    strings = collections.Counter(strings)
    frequency = list()
    for query in queries:
         counts = strings[query]
         frequency.append(counts)
    return(frequency)

if __name__ == '__main__':
    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print('\n'.join(map(str, res)))
