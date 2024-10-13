import sys
import math
import matplotlib.pyplot as plt

class Point:  # create a new class for points
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):  # define string representation for Point objects
        return f"({self.x}, {self.y})"  # format as (x, y)

def merge(arr, left, mid, right): # declare merge sort algorithm
    temp = [0] * (right - left + 1) # temporary array for merging
    i, j, k = left, mid + 1, 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i] # copy left half element
            k += 1
            i += 1
        else:
            temp[k] = arr[j] # copy right half element
            k += 1
            j += 1

    while i <= mid:
        temp[k] = arr[i] # copy remaining elements from left half
        k += 1
        i += 1

    while j <= right:
        temp[k] = arr[j] # copy remaining elements from right half
        k += 1
        j += 1

    for m in range(len(temp)):
        arr[left + m] = temp[m] # copy back the merged elements

def mergeSort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        mergeSort(arr, left, mid) # recursively sort left half
        mergeSort(arr, mid + 1, right) # recursively sort right half
        merge(arr, left, mid, right) # merge the sorted halves

def maxSubArray(arr):  # declare maxSubArray algorithm
    max_sum = -sys.maxsize  # initialize max_sum to negative infinity
    current_sum = 0
    start = end = s = 0

    for i in range(len(arr)):  # loop through the array
        current_sum += arr[i]  # increase sum by element at arr[i]
        if max_sum < current_sum:  # update max_sum if current_sum is greater
            max_sum = current_sum
            start = s
            end = i
        if current_sum < 0:  # reset current_sum if it drops below zero
            current_sum = 0
            s = i + 1  # update start index for the next subarray

    return max_sum, start, end  # return maximum sum and indices

def findAvg(arr):  # declare findAvg function
    total = sum(arr)  # set total equal to the sum of all elements in the array
    return total / len(arr)  # return average

def printArray(arr):  # declare printArray function
    print(" ".join(map(str, arr)))  # print array elements

def sort_points_by_x(points):  # declare sort_points_by_x function
    return sorted(points, key=lambda point: point.x)  # sort by x coordinate

def sort_points_by_y(points):  # declare sort_points_by_y function
    return sorted(points, key=lambda point: point.y)  # sort by y coordinate

def dist(p1, p2):  # declare dist function
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) # euclidean distance formula

def brute_force(points):  # brute force approach to find minimum distance
    min_distance = float('inf')  # initialize to infinity
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            min_distance = min(min_distance, dist(points[i], points[j]))  # update min_distance
    return min_distance

def strip_closest(strip, size, d):  # find the closest points in the strip
    min_distance = d  # initialize min_distance as d
    for i in range(size):
        for j in range(i + 1, size):
            if (strip[j].y - strip[i].y) < min_distance:  # check y coordinate difference
                min_distance = min(min_distance, dist(strip[i], strip[j]))  # update min_distance
    return min_distance

def closest_util(px, py):  # declare closest_util function
    n = len(px)
    if n <= 3:  # if n less than or equal to 3 (base case)
        return brute_force(px)

    mid = n // 2
    mid_point = px[mid]  # middle point for dividing

    pyl = []  # points on the left of the midline
    pyr = []  # points on the right of the midline
    for point in py:
        if point.x <= mid_point.x:
            pyl.append(point)  # add to left list
        else:
            pyr.append(point)  # add to right list

    dl = closest_util(px[:mid], pyl)  # closest distance on left
    dr = closest_util(px[mid:], pyr)  # closest distance on right
    d = min(dl, dr)  # find the minimum distance

    # create a list of points close to the midline
    strip = [point for point in py if abs(point.x - mid_point.x) < d]
    return min(d, strip_closest(strip, len(strip), d))  # return minimum distance

def closest(points):  # declare closest function
    px = sorted(points, key=lambda p: p.x)  # sort by x coordinate
    py = sorted(points, key=lambda p: p.y)  # sort by y coordinate
    return closest_util(px, py)  # call the helper function

def plotData(arr, anomalies, max_profit_period):
    plt.figure(figsize=(12, 6))  # create a new figure
    plt.plot(arr, label='Stock Prices', marker='o')  # plot stock prices

    if anomalies:  # check if anomalies exist
        anomaly_indices, anomaly_values = zip(*anomalies)
        plt.scatter(anomaly_indices, anomaly_values, color='red', label='Anomalies', zorder=5)

    if max_profit_period:  # highlight max profit period
        start, end = max_profit_period[1], max_profit_period[2]
        plt.axvspan(start, end, color='green', alpha=0.3, label='Max Profit Period')

    # initialize plot
    plt.title('Stock Prices Over Time')
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    print("Stock Market Price Analyzer.")
    arr = [38, 27, 43, 3, 9, 82, 10] # example usage
    print("Stock market prices at the end of each trading day: ", end="")
    printArray(arr)

    mergeSort(arr.copy(), 0, len(arr) - 1)
    print("\nStock prices in ascending order: ", end="")
    printArray(arr)

    max_sum, start, end = maxSubArray(arr)
    print("\nMaximum subarray sum is:", max_sum)
    print(f"Period with max profit is from day {start} to day {end}.")

    averageValue = findAvg(arr)
    print("\nStock Average:", averageValue)

    anomalies = [(i, value) for i, value in enumerate(arr) if value < averageValue - 10 or value > averageValue + 10]

    points = [Point(i + 1, value) for i, value in enumerate(arr)]

    sorted_by_x = sort_points_by_x(points.copy())
    sorted_by_y = sort_points_by_y(points.copy())

    print("\nSorted by X: ")
    printArray(sorted_by_x)

    print("\nSorted by Y: ")
    printArray(sorted_by_y)

    min_distance = closest(points)
    print("\nThe smallest distance between points is:", min_distance)

    plotData(arr, anomalies, (max_sum, start, end))

if __name__ == "__main__":
    main()
