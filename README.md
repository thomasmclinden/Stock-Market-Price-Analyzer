# Stock Market Price Analyzer

## Overview

This Python project analyzes stock market prices and provides useful insights such as sorting stock prices, detecting anomalies, identifying the maximum profit period, and finding the closest points between two data points. It also includes data visualization to help understand the stock price trends and anomalies.

### Libraries Used:

- **Matplotlib**: For plotting graphs and visualizing stock prices.
- **Math**: For mathematical operations, including calculating Euclidean distance between points.
- **Sys**: For handling large numbers and system-specific parameters.

---

## Features

### 1. Stock Price Sorting
This tool sorts stock prices using the **Merge Sort** algorithm to organize the prices in ascending order. It provides a sorted list of stock prices at the end of each trading day.

### 2. Max Subarray Sum (Maximum Profit)
The program calculates the maximum sum of a subarray of stock prices and determines the period with the maximum profit. This helps identify the best days to buy and sell for maximum profit.

### 3. Anomaly Detection
Anomalies are detected by identifying prices that significantly deviate from the average stock price. Anomalous data points are visualized using a scatter plot on the stock price graph.

### 4. Computational Geometry
The program includes a function to find the smallest distance between two points in a list of points. This uses a **Divide and Conquer** approach for efficiently finding the closest pair of points.

### 5. Data Visualization
The application uses **matplotlib** to plot the stock prices over time. Anomalies and the maximum profit period are highlighted to provide better insights into stock trends.

---

## Code Walkthrough

### Main Sections of the Code

1. **Libraries and Setup**:
   - The code uses `matplotlib` for plotting graphs and visualizations, `math` for calculating Euclidean distance between points, and `sys` for handling system-specific values.
   - The `Point` class represents a point on the graph with `x` and `y` coordinates.

2. **Stock Price Sorting**:
   - The stock prices are sorted using the **Merge Sort** algorithm. This algorithm divides the list of prices into two halves and recursively sorts them.

3. **Max Subarray Sum**:
   - The **Kadane's Algorithm** is used to find the maximum subarray sum, which helps in determining the best time to buy and sell the stock for maximum profit.

4. **Anomaly Detection**:
   - Anomalies are detected if a stock price is significantly above or below the average price. These anomalies are marked on the stock price chart.

5. **Computational Geometry**:
   - A divide-and-conquer approach is used to find the closest pair of points in the dataset. This is useful when analyzing the distance between two points in a stock price graph or dataset.

6. **Data Visualization**:
   - The stock prices, anomalies, and maximum profit period are visualized using **matplotlib**. The stock prices are plotted as a line graph, anomalies are shown as red dots, and the maximum profit period is highlighted.

---

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**:
   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/stock-market-analyzer.git

2. **Install the required libraries**:
   Install the Required Libraries: Install the necessary Python libraries using pip:
   ```bash
   pip install matplotlib

3. **After setting up the environment, run the program with the following command**:
    ```bash
   python main.py
---
## Example Code

```python
import sys
import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

def merge(arr, left, mid, right):
    temp = [0] * (right - left + 1)
    i, j, k = left, mid + 1, 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1

    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    for m in range(len(temp)):
        arr[left + m] = temp[m]

def mergeSort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def maxSubArray(arr):
    max_sum = -sys.maxsize
    current_sum = 0
    start = end = s = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        if max_sum < current_sum:
            max_sum = current_sum
            start = s
            end = i
        if current_sum < 0:
            current_sum = 0
            s = i + 1

    return max_sum, start, end

def findAvg(arr):
    total = sum(arr)
    return total / len(arr)

def printArray(arr):
    print(" ".join(map(str, arr)))

def sort_points_by_x(points):
    return sorted(points, key=lambda point: point.x)

def sort_points_by_y(points):
    return sorted(points, key=lambda point: point.y)

def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def brute_force(points):
    min_distance = float('inf')
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            min_distance = min(min_distance, dist(points[i], points[j]))
    return min_distance

def strip_closest(strip, size, d):
    min_distance = d
    for i in range(size):
        for j in range(i + 1, size):
            if (strip[j].y - strip[i].y) < min_distance:
                min_distance = min(min_distance, dist(strip[i], strip[j]))
    return min_distance

def closest_util(px, py):
    n = len(px)
    if n <= 3:
        return brute_force(px)

    mid = n // 2
    mid_point = px[mid]

    pyl = []
    pyr = []
    for point in py:
        if point.x <= mid_point.x:
            pyl.append(point)
        else:
            pyr.append(point)

    dl = closest_util(px[:mid], pyl)
    dr = closest_util(px[mid:], pyr)
    d = min(dl, dr)

    strip = [point for point in py if abs(point.x - mid_point.x) < d]
    return min(d, strip_closest(strip, len(strip), d))

def closest(points):
    px = sorted(points, key=lambda p: p.x)
    py = sorted(points, key=lambda p: p.y)
    return closest_util(px, py)

def plotData(arr, anomalies, max_profit_period):
    plt.figure(figsize=(12, 6))
    plt.plot(arr, label='Stock Prices', marker='o')

    if anomalies:
        anomaly_indices, anomaly_values = zip(*anomalies)
        plt.scatter(anomaly_indices, anomaly_values, color='red', label='Anomalies', zorder=5)

    if max_profit_period:
        start, end = max_profit_period[1], max_profit_period[2]
        plt.axvspan(start, end, color='green', alpha=0.3, label='Max Profit Period')

    plt.title('Stock Prices Over Time')
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    print("Stock Market Price Analyzer.")
    arr = [38, 27, 43, 3, 9, 82, 10]
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
