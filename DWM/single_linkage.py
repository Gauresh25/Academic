def distance(point1, point2):
    """Calculate Euclidean distance between two 2D points"""
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


# Sample data
data = [
    (1, 1),  # Point 0
    (2, 2),  # Point 1
    (1.5, 1.5),  # Point 2
    (8, 8)  # Point 3
]

# Initialize: each point starts in its own cluster
clusters = [[point] for point in data]
print("Initial clusters:")
for i, cluster in enumerate(clusters):
    print(f"Cluster {i}: {cluster}")

# Main loop - continue until only one cluster remains
iteration = 1
while len(clusters) > 1:
    print(f"\nIteration {iteration}")
    print("Current clusters:")
    for i, cluster in enumerate(clusters):
        print(f"Cluster {i}: {cluster}")

    # Find minimum distance between clusters
    min_distance = float('inf')
    merge_pair = (0, 1)

    # Compare each pair of clusters
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            # Find minimum distance between points in clusters i and j
            cluster_distance = float('inf')
            for point1 in clusters[i]:
                for point2 in clusters[j]:
                    dist = distance(point1, point2)
                    if dist < cluster_distance:
                        cluster_distance = dist

            print(f"Distance between cluster {i} and {j}: {cluster_distance:.2f}")

            # Update minimum if this is the smallest distance found
            if cluster_distance < min_distance:
                min_distance = cluster_distance
                merge_pair = (i, j)

    # Merge the closest clusters
    i, j = merge_pair
    print(f"\nMerging clusters {i} and {j}")
    print(f"Cluster {i}: {clusters[i]}")
    print(f"Cluster {j}: {clusters[j]}")

    # Merge j into i
    clusters[i].extend(clusters[j])
    # Remove cluster j
    clusters.pop(j)

    print("\nClusters after merge:")
    for i, cluster in enumerate(clusters):
        print(f"Cluster {i}: {cluster}")

    iteration += 1

print("\nFinal single cluster:")
print(clusters[0])