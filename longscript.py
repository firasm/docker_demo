# This is a script that will take a long time to run

import numpy as np
from datetime import datetime

startTime = datetime.now()

data = np.arange(0,1000000)

for i in range(0,100000):
    data*=data

endTime = datetime.now()

print('The script took {0:.2f} s to execute'.format((endTime - startTime).total_seconds()))
