import collections

def contacts(queries):
    data = list()
    result = list()
    for operation, name in queries:
        if operation == 'add':
            while len(data) < len(name):
                data.append(collections.defaultdict(lambda: set()))
            for i, c in enumerate(name):
                data[i][c].add(name)
        elif operation == 'find':
            if len(name) > len(data):
                # There is no name stored of that length
                result.append(0)
                continue
            current = None
            for i, c in enumerate(name):
                if i == 0:
                    current = data[i][c]
                else:
                    current = current.intersection(data[i][c])
            result.append(len(current))
    return result


if __name__ == '__main__':
    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    print('\n'.join(map(str, result)))
    print('\n')
