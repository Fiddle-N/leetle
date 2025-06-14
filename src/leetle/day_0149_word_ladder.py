import itertools
from collections import defaultdict, deque
from dataclasses import dataclass


@dataclass
class Item:
    dist: int
    curr_word: str
    seen: set[str]


def change_no(word_1, word_2):
    changes = 0
    for char_a, char_b in zip(word_1, word_2):
        if char_a != char_b:
            changes += 1
    return changes


def is_short_transformation(word_1, word_2):
    return change_no(word_1, word_2) == 1


def transform_graph(begin_word, word_list):
    full_list = [begin_word] + word_list
    graph = defaultdict(list)
    for word_1, word_2 in itertools.combinations(full_list, 2):
        if not is_short_transformation(word_1, word_2):
            continue
        graph[word_1].append(word_2)
        if word_2 != begin_word:
            graph[word_2].append(word_1)
    return graph


def bfs(graph, begin_word, end_word):
    q = deque([Item(dist=1, curr_word=begin_word, seen=set([begin_word]))])
    while True:
        if not q:
            return 0
        item = q.popleft()
        for next_word in graph[item.curr_word]:
            if next_word in item.seen:
                continue
            dist = item.dist + 1
            if next_word == end_word:
                return dist
            seen = item.seen.copy()
            seen.add(next_word)
            q.append(Item(dist, curr_word=next_word, seen=seen))


def solve(begin_word, end_word, word_list):
    if begin_word == end_word:
        return 1
    graph = transform_graph(begin_word, word_list)
    return bfs(graph, begin_word, end_word)
