from helpers import input_filepath

example = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def build_graph(data):
    graph = dict()
    for line in data.splitlines():
        if not line:
            continue
        l, r = [int(i) for i in line.split('|')]
        value = graph.get(l, [])
        value.append(r)
        graph[l] = value
    return graph


def resolve_graph(graph):
    num_keys = len(graph)

    def dfs(key, step):
        print(key, step)
        if key not in graph:
            return True
        if step > num_keys:
            return False
        return all(
            dfs(next_key, step+1)
            for next_key in graph[key]
        )

    return all(dfs(k, 0) for k in graph)


def check_seq(graph, seq):
    prev_num = None
    for next_num in seq:
        if prev_num is None:
            prev_num = next_num
            continue
        if prev_num not in graph:
            raise Exception('WT?F')
            return False
        if next_num not in graph[prev_num]:
            return False
        prev_num = next_num
    return True


def puzzle1(filename):
    with open(filename) as fp:
        input_data = fp.read()
    graph_data, seq_data = input_data.split('\n\n')
    graph = build_graph(graph_data)
    seqs = [
        [int(i) for i in line.split(',')]
        for line in seq_data.splitlines()
    ]
    return sum(
        seq[len(seq)//2]
        for seq in seqs
        if check_seq(graph, seq)
    )


if __name__ == "__main__":
    input_file = input_filepath("day05.txt")
    result1 = puzzle1(input_file)
    print(result1)
