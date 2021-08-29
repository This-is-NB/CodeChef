

import time
start = time.time()  
li = range(500000)
li = [i+5 for i in li]
print ("Time taken = %.5f" % (time.time() - start))
# >> Time taken = 0.06355

# from time import clock
import numpy as np
# li = range(500000)
start = time.time()
li = np.arange(500000)
# li = np.array(li)
li += 5
print ("Time taken = %.5f" % (time.time() - start))
# >> Time taken = 0.00055