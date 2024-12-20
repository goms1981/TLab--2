## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

Missing values may be due to the sensor issue, loose fit of devices, or the machine not reading the data correctly. The risk of filtering these values out might be losing valuable data where we can find out in what certain conditions, the sensor might not work. 

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

Standard deviation in the context of heart rate means that if you have low standard deviation, there is less variation of the heart rate as it is stable around the average. If there is high standard deviation, there is more variation so there is spikes in heart rate. 

## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

These following x values are where I notice drastic increases/decreases.
x=5
x=10
x=20
x=25
x=40

At x = 5, I see a great increase where the average heart rate jumps from 65 to around 95. 

At x = 10, I see a decrease from about 93 beats to 80 beats. 

At x = 20, there is a slight increase from around 83 to 94 beats.

At x = 25, there is a medium decrease from 93 beats to around 80 beats again.

Lastly, at x = 40, there is a slight decrease from 90 beats to around 76 beats.

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

Yes, in the stdevs.png graph, it increases or decreases drastically whenever the averages.png graph does so. 
