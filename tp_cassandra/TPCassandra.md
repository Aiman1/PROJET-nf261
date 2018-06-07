#TP CASSANDRA
## Questions

- Un jour donné
- un jour de la semaine donné
- une semaine donnée
- une zone de départ donnée
- une zone de destination donnée

## Cassandra
consistent hashing
CQL 3
## Serveur:
host: `nf26.leger.tf`
login: `tdg3`
pw: `XLky0jbx5Aj5`


## Commandes à exectuer


`CREATE KEYSPACE pacetheo WITH replication= {'class' : 'SimpleStrategy', 'replication_factor':2}`
`CREATE TABLE toto (id1 int, machin text, truc text, primarey key (id1));`
**Les clées sont obligatoires**

insert into toto (id1,truc) value (1, 'hoho')

**Les insert = les updates, ce sont des upsert**
pas de pbm à réinsérer la clés, on écrase donc



`CREATE TABLE toto (id1 int,id2 int,id3 int,id4 int, machin text, truc text, primarey key (id1,id2,id3,id4));`

==> 1 clé de partitionnement (pour les intervals consécutifs) puis des clés de tri.

On peut parfaitement avoir des clées composites, avec différents niveaux:
`CREATE TABLE toto (id1 int,id2 int,id3 int,id4 int, machin text, truc text, primarey key ((id1,id2),id3,id4));`


