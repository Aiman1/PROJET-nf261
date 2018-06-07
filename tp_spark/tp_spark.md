# TP Spark

## Obbjectif:
Données: [0,N]

- Somme des données des nombres x tels que x % 5 = 0

- ----------------------------------------------- = 1

- ----------------------------------------------- = 2

- ----------------------------------------------- = 3

- ----------------------------------------------- = 4

mapping: di -> (di mod5, di)
reduction +


Puis
-  1 seul map reduce pour la moyenne et la variance d'un sensemble de données étiquetées par étiquette `{(x_i,z_i)}i`
-  Même sensemble, calculer une médiane par étiquette (médiane + ou -, c'est comme on veut)
-  même calculer tous les déciles informatifs (1 à 9, 0 et 10 ne servent à rien)

Ensuite on utilisera les fausses données:
```{python}
import sys
sys.path.append('/data')
import falsedata
i = 0
for md in falsedata.getdata():
    print(md)
    i+=1
    if(i > 10):
        break
```

En utulisant spark:

```{python}


## Spark

Permet de faire du map-reduce
Peut fonctionner seul (scala s'occupe de tout)
Sous forme de cluster de calcul(ARM lié à Hadoop), de stockage de données (cassandra)
Spark est un environnement avec de nombrbeuses techno

## utilisation

SPYSPARK_PYTHON
SPYSPARK_PYTHON_DRIVER
sc -> variable python, le Spark COntext. Objet global plein de méthodes

```{python}
my_dataset = sc.parallelize(ranger(100))
my_dataset.map( lambbda x : (x%5,x)) 
#c'est le data set
_4.reduceByKey(lambda x,y : x+y)
_8.collect()

```


Connexion: 
```{bash}
ssh tdg3@nf26.leger.tf
source /pyspark.env
pyspark
```

ON est alors sur la console iptyhon, avec pyspark. on eput executer en une ligne:

```{python}
my_dataset = sc.parallelize(ranger(100)
z = sc.parallelize(range(1,100)).map(lambda x: (x%5, x)).reduceByKey(lambda x,y : x+y).collect()

```

## TP

-  1 seul map reduce pour la moyenne et la variance d'un sensemble de données étiquetées par étiquette `{(x_i,z_i)}i`

** CORRECTION **
{(xi,zi)}i
Il va falloir calculer la somme des xi, des 1 et des xi^2 pour chaque z.
On va tout calculer en 1 map:
mapping: d -> (d[1],np.array([1,d[0],d[0]**2]))
reduction: -> (q: (sum(1)_i, sum(x_i)i, sum(x_i^2)i))

```{python}
a -> (a[0], (a[1][1]/a[1][0], a[1][2]/a[1][1] - (a[1][1]/a[1][0])**2)

```

-  Même sensemble, calculer une médiane par étiquette (médiane + ou -, c'est comme on veut)
-  même calculer tous les déciles informatifs (1 à 9, 0 et 10 ne servent à rien)
