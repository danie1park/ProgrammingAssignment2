# Programming Assignment 2

UFIDs:  
Karla Tran: 89625286  
Daniel Park: 75200264  

# Overview

The assignment is written in Python. To get started, clone the GitHub repository:  
https://github.com/danie1park/ProgrammingAssignment2.git  

# Instructions

---
# Questions
## Question 1: Empirical Comparison
| Input File | k | m | FIFO | LRU | OPTFF |
|---|---|---|---|---|---|
|example2| 4 | 65 | 38 | 38 | 29 |
|example3| 3 | 58 | 43 | 33 | 23 |
|example4| 6 | 55 | 45 | 45 | 36 |

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

