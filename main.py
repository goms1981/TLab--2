"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import window_max, window_average, window_stddev
from cleaner import filter_nondigits, filter_outliers

import matplotlib.pyplot as plt



def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics, 
    and save visualizations.
    

    
    Args:
        filename (str): The path to the data file (e.g., 'data/data1.txt').
        
    Steps:
        1. Read the file into a list of strings.
        2. Use `filter_nondigits` to clean the data and remove invalid entries.
        3. Use `filter_outliers` to remove unrealistic heart rate samples (<30 or >250).
        4. Calculate rolling maximums, averages, and standard deviations using functions from `metrics.py`.
        5. Save the plots to the `images/` folder:
            - Rolling maximums -> 'images/maximums.png'
            - Rolling averages -> 'images/averages.png'
            - Rolling standard deviations -> 'images/stdevs.png'

    Returns:
        list[int], list[int], list[int]: You will return the maximums, averages, and stdevs (in this order).
    """  
    
    data = []


    with open(filename) as file:
        data = file.read().splitlines()


    #clean the data and remove invalid entries
    data = filter_nondigits(data)
    #remove certain heart rate samples (<30 or >250).
    data = filter_outliers(data)


    #calculate rolling maximums, averages, and standard deviations using functions from `metrics.py`.
    maximums = window_max(data, 6) 
    averages = window_average(data, 6)
    stdevs = window_stddev(data, 6)


    #rounds averages and stdevs to 2 places
    for val in range(len(averages)):
        averages[val] = round(averages[val], 2)
    for val in range(len(stdevs)):
        stdevs[val] = round(stdevs[val], 2)


   
    #draw the plots
    plt.figure()
    plt.plot(maximums)
    plt.savefig("images/maximums.png")
    plt.close()

    plt.figure()
    plt.plot(averages)
    plt.savefig("images/averages.png")
    plt.close()

    plt.figure()
    plt.plot(stdevs)
    plt.savefig("images/stdevs.png")
    plt.close()


    # return all 3 lists
    return maximums, averages, stdevs

if __name__ == "__main__":
    run("data/data1.txt")
    run("data/data2.txt")
    run("data/data3.txt")
    run("data/data4.txt")
    run("data/data5.txt")
    run("data/data6.txt")