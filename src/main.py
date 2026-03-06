from policies import fifo, lru, optff

import sys

def main():
    if len(sys.argv) != 2:
        print("Error: File is not properly formatted")
        return

    # Citations:
    # https://www.geeksforgeeks.org/python/read-a-file-line-by-line-in-python/
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        # First Line: k m
        first_line = file.readline()
        specs = first_line.split() # Citation: https://www.w3schools.com/python/ref_string_split.asp
        k = int(specs[0])
        m = int(specs[1])

        # Second Line: all the requests ids
        second_line = file.readline()
        requests = [int(request) for request in second_line.split()]

    # Check if m and requests match
    if len(requests) != m:
        print(f"Error: The number of requests ({len(requests)}) does not match m value ({m})")

    # Policies: FIFO | LRU | OPTFF
    fifo_output = fifo(k, requests)
    print(f"FIFO  : {fifo_output}")
    lru_output = lru(k, requests)
    print(f"LRU  : {lru_output}")
    optff_output = optff(k, requests)
    print(f"OPTFF  : {optff_output}")

if __name__=="__main__":
    main()