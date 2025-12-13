# K-Means
The K-Means algorithm takes a dataset comprised of points and an amount of _clusters_ noted $k$, and returns the $k$ _clusters_ of points that minimise the cumulative distance between all points in the same cluster.

## How does it work?
_Provided we have_ $k$ _initial points called "centroids", or that we have generated such points at random_
The algorithm works by repeatedly performing the three following steps:

1. Calculate the distance between each of the points in the dataset, and each of the _centroids_.
2. For each point in the dataset, assign it to the _cluster_ corresponding to the _centroid_ that is the nearest to it.
3. For each _cluster_, replace the _cluster_'s _centroid_ with the mean of all points in the _cluster_.

The process is deemed complete when an entire iteration is finished, without any of the points transitioning from one _cluster_ to another.

# DBSCAN
README is WIP
## How does it work?
README is WIP

