from typing import Tuple
from point import Point

# INSERT POINTS HERE
points              : list[Tuple[float, ...]]   = [(-8,0), (-1,0), (0,0), (1,0), (2,2), (3,3)]
initial_centroids   : list[Tuple[float, ...]]   = [(0,0), (3,3)]
# FROM HERE, JUST LET THE ALGORITHM RUN


LINE_LENGTH = 96
def validate_input(points: list[Point], initial_centroids: list[Point]):
    if not points:
        raise ValueError("There should be at least one point.")
    if not initial_centroids:
        raise ValueError("There should be at least one initial_centroid.")

    standard_len = len(points[0].cords)
    for point in points + initial_centroids:
        if len(point.cords) != standard_len:
            raise ValueError(f"Please provide all points in the same dimension. Point {point.cords} is in R^{len(point.cords)} while Point {points[0].cords} is in R^{standard_len}")

def print_state(iteration_number: int, centroids: list[Point], clusters_old: dict[int, frozenset]):
    iteration_text = f"Iteration {iteration_number}"
    iteration_text_padding = (LINE_LENGTH - len(iteration_text)) // 2

    print("=" * LINE_LENGTH)
    print(" " * iteration_text_padding + iteration_text)
    for centroid_idx, centroid in enumerate(centroids):
        print(f"\tCentroid: {centroid}")
        print(f"\tCluster: {clusters_old[centroid_idx]}")

def k_means(points: list[Point], initial_centroids: list[Point]):
    validate_input(points, initial_centroids)

    centroids: list[Point] = initial_centroids
    clusters: dict[int, list[Point]] = {}
    clusters_old: dict[int, frozenset[Point]] = {}

    is_some_point_switched_cluster: bool = True # do-while
    iteration_number = -1 

    while is_some_point_switched_cluster:
        is_some_point_switched_cluster  = False
        clusters                        = {}
        iteration_number                += 1

        # Calculating new centroids
        if iteration_number > 0: # in the first iteration, we just want to cluster the points
            for centroid_idx in range(len(centroids)):
                centroid_cluster: list[Point] = list(clusters_old[centroid_idx])
                centroid_cluster_sum: Point = centroid_cluster[0]
                for point in centroid_cluster[1:]:
                    centroid_cluster_sum += point
                centroid_cluster_mean: Point = centroid_cluster_sum / len(centroid_cluster)
                centroids[centroid_idx] = centroid_cluster_mean

        # Clustering the points
        for point in points:
            cluster_new_idx, _ = min(enumerate(centroids), key=lambda pair: point.distance(pair[1]))
            if cluster_new_idx not in clusters:
                clusters[cluster_new_idx] = []
            clusters[cluster_new_idx].append(point)
            cluster_old_idx = next((centroid_idx for centroid_idx, points in clusters_old.items() if point in points), None)
            if cluster_old_idx != cluster_new_idx:
                is_some_point_switched_cluster = True


        # Keeping track of previous clusters, we stop if no point switched cluster
        clusters_old = dict((centroid_idx, frozenset(points)) for centroid_idx, points in clusters.items())

        # Getting intermediary information
        print_state(iteration_number, centroids, clusters_old)
    print("=" * LINE_LENGTH)
points_typed            = [Point(point) for point in points]
initial_centroids_typed = [Point(centroid) for centroid in initial_centroids]

k_means(points_typed, initial_centroids_typed)
