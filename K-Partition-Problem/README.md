## K–Partition Problem | Printing all partitions

In the k–partition problem, we need to partition an array of positive integers into k disjoint subsets that all have an equal sum, and they completely cover the set.

For example, consider set `S = { 7, 3, 5, 12, 2, 1, 5, 3, 8, 4, 6, 4 }`.

 
1. S can be partitioned into two partitions, each having a sum of 30.

```
S1 = { 5, 3, 8, 4, 6, 4 }
S2 = { 7, 3, 5, 12, 2, 1 }
```

2. S can be partitioned into three partitions, each having a sum of 20.

```
S1 = { 2, 1, 3, 4, 6, 4 }
S2 = { 7, 5, 8 }
S3 = { 3, 5, 12 }
```
3. S can be partitioned into four partitions, each having a sum of 15.

```
S1 = { 1, 4, 6, 4 }
S2 = { 2, 5, 8 }
S3 = { 12, 3 }
S4 = { 7, 3, 5 }
```

4. S can be partitioned into five partitions, each having a sum of 12.

```
S1 = { 2, 6, 4 }
S2 = { 8, 4 }
S3 = { 3, 1, 5, 3 }
S4 = { 12 }
S5 = { 7, 5 }
```
