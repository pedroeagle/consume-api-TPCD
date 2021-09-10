import numpy as np
notas = "6,7,85,1,5,9,7,3,6,7"
notas_array = np.array(notas.split(',')).astype(np.int8)
print(np.mean(notas_array))