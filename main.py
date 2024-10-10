import sys
import matplotlib.pyplot as plt

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
    total = sum(arr) #total equals sum of every element in array
    return total / len(arr) #average equals total divided by length

def printArray(arr): # Function to print the array
    print(" ".join(map(str, arr)))

def findAnomalies(avg, arr):
    anomalies = [] #create list for anomalies
    for i in range(len(arr)): #for the length of the list
        if (arr[i] / avg) < 0.70 or (arr[i] / avg) > 1.3: #if selected index is 30% > or < then
            anomalies.append((i, arr[i]))  # Store index and value
    return anomalies #return the list

def plotData(arr, anomalies, max_profit_period):
    plt.figure(figsize=(12, 6))
    plt.plot(arr, label='Stock Prices', marker='o')

    # Highlight anomalies
    if anomalies:
        anomaly_indices, anomaly_values = zip(*anomalies)
        plt.scatter(anomaly_indices, anomaly_values, color='red', label='Anomalies', zorder=5)

    # Highlight maximum profit period
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
    arr = [38, 27, 43, 3, 9, 82, 10]  # Example usage
    print("Stock market prices at the end of each trading day: ", end="")
    printArray(arr)  # print original array

    mergeSort(arr, 0, len(arr) - 1)  # sort the algorithm
    print("\nStock prices in ascending order: ", end="")
    printArray(arr)  # print sorted array

    max_sum, start, end = maxSubArray(arr)
    print("\nMaximum subarray sum is:", max_sum)
    print(f"Period with max profit is from day {start+1} to day {end+1}.")

    averageValue = findAvg(arr)
    print("\nStock Average:", averageValue)

    anomalies = findAnomalies(averageValue, arr)
    print("\nDetected anomalies (30 Percent Greater or Less than average):", end=" ")
    printArray([v for _, v in anomalies])

    plotData(arr, anomalies, (max_sum, start, end)) # Plotting results

if __name__ == "__main__":
    main()  # end program