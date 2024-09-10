# AI-assign-1
AI assignment 1

## Team Members

- Jyotin Goel (B22AI063)


## Table of Contents
1. [Synthetic Data Generation](#synthetic-data-generation)
    - [Purpose](#purpose)
    - [Methodology](#methodology)
2. [Algorithms](#algorithms)
    - [IDDFS](#iddfs)
    - [UCS](#ucs)
    - [A* Search](#a-search)
    - [Greedy Search](#greedy-search)
3. [Experiments](#experiments)
4. [Citations](#citations)


## Synthetic Vocabulary Generation and Transition Matrix Generation
### Purpose
The purpose is to generate real synthetic data, to test out our approaches, trying to see if our search is able to also take care of things like grammar, syntax, etc in the searches, which heuristic functions allows us to do so.

### Methodology
My methodology is pretty simple we follow a step by step approach

#### Step 1: Generate a 500 word Essay or copy it from a book, etc.

#### Step 2: Make a vocabulary out of the 500 word essay, using nltk to first preprocess the text, and then save it to `vocab.txt` file.
Preprocessing involves:
- Getting the strings to lowercase
- Using NLTK's `punkt_tab` to further word tokenize our essay to get our vocabulary.

#### Step 3: Now that we have our Vocabulary of Words, we try to calculate the transition matrix for that essay.
Here we calculate the probabilities for our words in the vocabulary

Let us setup some pre requisities:

P(Wk | Wi) = (Count of Wk following Wi) / (Total Number of words following Wi)

For example: 

THe sentence "electricity is crucial"

"electricity", "is", "crucial"

Transition Matrix May be something like this:

|                | electricity |   is   | crucial |
|----------------|-------------|--------|---------|
| **electricity**|     0       |   1.0  |    0    |
| **is**         |     0       |   0    |   1.0   |
| **crucial**    |     0       |   0    |    0    |


## Algorithms

### IDDFS
Iterative Deepening Depth-First Search (IDDFS) in a probabilistic manner repeatedly explores paths to a fixed depth, incrementally increasing the limit. It balances depth-first exploration with breadth-first thoroughness, progressively examining paths based on their probability until finding the most likely path, combining efficiency with completeness in uncertain environments.(Is also claimed to be somewhat similar to BFS + DFS)

### UCS
Uniform Cost Search (UCS) in a probabilistic context selects paths based on cumulative probability costs, exploring the least costly path first. It ensures the most probable route is expanded before others, guaranteeing an optimal solution by considering all possible paths and their associated probabilities, focusing on overall path likelihood rather than immediate gains.

### Greedy Search
The greedy approach in a probabilistic manner involves selecting the option with the highest immediate probability of success at each step. This strategy maximizes the likelihood of short-term gains, assuming local optimal choices lead to global optimality, but may not always find the best overall solution due to its shortsighted nature.

### A* Search Algorithm
In A* search we have taken the heuristic function as the negative log likelihood of the probability of the edges.Logarithms also make it easier to work with very small or very large values because they scale them down, making the optimization process more stable.Thus leading me to use this.

To prove the admissibility of the negative log likelihood of probability as a heuristic function in an A* search, we'll need to show that this heuristic is optimistic, meaning it never overestimates the cost to reach the goal. Admissibility implies that for every node \( n \), the heuristic \( h(n) \) is less than or equal to the true cost \( h^*(n) \) from \( n \) to the goal. In the context of negative log likelihood, we'll show that this heuristic satisfies the admissibility criterion.

### Theoretical Basis
1. **Negative Log Likelihood and Probability:**
   - If \( p(n) \) is the probability associated with a certain event at node \( n \), the negative log likelihood is defined as:
     \[
     h(n) = -\log(p(n))
     \]
   - Since \( 0 \leq p(n) \leq 1 \), \( h(n) \geq 0 \), and as \( p(n) \) approaches 1, \( h(n) \) approaches 0.

2. **Admissibility:**
   - For \( h(n) \) to be admissible, it must satisfy:
     \[
     h(n) \leq h^*(n)
     \]
     where \( h^*(n) \) is the actual cost from \( n \) to the goal. In this context, the "cost" could be interpreted as the inverse likelihood of reaching the goal from node \( n \).

### Proof:
Let's consider a simple scenario with 5 nodes: \( A, B, C, D, G \), where \( G \) is the goal node.

#### Assign Probabilities:
- \( p(A) = 0.8 \)
- \( p(B) = 0.7 \)
- \( p(C) = 0.5 \)
- \( p(D) = 0.4 \)
- \( p(G) = 1.0 \) (since it's the goal, the probability of being at the goal when you're at the goal is 1)

#### Compute Negative Log Likelihood:
- \( h(A) = -log(0.8) approx 0.223 \)
- \( h(B) = -log(0.7) approx 0.357 \)
- \( h(C) = -log(0.5) = 0.693 \)
- \( h(D) = -log(0.4) approx 0.916 \)
- \( h(G) = -log(1.0) = 0 \)

#### Check Admissibility:
To check if the heuristic \( h(n) \) is admissible, compare it with the actual cost to the goal:

1. **Path \( A \to G \):**
   - \( h(A) \) should not overestimate the true cost to \( G \).
   - Since \( p(G) = 1 \), the cost is 0. \( h(A) = 0.223 \), which does not exceed the true cost (0), so it's admissible.

2. **Path \( B \to G \):**
   - \( h(B) = 0.357 \), which does not overestimate the true cost.

3. **Path \( C \to G \):**
   - \( h(C) = 0.693 \), still does not overestimate the true cost.

4. **Path \( D \to G \):**
   - \( h(D) = 0.916 \), also does not overestimate the true cost.

Since in each case, \( h(n) \) does not exceed the actual cost to the goal, the negative log likelihood function is admissible as a heuristic for A* search in this scenario.

## Experiments

### Experiment 1: With L=4, N=4

#### On Given vocab 

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 4 -n 4
```

Result is :

```bash
2024-09-09 22:48:10.210 | INFO     | __main__:build_transition:237 - Path exists
2024-09-09 22:48:10.217 | INFO     | __main__:build_vocab:246 - Path exists
2024-09-09 22:48:10.217 | INFO     | __main__:astar:255 - Starting Experiment: A* Search with L=4 and N=4
2024-09-09 22:48:10.228 | INFO     | __main__:astar:264 - Time taken: 0.01093912124633789
2024-09-09 22:48:10.228 | DEBUG    | __main__:astar:265 - <SoS> airport at grass grass <EoS>
2024-09-09 22:48:10.228 | INFO     | __main__:astar:266 - Score: 0.30834588448116296
2024-09-09 22:48:10.229 | INFO     | __main__:astar:267 - Total Nodes Explored: 1365
2024-09-09 22:48:10.229 | INFO     | __main__:greedy:288 - Starting Experiment: Greedy Search with L=4 and N=4
2024-09-09 22:48:10.229 | DEBUG    | __main__:greedy:299 - <SoS> green airport at grass <EoS>
2024-09-09 22:48:10.229 | INFO     | __main__:greedy:300 - Score: 0.74669852344255
2024-09-09 22:48:10.229 | INFO     | __main__:greedy:301 - Time taken: 8.749961853027344e-05
2024-09-09 22:48:10.229 | INFO     | __main__:greedy:302 - Total nodes Explored: 6
2024-09-09 22:48:10.229 | INFO     | __main__:iddfs:305 - Starting Experiment: IDDFS with L=4 and N=4
2024-09-09 22:48:10.231 | DEBUG    | __main__:iddfs:316 - <SoS> green airport at grass <EoS>
2024-09-09 22:48:10.231 | INFO     | __main__:iddfs:317 - Score: 0.6974164208953418
2024-09-09 22:48:10.232 | INFO     | __main__:iddfs:318 - Time taken: 0.0018548965454101562
2024-09-09 22:48:10.232 | INFO     | __main__:iddfs:319 - Total nodes Explored: 1702
2024-09-09 22:48:10.232 | INFO     | __main__:ucs:271 - Starting Experiment: Uniform Cost Search with L=4 and N=4
2024-09-09 22:48:10.233 | INFO     | __main__:ucs:281 - Time taken: 0.000989675521850586
2024-09-09 22:48:10.233 | DEBUG    | __main__:ucs:282 - <SoS> green airport at grass <EoS>
2024-09-09 22:48:10.233 | INFO     | __main__:ucs:283 - Score: 0.6974164208953418
2024-09-09 22:48:10.233 | INFO     | __main__:ucs:284 - Total Nodes Explored: 681
```

#### On synthetic generated vocab

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 4 -n 4
```

Results are as follows:

```bash
2024-09-09 22:50:29.589 | INFO     | __main__:build_transition:237 - Path exists
2024-09-09 22:50:29.595 | INFO     | __main__:build_vocab:246 - Path exists
2024-09-09 22:50:29.595 | INFO     | __main__:astar:255 - Starting Experiment: A* Search with L=4 and N=4
2024-09-09 22:50:29.606 | INFO     | __main__:astar:264 - Time taken: 0.01063394546508789
2024-09-09 22:50:29.606 | DEBUG    | __main__:astar:265 - <SoS> address accessible ac ac <EoS>
2024-09-09 22:50:29.606 | INFO     | __main__:astar:266 - Score: 0.30834588448116296
2024-09-09 22:50:29.607 | INFO     | __main__:astar:267 - Total Nodes Explored: 1365
2024-09-09 22:50:29.607 | INFO     | __main__:greedy:288 - Starting Experiment: Greedy Search with L=4 and N=4
2024-09-09 22:50:29.607 | DEBUG    | __main__:greedy:299 - <SoS> a address accessible ac <EoS>
2024-09-09 22:50:29.607 | INFO     | __main__:greedy:300 - Score: 0.74669852344255
2024-09-09 22:50:29.607 | INFO     | __main__:greedy:301 - Time taken: 9.560585021972656e-05
2024-09-09 22:50:29.607 | INFO     | __main__:greedy:302 - Total nodes Explored: 6
2024-09-09 22:50:29.608 | INFO     | __main__:iddfs:305 - Starting Experiment: IDDFS with L=4 and N=4
2024-09-09 22:50:29.610 | DEBUG    | __main__:iddfs:316 - <SoS> a address accessible ac <EoS>
2024-09-09 22:50:29.610 | INFO     | __main__:iddfs:317 - Score: 0.6974164208953418
2024-09-09 22:50:29.610 | INFO     | __main__:iddfs:318 - Time taken: 0.0019083023071289062
2024-09-09 22:50:29.610 | INFO     | __main__:iddfs:319 - Total nodes Explored: 1702
2024-09-09 22:50:29.610 | INFO     | __main__:ucs:271 - Starting Experiment: Uniform Cost Search with L=4 and N=4
2024-09-09 22:50:29.611 | INFO     | __main__:ucs:281 - Time taken: 0.0010228157043457031
2024-09-09 22:50:29.611 | DEBUG    | __main__:ucs:282 - <SoS> a address accessible ac <EoS>
2024-09-09 22:50:29.611 | INFO     | __main__:ucs:283 - Score: 0.6974164208953418
2024-09-09 22:50:29.611 | INFO     | __main__:ucs:284 - Total Nodes Explored: 681
```

#### Another Such Synthetic Generated Vocab and transition

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 4 -n 4
```

Results are as follows

```bash
2024-09-09 22:54:59.262 | INFO     | __main__:build_transition:237 - Path exists
2024-09-09 22:54:59.269 | INFO     | __main__:build_vocab:246 - Path exists
2024-09-09 22:54:59.270 | INFO     | __main__:astar:255 - Starting Experiment: A* Search with L=4 and N=4
2024-09-09 22:54:59.280 | INFO     | __main__:astar:264 - Time taken: 0.010546684265136719
2024-09-09 22:54:59.280 | DEBUG    | __main__:astar:265 - <SoS> also all alessandro alessandro <EoS>
2024-09-09 22:54:59.280 | INFO     | __main__:astar:266 - Score: 0.30834588448116296
2024-09-09 22:54:59.281 | INFO     | __main__:astar:267 - Total Nodes Explored: 1365
2024-09-09 22:54:59.281 | INFO     | __main__:greedy:288 - Starting Experiment: Greedy Search with L=4 and N=4
2024-09-09 22:54:59.281 | DEBUG    | __main__:greedy:299 - <SoS> affordable also all alessandro <EoS>
2024-09-09 22:54:59.281 | INFO     | __main__:greedy:300 - Score: 0.74669852344255
2024-09-09 22:54:59.281 | INFO     | __main__:greedy:301 - Time taken: 8.368492126464844e-05
2024-09-09 22:54:59.281 | INFO     | __main__:greedy:302 - Total nodes Explored: 6
2024-09-09 22:54:59.281 | INFO     | __main__:iddfs:305 - Starting Experiment: IDDFS with L=4 and N=4
2024-09-09 22:54:59.283 | DEBUG    | __main__:iddfs:316 - <SoS> affordable also all alessandro <EoS>
2024-09-09 22:54:59.284 | INFO     | __main__:iddfs:317 - Score: 0.6974164208953418
2024-09-09 22:54:59.284 | INFO     | __main__:iddfs:318 - Time taken: 0.0020394325256347656
2024-09-09 22:54:59.284 | INFO     | __main__:iddfs:319 - Total nodes Explored: 1702
2024-09-09 22:54:59.284 | INFO     | __main__:ucs:271 - Starting Experiment: Uniform Cost Search with L=4 and N=4
2024-09-09 22:54:59.285 | INFO     | __main__:ucs:281 - Time taken: 0.001035451889038086
2024-09-09 22:54:59.285 | DEBUG    | __main__:ucs:282 - <SoS> affordable also all alessandro <EoS>
2024-09-09 22:54:59.286 | INFO     | __main__:ucs:283 - Score: 0.6974164208953418
2024-09-09 22:54:59.286 | INFO     | __main__:ucs:284 - Total Nodes Explored: 681
```

### Experiment 2: With L=3

#### With N=3

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 3 -n 3
```

Result

```bash
2024-09-09 22:59:22.803 | INFO     | __main__:build_transition:237 - Path exists
2024-09-09 22:59:22.810 | INFO     | __main__:build_vocab:246 - Path exists
2024-09-09 22:59:22.811 | INFO     | __main__:astar:255 - Starting Experiment: A* Search with L=3 and N=3
2024-09-09 22:59:22.812 | INFO     | __main__:astar:264 - Time taken: 0.0010409355163574219
2024-09-09 22:59:22.812 | DEBUG    | __main__:astar:265 - <SoS> all alessandro alessandro <EoS>
2024-09-09 22:59:22.812 | INFO     | __main__:astar:266 - Score: 0.966648617907424
2024-09-09 22:59:22.812 | INFO     | __main__:astar:267 - Total Nodes Explored: 121
2024-09-09 22:59:22.812 | INFO     | __main__:greedy:288 - Starting Experiment: Greedy Search with L=3 and N=3
2024-09-09 22:59:22.812 | DEBUG    | __main__:greedy:299 - <SoS> all alessandro alessandro <EoS>
2024-09-09 22:59:22.812 | INFO     | __main__:greedy:300 - Score: 0.8914314580400001
2024-09-09 22:59:22.813 | INFO     | __main__:greedy:301 - Time taken: 7.557868957519531e-05
2024-09-09 22:59:22.813 | INFO     | __main__:greedy:302 - Total nodes Explored: 5
2024-09-09 22:59:22.813 | INFO     | __main__:iddfs:305 - Starting Experiment: IDDFS with L=3 and N=3
2024-09-09 22:59:22.813 | DEBUG    | __main__:iddfs:316 - <SoS> alessandro alessandro alessandro <EoS>
2024-09-09 22:59:22.813 | INFO     | __main__:iddfs:317 - Score: 0.7041744562256721
2024-09-09 22:59:22.813 | INFO     | __main__:iddfs:318 - Time taken: 0.00018215179443359375
2024-09-09 22:59:22.813 | INFO     | __main__:iddfs:319 - Total nodes Explored: 158
2024-09-09 22:59:22.813 | INFO     | __main__:ucs:271 - Starting Experiment: Uniform Cost Search with L=3 and N=3
2024-09-09 22:59:22.814 | INFO     | __main__:ucs:281 - Time taken: 0.00021076202392578125
2024-09-09 22:59:22.814 | DEBUG    | __main__:ucs:282 - <SoS> alessandro alessandro alessandro <EoS>
2024-09-09 22:59:22.814 | INFO     | __main__:ucs:283 - Score: 0.7041744562256721
2024-09-09 22:59:22.814 | INFO     | __main__:ucs:284 - Total Nodes Explored: 79
```

#### With N=4

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 3 -n 4
```

```bash
2024-09-09 23:00:03.423 | INFO     | __main__:build_transition:237 - Path exists
2024-09-09 23:00:03.430 | INFO     | __main__:build_vocab:246 - Path exists
2024-09-09 23:00:03.430 | INFO     | __main__:astar:255 - Starting Experiment: A* Search with L=3 and N=4
2024-09-09 23:00:03.433 | INFO     | __main__:astar:264 - Time taken: 0.0027544498443603516
2024-09-09 23:00:03.433 | DEBUG    | __main__:astar:265 - <SoS> all alessandro alessandro alessandro <EoS>
2024-09-09 23:00:03.433 | INFO     | __main__:astar:266 - Score: 0.9964894599184452
2024-09-09 23:00:03.433 | INFO     | __main__:astar:267 - Total Nodes Explored: 364
2024-09-09 23:00:03.434 | INFO     | __main__:greedy:288 - Starting Experiment: Greedy Search with L=3 and N=4
2024-09-09 23:00:03.434 | DEBUG    | __main__:greedy:299 - <SoS> all alessandro alessandro alessandro <EoS>
2024-09-09 23:00:03.434 | INFO     | __main__:greedy:300 - Score: 0.8652233731736242
2024-09-09 23:00:03.434 | INFO     | __main__:greedy:301 - Time taken: 7.62939453125e-05
2024-09-09 23:00:03.434 | INFO     | __main__:greedy:302 - Total nodes Explored: 6
2024-09-09 23:00:03.434 | INFO     | __main__:iddfs:305 - Starting Experiment: IDDFS with L=3 and N=4
2024-09-09 23:00:03.435 | DEBUG    | __main__:iddfs:316 - <SoS> alessandro alessandro alessandro alessandro <EoS>
2024-09-09 23:00:03.435 | INFO     | __main__:iddfs:317 - Score: 0.6834717272126373
2024-09-09 23:00:03.435 | INFO     | __main__:iddfs:318 - Time taken: 0.0006110668182373047
2024-09-09 23:00:03.435 | INFO     | __main__:iddfs:319 - Total nodes Explored: 482
2024-09-09 23:00:03.435 | INFO     | __main__:ucs:271 - Starting Experiment: Uniform Cost Search with L=3 and N=4
2024-09-09 23:00:03.436 | INFO     | __main__:ucs:281 - Time taken: 0.000408172607421875
2024-09-09 23:00:03.436 | DEBUG    | __main__:ucs:282 - <SoS> alessandro alessandro alessandro alessandro <EoS>
2024-09-09 23:00:03.436 | INFO     | __main__:ucs:283 - Score: 0.6834717272126373
2024-09-09 23:00:03.436 | INFO     | __main__:ucs:284 - Total Nodes Explored: 241
```

#### With N=5

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 3 -n 5
```

```bash
2024-09-09 23:00:27.017 | INFO     | __main__:build_transition:237 - Path exists
2024-09-09 23:00:27.024 | INFO     | __main__:build_vocab:246 - Path exists
2024-09-09 23:00:27.024 | INFO     | __main__:astar:255 - Starting Experiment: A* Search with L=3 and N=5
2024-09-09 23:00:27.033 | INFO     | __main__:astar:264 - Time taken: 0.009372472763061523
2024-09-09 23:00:27.034 | DEBUG    | __main__:astar:265 - <SoS> all alessandro alessandro alessandro alessandro <EoS>
2024-09-09 23:00:27.034 | INFO     | __main__:astar:266 - Score: 1.0263303019294665
2024-09-09 23:00:27.034 | INFO     | __main__:astar:267 - Total Nodes Explored: 1093
2024-09-09 23:00:27.034 | INFO     | __main__:greedy:288 - Starting Experiment: Greedy Search with L=3 and N=5
2024-09-09 23:00:27.034 | DEBUG    | __main__:greedy:299 - <SoS> all alessandro alessandro alessandro alessandro <EoS>
2024-09-09 23:00:27.034 | INFO     | __main__:greedy:300 - Score: 0.8397858060023197
2024-09-09 23:00:27.034 | INFO     | __main__:greedy:301 - Time taken: 8.296966552734375e-05
2024-09-09 23:00:27.034 | INFO     | __main__:greedy:302 - Total nodes Explored: 7
2024-09-09 23:00:27.035 | INFO     | __main__:iddfs:305 - Starting Experiment: IDDFS with L=3 and N=5
2024-09-09 23:00:27.036 | DEBUG    | __main__:iddfs:316 - <SoS> alessandro alessandro alessandro alessandro alessandro <EoS>
2024-09-09 23:00:27.036 | INFO     | __main__:iddfs:317 - Score: 0.6633776584325858
2024-09-09 23:00:27.036 | INFO     | __main__:iddfs:318 - Time taken: 0.0015003681182861328
2024-09-09 23:00:27.037 | INFO     | __main__:iddfs:319 - Total nodes Explored: 1454
2024-09-09 23:00:27.037 | INFO     | __main__:ucs:271 - Starting Experiment: Uniform Cost Search with L=3 and N=5
2024-09-09 23:00:27.038 | INFO     | __main__:ucs:281 - Time taken: 0.0010521411895751953
2024-09-09 23:00:27.038 | DEBUG    | __main__:ucs:282 - <SoS> alessandro alessandro alessandro alessandro alessandro <EoS>
2024-09-09 23:00:27.038 | INFO     | __main__:ucs:283 - Score: 0.6633776584325858
2024-09-09 23:00:27.038 | INFO     | __main__:ucs:284 - Total Nodes Explored: 727
```

#### With N=6

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 3 -n 6
```

```bash
2024-09-09 23:00:49.324 | INFO     | __main__:build_transition:237 - Path exists
2024-09-09 23:00:49.332 | INFO     | __main__:build_vocab:246 - Path exists
2024-09-09 23:00:49.332 | INFO     | __main__:astar:255 - Starting Experiment: A* Search with L=3 and N=6
2024-09-09 23:00:49.364 | INFO     | __main__:astar:264 - Time taken: 0.03197908401489258
2024-09-09 23:00:49.364 | DEBUG    | __main__:astar:265 - <SoS> all alessandro alessandro alessandro alessandro alessandro <EoS>
2024-09-09 23:00:49.365 | INFO     | __main__:astar:266 - Score: 1.0561711439404877
2024-09-09 23:00:49.365 | INFO     | __main__:astar:267 - Total Nodes Explored: 3280
2024-09-09 23:00:49.365 | INFO     | __main__:greedy:288 - Starting Experiment: Greedy Search with L=3 and N=6
2024-09-09 23:00:49.365 | DEBUG    | __main__:greedy:299 - <SoS> all alessandro alessandro alessandro alessandro alessandro <EoS>
2024-09-09 23:00:49.365 | INFO     | __main__:greedy:300 - Score: 0.8150961033058515
2024-09-09 23:00:49.365 | INFO     | __main__:greedy:301 - Time taken: 0.00010943412780761719
2024-09-09 23:00:49.365 | INFO     | __main__:greedy:302 - Total nodes Explored: 8
2024-09-09 23:00:49.366 | INFO     | __main__:iddfs:305 - Starting Experiment: IDDFS with L=3 and N=6
2024-09-09 23:00:49.372 | DEBUG    | __main__:iddfs:316 - <SoS> alessandro alessandro alessandro alessandro alessandro alessandro <EoS>
2024-09-09 23:00:49.372 | INFO     | __main__:iddfs:317 - Score: 0.6438743552746679
2024-09-09 23:00:49.372 | INFO     | __main__:iddfs:318 - Time taken: 0.0060389041900634766
2024-09-09 23:00:49.372 | INFO     | __main__:iddfs:319 - Total nodes Explored: 4370
2024-09-09 23:00:49.372 | INFO     | __main__:ucs:271 - Starting Experiment: Uniform Cost Search with L=3 and N=6
2024-09-09 23:00:49.376 | INFO     | __main__:ucs:281 - Time taken: 0.003313779830932617
2024-09-09 23:00:49.376 | DEBUG    | __main__:ucs:282 - <SoS> alessandro alessandro alessandro alessandro alessandro alessandro <EoS>
2024-09-09 23:00:49.376 | INFO     | __main__:ucs:283 - Score: 0.6438743552746679
2024-09-09 23:00:49.376 | INFO     | __main__:ucs:284 - Total Nodes Explored: 2185
```

### Experiment 3: With L=5

#### (Here, we are using a synthetic vocabulary taken from an essay)

#### With N=3

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 5 -n 3
```

Results are as follows

```bash
2024-09-09 23:13:05.609 | INFO     | __main__:build_transition:240 - Path exists
2024-09-09 23:13:05.622 | INFO     | __main__:build_vocab:254 - Path exists
2024-09-09 23:13:05.623 | INFO     | __main__:astar:263 - Starting Experiment: A* Search with L=5 and N=3
2024-09-09 23:13:05.624 | INFO     | __main__:astar:272 - Time taken: 0.0008752346038818359
2024-09-09 23:13:05.624 | DEBUG    | __main__:astar:273 - <SoS> also also also <EoS>
2024-09-09 23:13:05.624 | INFO     | __main__:astar:274 - Score: -1.5232379183429687
2024-09-09 23:13:05.624 | INFO     | __main__:astar:275 - Total Nodes Explored: 76
2024-09-09 23:13:05.624 | INFO     | __main__:greedy:296 - Starting Experiment: Greedy Search with L=5 and N=3
2024-09-09 23:13:05.625 | DEBUG    | __main__:greedy:307 - <SoS> alessandro all alternating <EoS>
2024-09-09 23:13:05.625 | INFO     | __main__:greedy:308 - Score: 1.3151147065540898
2024-09-09 23:13:05.625 | INFO     | __main__:greedy:309 - Time taken: 6.961822509765625e-05
2024-09-09 23:13:05.625 | INFO     | __main__:greedy:310 - Total nodes Explored: 5
2024-09-09 23:13:05.625 | INFO     | __main__:iddfs:313 - Starting Experiment: IDDFS with L=5 and N=3
2024-09-09 23:13:05.626 | DEBUG    | __main__:iddfs:324 - <SoS> alessandro alternating affordable <EoS>
2024-09-09 23:13:05.626 | INFO     | __main__:iddfs:325 - Score: 5.163739698391067
2024-09-09 23:13:05.626 | INFO     | __main__:iddfs:326 - Time taken: 0.0010645389556884766
2024-09-09 23:13:05.627 | INFO     | __main__:iddfs:327 - Total nodes Explored: 932
2024-09-09 23:13:05.627 | INFO     | __main__:ucs:279 - Starting Experiment: Uniform Cost Search with L=5 and N=3
2024-09-09 23:13:05.627 | INFO     | __main__:ucs:289 - Time taken: 0.0005054473876953125
2024-09-09 23:13:05.627 | DEBUG    | __main__:ucs:290 - <SoS> alessandro alternating affordable <EoS>
2024-09-09 23:13:05.627 | INFO     | __main__:ucs:291 - Score: 5.163739698391067
2024-09-09 23:13:05.627 | INFO     | __main__:ucs:292 - Total Nodes Explored: 311
```

#### With N=4

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 5 -n 4
```

Results are as follows

```bash
2024-09-09 23:15:40.953 | INFO     | __main__:build_transition:239 - Path exists
2024-09-09 23:15:40.966 | INFO     | __main__:build_vocab:253 - Path exists
2024-09-09 23:15:40.966 | INFO     | __main__:astar:262 - Starting Experiment: A* Search with L=5 and N=4
2024-09-09 23:15:40.970 | INFO     | __main__:astar:271 - Time taken: 0.004152059555053711
2024-09-09 23:15:40.970 | DEBUG    | __main__:astar:272 - <SoS> affordable affordable affordable affordable <EoS>
2024-09-09 23:15:40.971 | INFO     | __main__:astar:273 - Score: -4.260485239374628
2024-09-09 23:15:40.971 | INFO     | __main__:astar:274 - Total Nodes Explored: 577
2024-09-09 23:15:40.971 | INFO     | __main__:greedy:295 - Starting Experiment: Greedy Search with L=5 and N=4
2024-09-09 23:15:40.971 | DEBUG    | __main__:greedy:306 - <SoS> also affordable affordable affordable <EoS>
2024-09-09 23:15:40.971 | INFO     | __main__:greedy:307 - Score: 4.415595126446175
2024-09-09 23:15:40.971 | INFO     | __main__:greedy:308 - Time taken: 8.869171142578125e-05
2024-09-09 23:15:40.971 | INFO     | __main__:greedy:309 - Total nodes Explored: 6
2024-09-09 23:15:40.972 | INFO     | __main__:iddfs:312 - Starting Experiment: IDDFS with L=5 and N=4
2024-09-09 23:15:40.979 | DEBUG    | __main__:iddfs:323 - <SoS> all all all also <EoS>
2024-09-09 23:15:40.979 | INFO     | __main__:iddfs:324 - Score: 5.060414356345518
2024-09-09 23:15:40.979 | INFO     | __main__:iddfs:325 - Time taken: 0.00697636604309082
2024-09-09 23:15:40.979 | INFO     | __main__:iddfs:326 - Total nodes Explored: 4682
2024-09-09 23:15:40.979 | INFO     | __main__:ucs:278 - Starting Experiment: Uniform Cost Search with L=5 and N=4
2024-09-09 23:15:40.982 | INFO     | __main__:ucs:288 - Time taken: 0.0022890567779541016
2024-09-09 23:15:40.982 | DEBUG    | __main__:ucs:289 - <SoS> all all all also <EoS>
2024-09-09 23:15:40.982 | INFO     | __main__:ucs:290 - Score: 5.060414356345518
2024-09-09 23:15:40.982 | INFO     | __main__:ucs:291 - Total Nodes Explored: 1561
```

#### With N=5

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 5 -n 5
```

Results are as follows:

```bash
2024-09-09 23:16:09.296 | INFO     | __main__:build_transition:239 - Path exists
2024-09-09 23:16:09.310 | INFO     | __main__:build_vocab:253 - Path exists
2024-09-09 23:16:09.310 | INFO     | __main__:astar:262 - Starting Experiment: A* Search with L=5 and N=5
2024-09-09 23:16:09.311 | INFO     | __main__:astar:271 - Time taken: 0.0005178451538085938
2024-09-09 23:16:09.311 | DEBUG    | __main__:astar:272 - <SoS> alessandro alessandro alessandro alessandro alessandro <EoS>
2024-09-09 23:16:09.311 | INFO     | __main__:astar:273 - Score: -1.5349389335131844
2024-09-09 23:16:09.311 | INFO     | __main__:astar:274 - Total Nodes Explored: 28
2024-09-09 23:16:09.311 | INFO     | __main__:greedy:295 - Starting Experiment: Greedy Search with L=5 and N=5
2024-09-09 23:16:09.311 | DEBUG    | __main__:greedy:306 - <SoS> all alessandro alessandro alessandro alessandro <EoS>
2024-09-09 23:16:09.312 | INFO     | __main__:greedy:307 - Score: 2.62740795907676
2024-09-09 23:16:09.312 | INFO     | __main__:greedy:308 - Time taken: 7.724761962890625e-05
2024-09-09 23:16:09.312 | INFO     | __main__:greedy:309 - Total nodes Explored: 7
2024-09-09 23:16:09.312 | INFO     | __main__:iddfs:312 - Starting Experiment: IDDFS with L=5 and N=5
2024-09-09 23:16:09.355 | DEBUG    | __main__:iddfs:323 - <SoS> alessandro also alternating alternating alternating <EoS>
2024-09-09 23:16:09.355 | INFO     | __main__:iddfs:324 - Score: 6.162845710401048
2024-09-09 23:16:09.355 | INFO     | __main__:iddfs:325 - Time taken: 0.04262113571166992
2024-09-09 23:16:09.355 | INFO     | __main__:iddfs:326 - Total nodes Explored: 23432
2024-09-09 23:16:09.355 | INFO     | __main__:ucs:278 - Starting Experiment: Uniform Cost Search with L=5 and N=5
2024-09-09 23:16:09.367 | INFO     | __main__:ucs:288 - Time taken: 0.011492490768432617
2024-09-09 23:16:09.367 | DEBUG    | __main__:ucs:289 - <SoS> alessandro also alternating alternating alternating <EoS>
2024-09-09 23:16:09.367 | INFO     | __main__:ucs:290 - Score: 6.162845710401048
2024-09-09 23:16:09.367 | INFO     | __main__:ucs:291 - Total Nodes Explored: 7811
```

#### With N=6

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 5 -n 6
```

Results are as follows:

```bash
2024-09-09 23:16:52.661 | INFO     | __main__:build_transition:239 - Path exists
2024-09-09 23:16:52.674 | INFO     | __main__:build_vocab:253 - Path exists
2024-09-09 23:16:52.675 | INFO     | __main__:astar:262 - Starting Experiment: A* Search with L=5 and N=6
2024-09-09 23:16:52.690 | INFO     | __main__:astar:271 - Time taken: 0.014851808547973633
2024-09-09 23:16:52.690 | DEBUG    | __main__:astar:272 - <SoS> also affordable also affordable also affordable <EoS>
2024-09-09 23:16:52.690 | INFO     | __main__:astar:273 - Score: 1.6959558874695844
2024-09-09 23:16:52.690 | INFO     | __main__:astar:274 - Total Nodes Explored: 1510
2024-09-09 23:16:52.691 | INFO     | __main__:greedy:295 - Starting Experiment: Greedy Search with L=5 and N=6
2024-09-09 23:16:52.691 | DEBUG    | __main__:greedy:306 - <SoS> also affordable also affordable also affordable <EoS>
2024-09-09 23:16:52.691 | INFO     | __main__:greedy:307 - Score: 0.07761697631088385
2024-09-09 23:16:52.691 | INFO     | __main__:greedy:308 - Time taken: 0.00011682510375976562
2024-09-09 23:16:52.691 | INFO     | __main__:greedy:309 - Total nodes Explored: 8
2024-09-09 23:16:52.691 | INFO     | __main__:iddfs:312 - Starting Experiment: IDDFS with L=5 and N=6
2024-09-09 23:16:53.166 | DEBUG    | __main__:iddfs:323 - <SoS> all affordable affordable affordable also all <EoS>
2024-09-09 23:16:53.166 | INFO     | __main__:iddfs:324 - Score: 6.392597275178787
2024-09-09 23:16:53.167 | INFO     | __main__:iddfs:325 - Time taken: 0.4747812747955322
2024-09-09 23:16:53.167 | INFO     | __main__:iddfs:326 - Total nodes Explored: 117182
2024-09-09 23:16:53.167 | INFO     | __main__:ucs:278 - Starting Experiment: Uniform Cost Search with L=5 and N=6
2024-09-09 23:16:53.225 | INFO     | __main__:ucs:288 - Time taken: 0.05762672424316406
2024-09-09 23:16:53.225 | DEBUG    | __main__:ucs:289 - <SoS> all affordable affordable affordable also all <EoS>
2024-09-09 23:16:53.225 | INFO     | __main__:ucs:290 - Score: 6.392597275178787
2024-09-09 23:16:53.225 | INFO     | __main__:ucs:291 - Total Nodes Explored: 39061
```

### Experiment 4: With L=10

#### With N=3

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 10 -n 3
```

```bash
2024-09-09 23:17:37.587 | INFO     | __main__:build_transition:239 - Path exists
2024-09-09 23:17:37.601 | INFO     | __main__:build_vocab:253 - Path exists
2024-09-09 23:17:37.601 | INFO     | __main__:astar:262 - Starting Experiment: A* Search with L=10 and N=3
2024-09-09 23:17:37.613 | INFO     | __main__:astar:271 - Time taken: 0.011404275894165039
2024-09-09 23:17:37.613 | DEBUG    | __main__:astar:272 - <SoS> antiquity antiquity antiquity <EoS>
2024-09-09 23:17:37.613 | INFO     | __main__:astar:273 - Score: -3.2972192052127576
2024-09-09 23:17:37.613 | INFO     | __main__:astar:274 - Total Nodes Explored: 1758
2024-09-09 23:17:37.613 | INFO     | __main__:greedy:295 - Starting Experiment: Greedy Search with L=10 and N=3
2024-09-09 23:17:37.613 | DEBUG    | __main__:greedy:306 - <SoS> are antiquity antiquity <EoS>
2024-09-09 23:17:37.613 | INFO     | __main__:greedy:307 - Score: 7.9587346366731255
2024-09-09 23:17:37.614 | INFO     | __main__:greedy:308 - Time taken: 7.700920104980469e-05
2024-09-09 23:17:37.614 | INFO     | __main__:greedy:309 - Total nodes Explored: 5
2024-09-09 23:17:37.614 | INFO     | __main__:iddfs:312 - Starting Experiment: IDDFS with L=10 and N=3
2024-09-09 23:17:37.633 | DEBUG    | __main__:iddfs:323 - <SoS> affordable all alternating <EoS>
2024-09-09 23:17:37.633 | INFO     | __main__:iddfs:324 - Score: 11.534375030268869
2024-09-09 23:17:37.633 | INFO     | __main__:iddfs:325 - Time taken: 0.019104719161987305
2024-09-09 23:17:37.634 | INFO     | __main__:iddfs:326 - Total nodes Explored: 12212
2024-09-09 23:17:37.634 | INFO     | __main__:ucs:278 - Starting Experiment: Uniform Cost Search with L=10 and N=3
2024-09-09 23:17:37.637 | INFO     | __main__:ucs:288 - Time taken: 0.0033485889434814453
2024-09-09 23:17:37.637 | DEBUG    | __main__:ucs:289 - <SoS> affordable all alternating <EoS>
2024-09-09 23:17:37.637 | INFO     | __main__:ucs:290 - Score: 11.534375030268869
2024-09-09 23:17:37.637 | INFO     | __main__:ucs:291 - Total Nodes Explored: 2221
```

#### With N=4

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 10 -n 4
```

```bash
2024-09-09 23:18:03.838 | INFO     | __main__:build_transition:239 - Path exists
2024-09-09 23:18:03.851 | INFO     | __main__:build_vocab:253 - Path exists
2024-09-09 23:18:03.852 | INFO     | __main__:astar:262 - Starting Experiment: A* Search with L=10 and N=4
2024-09-09 23:18:03.898 | INFO     | __main__:astar:271 - Time taken: 0.04602694511413574
2024-09-09 23:18:03.898 | DEBUG    | __main__:astar:272 - <SoS> appliances as are antiquity <EoS>
2024-09-09 23:18:03.898 | INFO     | __main__:astar:273 - Score: -1.0922722793121937
2024-09-09 23:18:03.898 | INFO     | __main__:astar:274 - Total Nodes Explored: 6195
2024-09-09 23:18:03.898 | INFO     | __main__:greedy:295 - Starting Experiment: Greedy Search with L=10 and N=4
2024-09-09 23:18:03.898 | DEBUG    | __main__:greedy:306 - <SoS> are antiquity affordable and <EoS>
2024-09-09 23:18:03.899 | INFO     | __main__:greedy:307 - Score: 2.8625366957877096
2024-09-09 23:18:03.899 | INFO     | __main__:greedy:308 - Time taken: 0.00010609626770019531
2024-09-09 23:18:03.899 | INFO     | __main__:greedy:309 - Total nodes Explored: 6
2024-09-09 23:18:03.899 | INFO     | __main__:iddfs:312 - Starting Experiment: IDDFS with L=10 and N=4
2024-09-09 23:18:04.316 | DEBUG    | __main__:iddfs:323 - <SoS> are antiquity antiquity appliances <EoS>
2024-09-09 23:18:04.316 | INFO     | __main__:iddfs:324 - Score: 4.233961023554623
2024-09-09 23:18:04.316 | INFO     | __main__:iddfs:325 - Time taken: 0.41671299934387207
2024-09-09 23:18:04.316 | INFO     | __main__:iddfs:326 - Total nodes Explored: 122212
2024-09-09 23:18:04.316 | INFO     | __main__:ucs:278 - Starting Experiment: Uniform Cost Search with L=10 and N=4
2024-09-09 23:18:04.349 | INFO     | __main__:ucs:288 - Time taken: 0.03273415565490723
2024-09-09 23:18:04.349 | DEBUG    | __main__:ucs:289 - <SoS> are antiquity antiquity appliances <EoS>
2024-09-09 23:18:04.350 | INFO     | __main__:ucs:290 - Score: 4.233961023554623
2024-09-09 23:18:04.350 | INFO     | __main__:ucs:291 - Total Nodes Explored: 22221
```

#### With N=5

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 10 -n 5
```

Results are as follows:

```bash
2024-09-09 23:19:40.333 | INFO     | __main__:build_transition:239 - Path exists
2024-09-09 23:19:40.346 | INFO     | __main__:build_vocab:253 - Path exists
2024-09-09 23:19:40.346 | INFO     | __main__:astar:262 - Starting Experiment: A* Search with L=10 and N=5
2024-09-09 23:19:40.437 | INFO     | __main__:astar:271 - Time taken: 0.09026741981506348
2024-09-09 23:19:40.437 | DEBUG    | __main__:astar:272 - <SoS> alessandro all appliances alternating are <EoS>
2024-09-09 23:19:40.437 | INFO     | __main__:astar:273 - Score: -2.1060265135797516
2024-09-09 23:19:40.437 | INFO     | __main__:astar:274 - Total Nodes Explored: 10992
2024-09-09 23:19:40.437 | INFO     | __main__:greedy:295 - Starting Experiment: Greedy Search with L=10 and N=5
2024-09-09 23:19:40.437 | DEBUG    | __main__:greedy:306 - <SoS> all appliances alternating are and <EoS>
2024-09-09 23:19:40.438 | INFO     | __main__:greedy:307 - Score: 6.172236340887277
2024-09-09 23:19:40.438 | INFO     | __main__:greedy:308 - Time taken: 9.632110595703125e-05
2024-09-09 23:19:40.438 | INFO     | __main__:greedy:309 - Total nodes Explored: 7
2024-09-09 23:19:40.438 | INFO     | __main__:iddfs:312 - Starting Experiment: IDDFS with L=10 and N=5
2024-09-09 23:20:28.009 | DEBUG    | __main__:iddfs:323 - <SoS> also alessandro are and appliances <EoS>
2024-09-09 23:20:28.010 | INFO     | __main__:iddfs:324 - Score: 8.674154179307141
2024-09-09 23:20:28.010 | INFO     | __main__:iddfs:325 - Time taken: 47.571229696273804
2024-09-09 23:20:28.010 | INFO     | __main__:iddfs:326 - Total nodes Explored: 1222212
2024-09-09 23:20:28.010 | INFO     | __main__:ucs:278 - Starting Experiment: Uniform Cost Search with L=10 and N=5
2024-09-09 23:20:28.431 | INFO     | __main__:ucs:288 - Time taken: 0.4208066463470459
2024-09-09 23:20:28.431 | DEBUG    | __main__:ucs:289 - <SoS> also alessandro are and appliances <EoS>
2024-09-09 23:20:28.431 | INFO     | __main__:ucs:290 - Score: 8.674154179307141
2024-09-09 23:20:28.432 | INFO     | __main__:ucs:291 - Total Nodes Explored: 222221
```

#### With N=6

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 10 -n 6
```

Results are as follows

```bash
Still Runnning ...... :)
```

Implies I waited but never got the results, my computer cannot support it (SIGKILL)


### Experiment 5: With L=15


#### With N=3

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 15 -n 3
```

```bash
2024-09-09 23:23:27.448 | INFO     | __main__:build_transition:239 - Path exists
2024-09-09 23:23:27.463 | INFO     | __main__:build_vocab:253 - Path exists
2024-09-09 23:23:27.463 | INFO     | __main__:astar:262 - Starting Experiment: A* Search with L=15 and N=3
2024-09-09 23:23:27.479 | INFO     | __main__:astar:271 - Time taken: 0.016185998916625977
2024-09-09 23:23:27.480 | DEBUG    | __main__:astar:272 - <SoS> as backbone availability <EoS>
2024-09-09 23:23:27.481 | INFO     | __main__:astar:273 - Score: -2.474936787670644
2024-09-09 23:23:27.481 | INFO     | __main__:astar:274 - Total Nodes Explored: 1804
2024-09-09 23:23:27.481 | INFO     | __main__:greedy:295 - Starting Experiment: Greedy Search with L=15 and N=3
2024-09-09 23:23:27.481 | DEBUG    | __main__:greedy:306 - <SoS> aspect are alessandro <EoS>
2024-09-09 23:23:27.481 | INFO     | __main__:greedy:307 - Score: 4.504665454145546
2024-09-09 23:23:27.481 | INFO     | __main__:greedy:308 - Time taken: 0.00011086463928222656
2024-09-09 23:23:27.482 | INFO     | __main__:greedy:309 - Total nodes Explored: 5
2024-09-09 23:23:27.482 | INFO     | __main__:iddfs:312 - Starting Experiment: IDDFS with L=15 and N=3
2024-09-09 23:23:27.624 | DEBUG    | __main__:iddfs:323 - <SoS> availability at automation <EoS>
2024-09-09 23:23:27.625 | INFO     | __main__:iddfs:324 - Score: 10.798133002291948
2024-09-09 23:23:27.625 | INFO     | __main__:iddfs:325 - Time taken: 0.1426708698272705
2024-09-09 23:23:27.625 | INFO     | __main__:iddfs:326 - Total nodes Explored: 57842
2024-09-09 23:23:27.625 | INFO     | __main__:ucs:278 - Starting Experiment: Uniform Cost Search with L=15 and N=3
2024-09-09 23:23:27.637 | INFO     | __main__:ucs:288 - Time taken: 0.011791467666625977
2024-09-09 23:23:27.637 | DEBUG    | __main__:ucs:289 - <SoS> availability at automation <EoS>
2024-09-09 23:23:27.637 | INFO     | __main__:ucs:290 - Score: 10.798133002291948
2024-09-09 23:23:27.638 | INFO     | __main__:ucs:291 - Total Nodes Explored: 7231
```


#### With N=4

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 15 -n 4
```

Results are as follows

```bash
2024-09-09 23:24:12.940 | INFO     | __main__:build_transition:239 - Path exists
2024-09-09 23:24:12.954 | INFO     | __main__:build_vocab:253 - Path exists
2024-09-09 23:24:12.955 | INFO     | __main__:astar:262 - Starting Experiment: A* Search with L=15 and N=4
2024-09-09 23:24:13.276 | INFO     | __main__:astar:271 - Time taken: 0.3211371898651123
2024-09-09 23:24:13.276 | DEBUG    | __main__:astar:272 - <SoS> as as as as <EoS>
2024-09-09 23:24:13.277 | INFO     | __main__:astar:273 - Score: -3.9625520695856133
2024-09-09 23:24:13.277 | INFO     | __main__:astar:274 - Total Nodes Explored: 41349
2024-09-09 23:24:13.277 | INFO     | __main__:greedy:295 - Starting Experiment: Greedy Search with L=15 and N=4
2024-09-09 23:24:13.277 | DEBUG    | __main__:greedy:306 - <SoS> and antiquity backbone affordable <EoS>
2024-09-09 23:24:13.277 | INFO     | __main__:greedy:307 - Score: 7.778410161739126
2024-09-09 23:24:13.277 | INFO     | __main__:greedy:308 - Time taken: 0.00011301040649414062
2024-09-09 23:24:13.277 | INFO     | __main__:greedy:309 - Total nodes Explored: 6
2024-09-09 23:24:13.278 | INFO     | __main__:iddfs:312 - Starting Experiment: IDDFS with L=15 and N=4
2024-09-09 23:24:31.843 | DEBUG    | __main__:iddfs:323 - <SoS> as as as at <EoS>
2024-09-09 23:24:31.843 | INFO     | __main__:iddfs:324 - Score: 69.49700833197527
2024-09-09 23:24:31.844 | INFO     | __main__:iddfs:325 - Time taken: 18.565299034118652
2024-09-09 23:24:31.844 | INFO     | __main__:iddfs:326 - Total nodes Explored: 867842
2024-09-09 23:24:31.844 | INFO     | __main__:ucs:278 - Starting Experiment: Uniform Cost Search with L=15 and N=4
2024-09-09 23:24:32.049 | INFO     | __main__:ucs:288 - Time taken: 0.20499539375305176
2024-09-09 23:24:32.049 | DEBUG    | __main__:ucs:289 - <SoS> as as as at <EoS>
2024-09-09 23:24:32.049 | INFO     | __main__:ucs:290 - Score: 69.49700833197527
2024-09-09 23:24:32.049 | INFO     | __main__:ucs:291 - Total Nodes Explored: 108481
```

#### With N=5

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 15 -n 5
```

```bash
Still Running ...... :)
```

Implies I waited but never got the results, my computer cannot support it (SIGKILL)

#### With N=6

```bash
python b22ai063.py --vocab <path_vocab> --transition <path_transition> -l 15 -n 6
```

```bash
Still Runnning ........ :)
```

Implies I waited but never got the results, my computer cannot support it (SIGKILL)

## Citations

- [Geek For Geeks](https://www.geeksforgeeks.org/a-search-algorithm/)
    - [A* Search](https://www.geeksforgeeks.org/a-search-algorithm/)
    - [IDDFS](https://www.geeksforgeeks.org/a-search-algorithm/)
    - [Greedy](https://www.geeksforgeeks.org/greedy-algorithms/)
    - [UCS](https://www.geeksforgeeks.org/uniform-cost-search-dijkstra-for-large-graphs/)

- People Who I talked to 
    - Shivam KhanChandani (B22BB038) Talked in Regards to UCS and IDDFS
    - Vishesh (B22AI050) Talked as to whether we need n+2 sentences, or how should we approach the problem.
    - Vikrant Singh (B22AI043) Talked in regards to UCS and IDDFS

- Blogs I referred to 
    - [MEDIUM](https://medium.com/analytics-vidhya/parts-of-speech-pos-and-viterbi-algorithm-3a5d54dfb346#:~:text=A%20transition%20matrix%20is%20an,states%20that%20might%20come%20next.)