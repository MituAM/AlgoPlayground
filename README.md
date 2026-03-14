# AlgoPlayground

**AlgoPlayground** is an interactive command‑line application that demonstrates mastery of fundamental algorithm design paradigms: graph algorithms, greedy algorithms, divide and conquer, dynamic programming, and network flow. It provides a hands‑on environment to run algorithms, view correctness proofs, analyze theoretical and experimental running times, and receive well‑argued algorithmic advice.

## Features

- **Five algorithm categories** – each with classic, efficiently implemented algorithms.
- **Correctness proofs** – concise mathematical arguments (invariants, induction, exchange arguments) displayed for every algorithm.
- **Complexity analysis** – theoretical time and space complexity shown alongside each run.
- **Experimental timing** – measure execution time on user‑provided or random inputs.
- **Benchmarking** – test how runtime scales with input size for selected algorithms.
- **Algorithmic advice** – answer simple questions about your problem to get a reasoned recommendation.
- **User‑friendly menu** – navigate through categories, input data, and view results.

## Algorithms Included

| Category          | Algorithms                                                                                     |
|-------------------|------------------------------------------------------------------------------------------------|
| Graph             | Dijkstra (shortest path), Bellman‑Ford (negative weights), Floyd‑Warshall (all‑pairs), Kruskal (MST) |
| Greedy            | Activity Selection, Fractional Knapsack                                                        |
| Divide & Conquer  | Merge Sort, Quick Sort                                                                         |
| Dynamic Programming | 0/1 Knapsack, Longest Common Subsequence (LCS)                                               |
| Network Flow      | Edmonds‑Karp (max flow)                                                                        |

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository or download the `algoplayground.py` file.
2. Run the script from your terminal:

   ```bash
   python algoplayground.py

## Usage

The main menu offers three options:

1. Run a specific algorithm

  -Choose a category, then an algorithm.

  -Input data as prompted (edges, arrays, items, etc.).

  -View the result, correctness proof, complexity, and execution time.

2. Benchmark an algorithm

  -Select an algorithm and enter a list of input sizes.

  -The program generates random data of each size and reports the measured runtime.

  -Ideal for observing empirical growth rates (e.g., O(n log n) vs O(n²)).

3. Get algorithmic advice

  -Answer a few questions about your problem (data type, constraints, etc.).

  -Receive a clear, reasoned suggestion for the most suitable algorithm.
