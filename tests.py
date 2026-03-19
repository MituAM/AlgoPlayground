import pytest
import random
from algoplayground import (
    dijkstra, bellman_ford, floyd_warshall, kruskal,
    activity_selection, fractional_knapsack,
    merge_sort, quick_sort,
    knapsack_01, lcs,
    edmonds_karp
)

# ---------------------------- Graph Algorithms ----------------------------

def test_dijkstra_simple():
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 1), ('D', 5)],
        'C': [('D', 8)],
        'D': []
    }
    dist, prev = dijkstra(graph, 'A')
    assert dist['A'] == 0
    assert dist['B'] == 4
    assert dist['C'] == 2
    assert dist['D'] == 9
    assert prev['D'] == 'B'
    assert prev['B'] == 'A'

def test_dijkstra_disconnected():
    graph = {'A': [('B', 1)], 'B': [], 'C': []}
    dist, prev = dijkstra(graph, 'A')
    assert dist['C'] == float('inf')
    assert prev['C'] is None

def test_bellman_ford_no_negative_cycle():
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 1), ('D', 5)],
        'C': [('D', 8)],
        'D': []
    }
    dist, prev, neg_cycle = bellman_ford(graph, 'A')
    assert not neg_cycle
    assert dist['D'] == 9

def test_bellman_ford_negative_weights():
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', -3)],  # negative edge
        'C': [('D', 2)],
        'D': []
    }
    dist, prev, neg_cycle = bellman_ford(graph, 'A')
    assert not neg_cycle
    assert dist['D'] == 3

def test_bellman_ford_negative_cycle():
    graph = {
        'A': [('B', 1)],
        'B': [('C', -2)],
        'C': [('A', -1)]
    }
    dist, prev, neg_cycle = bellman_ford(graph, 'A')
    assert neg_cycle

def test_floyd_warshall():
    graph = {
        'A': [('B', 3), ('C', 8)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    dist, vertices, neg_cycle = floyd_warshall(graph)
    assert not neg_cycle
    idx = {v: i for i, v in enumerate(vertices)}
    assert dist[idx['A']][idx['D']] == 6

def test_kruskal():
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    mst, total = kruskal(edges, 4)
    assert total == 19
    assert len(mst) == 3
    mst_set = {(min(u,v), max(u,v), w) for u,v,w in mst}
    expected = {(2,3,4), (0,3,5), (0,1,10)}
    assert mst_set == expected

# ---------------------------- Greedy Algorithms ----------------------------

def test_activity_selection():
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    selected = activity_selection(activities)
    expected = [(1,4), (5,7), (8,11), (12,16)]
    assert selected == expected

def test_activity_selection_empty():
    assert activity_selection([]) == []

def test_fractional_knapsack():
    items = [(60, 10), (100, 20), (120, 30)]
    capacity = 50
    total_val, fractions = fractional_knapsack(items, capacity)
    assert total_val == 240.0
    assert len(fractions) == 3
    assert fractions[0][1] == 1.0
    assert fractions[1][1] == 1.0
    assert abs(fractions[2][1] - 20/30) < 1e-9

def test_fractional_knapsack_exact_capacity():
    items = [(10, 5), (20, 5)]
    capacity = 10
    total_val, fractions = fractional_knapsack(items, capacity)
    assert total_val == 30.0
    assert all(f == 1.0 for _, f in fractions)

# ---------------------------- Divide & Conquer ----------------------------

def test_merge_sort():
    assert merge_sort([]) == []
    assert merge_sort([5]) == [5]
    assert merge_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    assert merge_sort([9, 8, 7, 6]) == [6, 7, 8, 9]

def test_quick_sort():
    assert quick_sort([]) == []
    assert quick_sort([5]) == [5]
    assert quick_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    assert quick_sort([9, 8, 7, 6]) == [6, 7, 8, 9]

# ---------------------------- Dynamic Programming ----------------------------

def test_knapsack_01():
    items = [(60, 10), (100, 20), (120, 30)]
    capacity = 50
    max_val, selected = knapsack_01(items, capacity)
    assert max_val == 220
    assert set(selected) == {1, 2}

def test_knapsack_01_no_items():
    max_val, selected = knapsack_01([], 10)
    assert max_val == 0
    assert selected == []

def test_lcs():
    X = "ABCBDAB"
    Y = "BDCAB"
    length, lcs_str = lcs(X, Y)
    assert length == 4
    assert lcs_str in ["BCAB", "BDAB"]

def test_lcs_empty():
    assert lcs("", "ABC") == (0, "")
    assert lcs("ABC", "") == (0, "")

# ---------------------------- Network Flow ----------------------------

def test_edmonds_karp():
    cap = {
        's': {'a': 10, 'c': 8},
        'a': {'b': 5, 'c': 2},
        'b': {'t': 7},
        'c': {'b': 10, 't': 10},
        't': {}
    }
    flow, resid = edmonds_karp(cap, 's', 't')
    assert flow == 15

def test_edmonds_karp_disconnected():
    cap = {'s': {'a': 5}, 'a': {}, 't': {}}
    flow, resid = edmonds_karp(cap, 's', 't')
    assert flow == 0
