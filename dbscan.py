from typing import Tuple
from point import Point

# INSERT POINTS HERE
points              : list[Tuple[float, ...]]   = [(0,), (1,), (2,), (3,), (4,), (5,), (6,), (10,), (14,), (15,), (16,), (17,), (18,)]
# FROM HERE, JUST LET THE ALGORITHM RUN

EPS=1.5
N_0 = 2
LINE_LENGTH = 96
def print_state(iteration_number: int, clusters: set[frozenset[Point]]):
    iteration_text = f"Iteration {iteration_number}"
    iteration_text_padding = (LINE_LENGTH - len(iteration_text)) // 2

    print("=" * LINE_LENGTH)
    print(" " * iteration_text_padding + iteration_text)
    for cluster in clusters:
        print(f"\tCluster: {cluster}")

def dbscan(points: list[Point], N_0: int, EPS: float):
    points_in_neighborhood: dict[Point, list[Point]] = { point: [] for point in points }
    core_points: list[Point] = []
    border_points: dict[Point, Point] = {}
    noise_points: list[Point] = []
    clusters: set[frozenset[Point]] = set(frozenset({ point }) for point in points)

    did_join_clusters = True
    iteration_number = 0
    while did_join_clusters:
        print_state(iteration_number, clusters)
        iteration_number += 1
        did_join_clusters = False

        # Count points in proximity of each point
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = points[i].distance(points[j])
                if dist < EPS:
                    points_in_neighborhood[points[i]].append(points[j])
                    points_in_neighborhood[points[j]].append(points[i])
        # Divide all points into the three categories
        for point in points:
            # Core Point
            if len(points_in_neighborhood[point]) >= N_0:
                core_points.append(point)
                continue
            # Border Point
            for neighboring_point in points_in_neighborhood[point]:
                if len(points_in_neighborhood[point]) >= N_0:
                    border_points[point] = neighboring_point
                    continue
            # Noise Point
            noise_points.append(point)
        # Delete all noise points: collected them just to emphasis that...
        noise_points = []
        # Given two different core points x_i,x_j, such that x_i\inB_EPS(x_j), "connect" the two into two clusters
        for i in range(len(core_points)):
            for j in range(i+1, len(core_points)):
                if core_points[i].distance(core_points[j]) < EPS:
                    cluster_i = next(cluster for cluster in clusters if core_points[i] in cluster)
                    cluster_j = next(cluster for cluster in clusters if core_points[j] in cluster)

                    new_cluster = cluster_i | cluster_j
                    if core_points[j] in cluster_i:
                        break
                    else:
                        clusters.remove(cluster_i)
                        clusters.remove(cluster_j)
                    clusters.add(new_cluster)
                    did_join_clusters = True
                    break

        # Given a border point x_i\inB_EPS(x_j), "connect" it to the cluster of the core point x_j
        for border_point, core_point in border_points.items():
            cluster_core_point = next(cluster for cluster in clusters if core_point in cluster)
            if border_point in cluster_core_point:
                continue
            else:
                new_cluster = cluster_core_point | frozenset({ border_point })
                clusters.remove(cluster_core_point)
                clusters.add(new_cluster)
                did_join_clusters = True
                continue
    print("=" * LINE_LENGTH)

points_typed = [Point(point) for point in points]
dbscan(points_typed, N_0, EPS)
