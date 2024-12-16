import statistics

def window_max(data: list, n: int) -> list:
    #window_max([1, 2, 3, 4, 5, 6, 7], 1)
    #[1,2,3,4,5,6,7]
    #window_max([1, 2, 3, 4, 5, 6, 7], 3)
    """
    Calculate maximum value of every "n"-size window
    
    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    maximums = []

    if not data or n <= 0:
        return []
    
    for i in range(0,len(data), n):
        window = data[i:i+n]
        window_max = max(window)
        maximums.append(window_max)

    return maximums


def window_average(data: list, n: int) -> list:
    """
    Calculates the average of an n-sized window over the given data.

    Args:
        data (list): A list of numerical values (integers or floats) to calculate the windowed averages from.
        n (int): The size of the window used to compute the averages.

    Returns:
        list: A list of average values, where each value represents the average of a window of size `n`.
              If the remaining data is smaller than `n`, its average is calculated and included.
    """
    result = []
    if not data or n <= 0:
        return []
    for i in range(0, len(data), n):
        window = data[i:i+n]
        window_average = sum(window)/len(window)
        result.append(window_average)

    return result



def window_stddev(data: list, n: int) -> list:
    """
    Calculates the standard deviation of n size window
    
    Args:
        data (list): A list of numerical values (integers or floats) to calculate the windowed standard deviations from.
        n (int): The size of the window used to compute the standard deviations.

    Returns:
        list: A list of standard deviation values, where each value represents the standard deviation of a window of size `n`.
              If a window contains fewer than two elements, it is skipped and not included in the result.
    """
    result = []
    if not data or n <= 0:
        return []
    for i in range(0, len(data), n):
        window = data[i:i+n]
        if len(window) >= 2:
            std_dev = statistics.stdev(window)
            result.append(round(std_dev, 2))

    return result
