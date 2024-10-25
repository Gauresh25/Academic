import random
import math


def distance(point, centroid):
    """Calculate distance between two 2D points"""
    return math.sqrt((point[0] - centroid[0]) ** 2 + (point[1] - centroid[1]) ** 2)


def kmeans_2clusters(data, max_iterations=100):
    """
    Simplified K-means for exactly 2 clusters
    Args:
        data: list of (x, y) tuples
        max_iterations: maximum number of iterations
    Returns:
        clusters: list of 0s and 1s indicating cluster assignments
        centroid1, centroid2: final positions of the two centroids
    """
    # Initialize by picking 2 random points as centroids
    points = data.copy()
    random.shuffle(points)
    centroid1 = points[0]  # First centroid
    centroid2 = points[1]  # Second centroid

    for _ in range(max_iterations):
        # Assign points to nearest centroid
        clusters = []
        cluster1_points = []  # Points assigned to centroid1
        cluster2_points = []  # Points assigned to centroid2

        # Assign each point to nearest centroid
        for point in data:
            dist1 = distance(point, centroid1)
            dist2 = distance(point, centroid2)

            if dist1 < dist2:
                clusters.append(0)
                cluster1_points.append(point)
            else:
                clusters.append(1)
                cluster2_points.append(point)

        # Calculate new centroid positions
        new_centroid1 = (
            sum(p[0] for p in cluster1_points) / len(cluster1_points),
            sum(p[1] for p in cluster1_points) / len(cluster1_points)
        )

        new_centroid2 = (
            sum(p[0] for p in cluster2_points) / len(cluster2_points),
            sum(p[1] for p in cluster2_points) / len(cluster2_points)
        )

        # Check if centroids have moved
        if (new_centroid1 == centroid1 and new_centroid2 == centroid2):
            break

        centroid1 = new_centroid1
        centroid2 = new_centroid2

    return clusters, centroid1, centroid2


# Example usage:
if __name__ == "__main__":
    # Sample data with two clear clusters
    data = [
        (1, 1), (2, 1), (1, 2),  # Cluster 1
        (8, 8), (9, 8), (8, 9)  # Cluster 2
    ]

    # Run clustering
    clusters, cent1, cent2 = kmeans_2clusters(data)

    # Print results
    print("\nResults:")
    for i, (point, cluster) in enumerate(zip(data, clusters)):
        print(f"Point {point} is in cluster {cluster}")
    print(f"\nFinal centroids:")
    print(f"Centroid 1: {cent1}")
    print(f"Centroid 2: {cent2}")