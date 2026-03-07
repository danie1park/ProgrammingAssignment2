# Programming Assignment 2

UFIDs:  
Karla Tran: 89625286  
Daniel Park: 75200264  

# Overview

This repository contains a Python implementation of three cache eviction policies (FIFO, LRU, OPTFF) as required by Programming Assignment 2.  
The assignment is written in Python. To get started, clone the GitHub repository:  
https://github.com/danie1park/ProgrammingAssignment2.git

# Instructions

   Make sure to have Python 3 installed (tested with 3.10+).  
   No external dependencies are needed.  

**Running the program**
* The program will be run in the root directory of the repository.
* The executable script is `src/main.py`
* Provide only one argument: the path to an input file formatted as described below.  
  - Example command:  
    `python3 src/main.py tests/example1.in`
    - The program prints three lines to stdout:
    ```
    FIFO  : <number_of_misses>
    LRU   : <number_of_misses>
    OPTFF : <number_of_misses>
    ```

**Input format**
* The format was chosen according to the assignment requirements.
* First line: two integers `k m` (cache capacity and number of requests).
* Second line: `m` integer request IDs separated by spaces.
* See the `tests/` directory for sample input files.

**Assumptions**:
   - Use exactly two lines only:
       - First line contains `k m`
       - Second contains `r_1 r_2 ... r_m` 
       - Follow this or the program may not run as expected
   - Based on the assignment requirements, the output files were assumed to contain expected outputs of the input files, instead of being directly written to. Instead, the program prints results to the terminal.  
   - Based on the line from 2 of the Submissions section:  
       `The corresponding expected output file (e.g., example.out)`

**Verifying results**
* Corresponding expected outputs are provided as `.out` files alongside each `.in` file.  
* To compare the stdout of your run with the contents of the `.out` file, run:  
    ```
    python3 src/main.py tests/example2.in | diff - tests/example2.out
    ```
**Tests**
* Four nontrivial example files, with at least three containing at least 50 requests can be found in `tests/`.
* Example 1 has less than 50 requests.

---
# Questions
## Question 1: Empirical Comparison
| Input File | k | m | FIFO | LRU | OPTFF |
|---|---|---|---|---|---|
|example2.in| 4 | 65 | 38 | 38 | 29 |
|example3.in| 3 | 56 | 43 | 33 | 23 |
|example4.in| 6 | 55 | 45 | 45 | 36 |
|example5.in| 3 | 50 | 29 | 23 | 17 |

`example1.in` was not include because m < 50.

**Does OPTFF have the fewest misses?**
OPTFF has the fewest misses of all the policies.

**How does FIFO compare to LRU?**
FIFO tends to do worst or equally in comparison to LRU.

## Question 2: Bad Sequence for LRU or FIFO
**For ( k = 3 ), investigate whether there exists a request sequence for which OPTFF incurs strictly fewer misses than LRU (or FIFO).**
If such a sequence exists:
- Construct one.
- Compute and report the miss counts for both policies.

If you believe no such sequence exists for the policy you chose:
- Provide a clear justification.

**In either case, briefly explain your reasoning.**

## Question 3: Prove OPTFF is Optimal
**Let OPTFF be Belady’s Farthest-in-Future algorithm.
Let ( A ) be any offline algorithm that knows the full request sequence.
Prove that the number of misses of OPTFF is no larger than that of ( A ) on any fixed sequence.**

Citation: Strongly inspired by Greedy Algorithm lecture slides and notes  

I will solve this problem using proof by induction.  

The proof is to show that OPTFF (Belady’s Farthest-in-Future, optimal offline) is optimal for the offline caching problem.  

**Theorem:** OPTFF is an optimal eviction algorithm. For any request sequence, the number of cache misses by OPTFF is no larger than that of any offline algorithm ( A ).

**Invariant:** There exists an optimal reduced schedule S derived from algorithm ( A ) that matches the eviction decisions of S_OPTFF​ through the first j steps.  

**Base Case: j = 0**
Prior to any requests, the cache contents of S and S_OPTFF would match. This invariant holds for j = 0.  

**Inductive Step:**  
Say there exists an optimal reduced schedule S that agrees with S_OPTFF through step j. We will then construct a new optimal schedule, S’, that agrees with S_OPTFF through j + 1.  

Let d be the item requested at step j + 1.  
* Case 1: d is already in the cache. Then neither S nor S_OPTFF need to perform an eviction. Then, S’ = S and the invariant holds.
* Case 2: d is not in the cache. Then S and S_OPTFF both evict the same item. S’ = S still remains optimal and agrees with S_OPTFF through j + 1.
* Case 3: d is not in the cache, and the algorithms evict different items. Let S_OPTFF evict item e, and S evict item f, e ≠ f. Then, we will construct a new schedule S’ that shares the same behavior as S except at j + 1, where it evicts e instead of f. Now, S’ agrees with S_OPTFF for the first j + 1 steps. We now argue that having f in the cache instead of e is no worse.

    - Since OPTFF evicts the item whose next request is farthest in the future, the next request for f must occur before the next request for e (or perhaps e may never be requested again).

    - Because of this, keeping f in the cache instead of e cannot cause S′ to incur more cache misses than S. If S needs f later, S′ already has it. If S′ later needs e, it may incur a miss there, but that miss occurs no earlier than in S.

    - Therefore S′ has no more misses than S, and it remains optimal while agreeing with S_OPTFF for one more step.  

Since we can extend the invariant from j to j + 1, the invariant holds for all steps by induction. Therefore, there exists an optimal schedule that makes exactly the same eviction decisions as OPTFF. This means OPTFF incurs no more cache misses than any other algorithm.  

Thus, OPTFF is an optimal eviction algorithm.
