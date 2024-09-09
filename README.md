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
4. [Conclusion](#conclusion)


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



## Conclusion