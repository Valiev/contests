from helpers import input_filepath
from pprint import pprint

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


def cmp_graph_pos(graph, from_node, to_node):
    def dfs(n1, n2):
        if n1 not in graph:
            return False
        if n2 in graph[n1]:
            return True
        return any(
            dfs(k, n2)
            for k in graph[n1]
        )
    return dfs(from_node, to_node)


def fix_seq(graph, seq):
    N = len(seq)
    print('fixing seq', seq)
    for pos in range(N):
        print('- pos:', pos)
        cmp_pos = pos + 1
        while cmp_pos < N:
            print(cmp_pos)
            if cmp_graph_pos(graph, seq[pos], seq[cmp_pos]):
                cmp_pos += 1
            else:
                print(seq, "switching", seq[pos], seq[cmp_pos])
                seq[pos], seq[cmp_pos] = seq[cmp_pos], seq[pos]
                cmp_pos = pos + 1
    return seq


def prep_data(filename):
    with open(filename) as fp:
        input_data = fp.read()
    graph_data, seq_data = input_data.split('\n\n')
    graph = build_graph(graph_data)
    seqs = [
        [int(i) for i in line.split(',')]
        for line in seq_data.splitlines()
    ]
    return graph, seqs


def puzzle1(filename):
    graph, seqs = prep_data(filename)
    return sum(
        seq[len(seq)//2]
        for seq in seqs
        if check_seq(graph, seq)
    )


def puzzle2(filename):
    graph, seqs = prep_data(filename)
    # pprint(graph)
    return sum(
        fix_seq(graph, seq)[len(seq)//2]
        for seq in seqs
        if not check_seq(graph, seq)
    )


if __name__ == "__main__":
    input_file = input_filepath("day05.txt")
    result1 = puzzle1(input_file)
    print(result1)
    result2 = puzzle2(input_file)
    print(result2)
