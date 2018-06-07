import numpy as np
import spark_context as sc  # à corriger, pas nécessaire sur le machine du TD
# pour les donnees plus complexes


def map1(d):
    x, z = d
    return(z, np.array[1, x, x**2])


def map2(d):
    (k, (s1, sx, sxsq)) = d  # c'est cool python!!
    return (k, (sx/s1, sxsq/s1 - (sx/s1)**2))


dataset = sc.parallelize(range(1, 100)).map(lambda x: (x % 5, x))
dataset.map(map1).map(map2)
dataset.map(map2)
dataset_r = dataset.reduce(lambda x, y: x+y)
