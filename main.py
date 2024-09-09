import heapq
import argparse
import math
import time
import numpy as np
import os
from typing import List, Tuple, Set, Dict
from loguru import logger

class Node:
    def __init__(self, path: List[int], g_score: float, h_score: float):
        self.path = path
        self.g_score = g_score
        self.h_score = h_score
        self.f_score = g_score + h_score

    def __lt__(self, other):
        return self.f_score < other.f_score

def read_transition_matrix(filename: str) -> List[List[float]]:
    with open(filename, 'r') as f:
        return [list(map(float, line.strip().split())) for line in f]

def read_vocabulary(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def negative_log_likelihood(prob: float) -> float:
    return -math.log(prob) if prob > 0 else float('inf')


def ucs(
    vocab: List[str], 
    transition_matrix: List[List[float]], 
    n: int, 
    L: int
) -> Tuple[List[str], float, int]:
    pq = []
    start_word = "<SoS>"
    end_word = "<EoS>"
    nodes_explored = 1
    
    # Initialize the priority queue with all possible starting words
    for i in range(L):  # Changed from n to L
        score = transition_matrix[-2][i]  
        heapq.heappush(pq, (-score, i, 1, [start_word, vocab[i]]))
        nodes_explored += 1

    max_sentence, max_score = None, 0
    while pq:
        score, index, depth, sentence = heapq.heappop(pq)

        score = -score  
        nodes_explored += 1
        
        if depth == n:
            sentence.append(end_word)
            final_score = score * transition_matrix[index][-1]
            
            if final_score > max_score:
                max_sentence, max_score = sentence, final_score
            continue
        
        if depth > n:
            break
        
        for i in range(L):  # Changed from n to L
            next_score = transition_matrix[index][i]
            new_score = score * next_score
            new_sentence = sentence + [vocab[i]]
            nodes_explored += 1
            heapq.heappush(pq, (-new_score, i, depth + 1, new_sentence))

    return max_sentence, max_score, nodes_explored

def iddfs(vocab, transition_matrix, n, L):
    q = []

    start_word = "<SoS>"
    end_word = "<EoS>"
    for i in range(n):
        score = transition_matrix[-2][i]  
        q.append((score, i, 1, [start_word, vocab[i]]))

    best_sentence = None    
    while q:
        cur_score, index , depth, sentence = q.pop(0)
        # If we've reached the required number of words
        if depth == L-2:
            # Add <EoS> and calculate the final transition score
            sentence.append(end_word)
            final_score = cur_score * transition_matrix[-1][index]  # Transition to <EoS>
            best_sentence, score = sentence, final_score
            
        elif depth>L-2:
            break                 
        
        # Expand the next words from the current word
        for i in range(n):  # Iterate over vocab words
            next_prob = transition_matrix[index][i]
            new_score = cur_score * next_prob
            new_sentence = sentence + [vocab[i]]
            # Avoid paths that have been previously expanded from the same word
            q.append((new_score, i, depth + 1, new_sentence))
            
    return best_sentence, score

def modified_iddfs(
    vocab: List[str], 
    transition_matrix: List[List[float]], 
    n: int, 
    L: int
) -> Tuple[List[str], float, int]:
    q = []

    nodes_explored = 1
    start_word = "<SoS>"
    end_word = "<EoS>"
    
    # Initialize the queue with all possible starting words
    for i in range(L):  # Changed from n to L
        score = transition_matrix[-2][i]  
        q.append((score, i, 1, [start_word, vocab[i]]))

    best_sentence, max_score = None, 0
    while q:
        cur_score, index, depth, sentence = q.pop(0)
        nodes_explored += 1
        
        if depth == n:  # Changed from L-2 to n
            sentence.append(end_word)
            final_score = cur_score * transition_matrix[index][-1]  # Changed from transition_matrix[-1][index]
            
            if final_score > max_score:
                best_sentence, max_score = sentence, final_score

        elif depth > n:  # Changed from L-2 to n
            break                 
        
        for i in range(L):  # Changed from n to L
            next_prob = transition_matrix[index][i]
            new_score = cur_score * next_prob
            nodes_explored += 1
            new_sentence = sentence + [vocab[i]]
            q.append((new_score, i, depth + 1, new_sentence))
            
    return best_sentence, max_score, nodes_explored

def generate_optimal_sentence_astar(
    transition_matrix: List[List[float]], 
    vocabulary: List[str], 
    sentence_length: int
) -> Tuple[List[str], float, int]:
    L = len(vocabulary)
    start_probs = transition_matrix[L]
    end_probs = transition_matrix[L + 1]

    def heuristic(path: List[int]) -> float:
        score = 0
        for i in range(len(path)):
            if i == 0:
                score += negative_log_likelihood(start_probs[path[i]])
            elif i == len(path) - 1:
                score += negative_log_likelihood(end_probs[path[i]])
            else:
                score += negative_log_likelihood(transition_matrix[path[i-1]][path[i]])
        return score

    open_set = []
    heapq.heappush(open_set, Node([0], 0, heuristic([0])))
    
    best_score = float('inf')
    best_sentence = ["<SoS>", "<EoS>"]
    nodes_explored = 0

    while open_set:
        current = heapq.heappop(open_set)
        nodes_explored += 1

        if len(current.path) == sentence_length + 2:
            score = current.g_score
            if score < best_score:
                best_score = score
                best_sentence = ["<SoS>"] + [vocabulary[i] for i in current.path[1:-1]] + ["<EoS>"]
            continue

        current_word_index = current.path[-1]
        for next_word_index in range(L):
            prob = transition_matrix[current_word_index][next_word_index]
            if prob > 0:
                tentative_g_score = current.g_score + negative_log_likelihood(prob)
                new_path = current.path + [next_word_index]
                heapq.heappush(open_set, Node(new_path, tentative_g_score, heuristic(new_path)))

    return best_sentence, best_score, nodes_explored


def generate_sentence_greedy(L, n, transition_matrix, vocabulary):
    # Initialize start and end tokens
    start_token = "<SoS>"
    end_token = "<EoS>"
    vocabulary.append(start_token)
    vocabulary.append(end_token)

    # Generate the sentence greedily
    sentence = [start_token]
    current_word = start_token
    nodes_explored = 1
    for _ in range(n):
        next_word_idx = np.argmax(transition_matrix[vocabulary.index(current_word)])
        next_word = vocabulary[next_word_idx]
        sentence.append(next_word)
        current_word = next_word
        nodes_explored += 1

    # Calculate the score
    score = transition_matrix[vocabulary.index(start_token)][vocabulary.index(sentence[1])]
    for i in range(1, len(sentence) - 1):
        if i + 1 < len(sentence):
            score *= transition_matrix[vocabulary.index(sentence[i])][vocabulary.index(sentence[i+1])]
        else:
            score *= transition_matrix[vocabulary.index(sentence[i])][vocabulary.index(end_token)]

    nodes_explored += 1
    sentence.append(end_token)
    return " ".join(sentence), score, nodes_explored

class Experiment(object):
    def __init__(self, vocab_file, transition_m_file, L, n) -> None:
        self.vocab_file = vocab_file
        self.transition_m_file = transition_m_file
        self.L = L
        self.n = n

    def build_transition(self) -> Tuple[bool, np.array]:
        if os.path.exists(self.transition_m_file):
            logger.info("Path exists")
            self.transition_matrix = np.loadtxt(self.transition_m_file)
            return True, self.transition_matrix
        else:
            logger.error("Path Doesnt Exist")
            return False, None

    def build_vocab(self) -> Tuple[bool, List[str]]:
        if os.path.exists(self.vocab_file):
            logger.info("Path exists")
            self.vocab = [line.strip() for line in open(self.vocab_file)]
            return True, self.vocab
        else:
            logger.error("Path Doesn't exist")
            return False, None

    def astar(self):
        start_time = time.time()
        logger.info(
            f"Starting Experiment: A* Search with L={self.L} and N={self.n}"
        )
        optimal_sentence, score, nodes_explored = generate_optimal_sentence_astar(
            self.transition_matrix, 
            self.vocab[:self.L], 
            self.n
        )
        end_time = time.time()
        logger.info(f"Time taken: {end_time - start_time}")
        logger.debug(" ".join(optimal_sentence))
        logger.info(f"Score: {score}")
        logger.info(f"Total Nodes Explored: {nodes_explored}")

    def ucs(self):
        start_time = time.time()
        logger.info(
            f"Starting Experiment: Uniform Cost Search with L={self.L} and N={self.n}"
        )
        optimal_sentence, score, nodes_explored = ucs(
            self.vocab[:self.L], 
            self.transition_matrix,
            self.n,
            self.L
        )
        end_time = time.time()
        logger.info(f"Time taken: {end_time - start_time}")
        logger.debug(" ".join(optimal_sentence))
        logger.info(f"Score: {score}")
        logger.info(f"Total Nodes Explored: {nodes_explored}")
        

    def greedy(self):
        logger.info(
            f"Starting Experiment: Greedy Search with L={self.L} and N={self.n}"
        )
        start_time = time.time()
        sentence, score, nodes_explored = generate_sentence_greedy(
            self.L,
            self.n,
            self.transition_matrix,
            self.vocab[:self.L]
        )
        end_time = time.time()
        logger.debug(sentence)
        logger.info(f"Score: {score}")
        logger.info(f"Time taken: {end_time - start_time}")
        logger.info(f"Total nodes Explored: {nodes_explored}")

    def iddfs(self):
        logger.info(
            f"Starting Experiment: IDDFS with L={self.L} and N={self.n}"
        )
        start_time = time.time()
        sentence, score, nodes_explored = modified_iddfs(
            vocab=self.vocab,
            transition_matrix=self.transition_matrix,
            n=self.n,
            L=self.L
        )
        end_time = time.time()
        logger.debug((" ".join(sentence)))
        logger.info(f"Score: {score}")
        logger.info(f"Time taken: {end_time - start_time}")
        logger.info(f"Total nodes Explored: {nodes_explored}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="AI Assignmnet 1, Creator: Jyotin Goel"
    )
    parser.add_argument("--vocab", help="Path to vocabulary file")
    parser.add_argument("--transition", help="Path to Transition Matrix file")
    parser.add_argument("-l", help="Length of Vocabulary of L words")
    parser.add_argument("-n", help="Length of Sentence of n+2 Words")
    args = parser.parse_args()
    
    check = Experiment(
        args.vocab, 
        args.transition,
        int(args.l), 
        int(args.n)
    )
    check.build_transition()
    check.build_vocab()
    check.astar()
    check.greedy()
    check.iddfs()
    check.ucs()