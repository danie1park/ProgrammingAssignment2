# Programming Assignment 2

**UFIDs**:  
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
* The format was done according to the 
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
**If such a sequence exists:**  
- **Construct one.**
- **Compute and report the miss counts for both policies.**

**If you believe no such sequence exists for the policy you chose:**  
- **Provide a clear justification.**

**In either case, briefly explain your reasoning.**

**OPTFF incurs strictly fewer misses than LRU:**  
There exists a request sequence for which OPTFF incurs strictly fewer misses than LRU.

For example:  
If $k = 3$, and $m = 8$, and the requests are $[1, 2, 3, 4, 1, 2, 3, 4]$, the miss counts would be OPTFF = 5 and LRU = 8, so OPTFF has strictly fewer misses than LRU.

A cyclical request sequence with at least k+1 (4) distinct items and k = 3 causes OPTFF to have strictly fewer cache misses than LRU. LRU always evicts the least recently used item, so the cyclical pattern forces the cache to miss whenever the cache is full and a request is made. OPTFF, instead, evicts the farthest-in-future-requested item which would be the last item in cycle that was added (between 3 and 4 depending on which is requested). This allows OPTFF to always have less misses than LRU.

**OPTFF incurs strictly fewer misses than FIFO:**  
There exists a request sequence for which OPTFF incurs strictly fewer misses than FIFO.

For example:  
If $k = 3$, and $m = 8$, and the requests are $[1, 2, 3, 4, 1, 2, 3, 4]$, the miss counts would be OPTFF = 5 and FIFO = 8, so OPTFF has strictly fewer misses than FIFO.

In the same conditions given in the reasoning above, FIFO always evicts the first item in the cached order (oldest item). The cyclical pattern forces the cache to miss whenever the cache is full and a request is made. OPTFF logic follows the same reasoning as in the above reasoning.


## Question 3: Prove OPTFF is Optimal
**Let OPTFF be Belady’s Farthest-in-Future algorithm.
Let ( A ) be any offline algorithm that knows the full request sequence.
Prove that the number of misses of OPTFF is no larger than that of ( A ) on any fixed sequence.**

