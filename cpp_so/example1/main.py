import time
import pyximport;pyximport.install()

import pyth_triples 

def main():
    start = time.time()
    result = pyth_triples.count_triples(1000)
    duration = time.time() - start
    print(result, duration)

if __name__ == '__main__':
    main()
