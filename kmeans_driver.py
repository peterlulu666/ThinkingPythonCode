import math
import random

import kmeans_viz

# Your initial dataset is this list of lists, containing 100 2-dimensional points
# Input data set
DATA = [[-32.97, -21.06], [9.01, -31.63], [-20.35, 28.73], [-0.18, 26.73], [-25.05, -9.56], [-0.13, 23.83],
        [19.88, -18.32], [17.49, -14.09], [17.85, 27.17], [-30.94, -8.85], [4.81, 42.22], [-4.59, 11.18],
        [9.96, -35.64], [24.72, -11.39], [14.44, -43.31], [-10.49, 33.55], [4.24, 31.54], [-27.12, -17.34],
        [25.24, -12.61], [20.26, -4.7], [-16.4, -19.22], [-15.31, -7.65], [-26.61, -20.31], [15.22, -30.33],
        [-29.3, -12.42], [-50.24, -21.18], [-32.67, -13.11], [-30.47, -17.6], [-23.25, -6.72], [23.08, -9.34],
        [-25.44, -6.09], [-37.91, -4.55], [0.14, 34.76], [7.93, 49.21], [-6.76, 12.14], [-19.13, -2.24], [12.65, -7.23],
        [11.25, 25.98], [-9.03, 22.77], [9.29, -26.2], [15.83, -1.45], [-22.98, -27.37], [-25.12, -23.35],
        [21.12, -26.68], [20.39, -24.66], [26.69, -28.45], [-45.42, -25.22], [-8.37, -21.09], [11.52, -16.15],
        [7.43, -32.89], [-31.94, -11.86], [14.48, -10.08], [0.63, -20.52], [9.86, 13.79], [-28.87, -17.15],
        [-29.67, -22.44], [-20.94, -22.59], [11.85, -9.23], [30.86, -21.06], [-3.8, 22.54], [-5.84, 21.71],
        [-7.01, 23.65], [22.5, -11.17], [-25.71, -14.13], [-32.62, -15.93], [-7.27, 12.77], [26.57, -13.77],
        [9.94, 26.95], [-22.45, -23.18], [-34.7, -5.62], [29.53, -22.88], [0.7, 31.02], [-22.52, -10.02],
        [-23.36, -14.54], [-19.44, -12.94], [-0.5, 23.36], [-45.27, -19.8], [8.95, 13.63], [47.16, -14.46],
        [5.57, 4.85], [-19.03, -25.41], [28.16, -13.86], [-15.42, -14.68], [10.19, -25.08], [0.44, 23.65],
        [-20.71, -20.94], [35.91, -20.07], [42.81, -21.88], [5.1, 9.33], [-15.8, -18.47], [5.39, -26.82],
        [-40.53, -17.16], [-29.54, 23.72], [7.8, 23.4], [-22.19, -27.76], [-23.48, -25.01], [-21.2, -21.74],
        [23.14, -24.14], [-28.13, -13.04], [-24.38, -6.79]]


def main():
    # data​, a list of lists, each containing exactly
    # 2 floats to represent a 2-dimensional point. For this program, ​
    # data​ will contain 100 points. (This should be the same as input data.
    data = DATA
    # centroids​, a list of lists, each containing exactly
    # 2 floats to represent a 2-dimensional point.
    # For this program, ​centroids​ will contain 4 points, because we’re making 4 clusters.
    centroids = []
    # assignment​, a list of lists, each containing exactly 2 integers to represent the indices of ​data
    # and ​centroids​, respectively. For example, if assignment contains [[8, 0], [9, 3]], then we would
    # say that ​data[8]​is assigned to ​centroid[0]​, and ​data[9]​ is assigned to centroid[3]
    # colors​, a list of strings that is the same length as ​centroids.
    assignment = []
    # colors​, a list of strings that is the same length as ​centroids
    colors = ["red", "blue", "purple", "green"]
    # Set the number of clusters (i.e., the value of ​k​ in ​k-means clustering​). We’ll use 4
    number_of_clusters = 4
    # Choose 4 random points to be your “centroids.” Our centroids will be chosen from our initial data.
    # Choose 4 points at random from the input data set.
    random_points = []
    for index in range(number_of_clusters):
        random_points.append(random.choice(data))

    # For each point in the data set, find the closest centroid.
    # Assign that point to the centroid.
    # Once all the points are assigned to a centroid, we have our clusters
    # The closest centroid
    position_one = 0
    position_two = 0
    minimum = 100

    for point_A in data:

        for point_B in random_points:
            # The closest centroid for a given point is chosen using the Euclidean distance algorithm
            distance = abs(math.sqrt(((point_A[0] - point_B[0]) ** 2) + ((point_A[1] - point_B[1]) ** 2)))

            if (distance != 0) and (distance < minimum):
                minimum = distance
                position_one = data.index(point_A)
                position_two = random_points.index(point_B)

        centroids.append(position_one)
        centroids.append(position_two)

        assignment.append(centroids)

        minimum = 100
        position_one = 0
        position_two = 0
        centroids = []

    # Invoke the functions we’ve defined in ​kmeans_viz.py.
    # You need to invoke only two functions: draw_centroids​ ​and ​draw_assignment.
    kmeans_viz.draw_centroids(random_points, colors)
    kmeans_viz.draw_assignment(random_points, data, assignment, colors)


main()
