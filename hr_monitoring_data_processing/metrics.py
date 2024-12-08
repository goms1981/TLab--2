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
        window=data[i:i+n]
        window_max = max(window)
        maximums.append(window_max)

    return maximums


def window_average(data: list, n: int) -> list:
    result=[]
    if not data or n <= 0:
        return []
    for i in range(0, len(data), n):
        window=data[i:i+n]
        window_average=sum(window)/len(window)
        result.append(window_average)

    return result



def window_stddev(data: list, n: int) -> list:
    result=[]
    if not data or n <= 0:
        return []
    for i in range(0, len(data), n):
        window=data[i:i+n]
        if len(window) >= 2:
            std_dev = statistics.stdev(window)
            result.append(round(std_dev, 2))

    return result
