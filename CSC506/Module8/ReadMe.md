# File Descriptions

[bubblysort.py](https://github.com/davidmvermillion/CSUGHomework/blob/main/CSC506/Module8/bubblysort.py) is a bidirectional bubble sorting algorithm \

[SampleGeneration.ipynb](https://github.com/davidmvermillion/CSUGHomework/blob/main/CSC506/Module8/SampleGeneration.ipynb) generates the associated pickle files with performance values for bidirectional bubble, heap, and merge sorting algorithms.

[SampleAnalysis.ipynb](https://github.com/davidmvermillion/CSUGHomework/blob/main/CSC506/Module8/SampleAnalysis.ipynb) generates the graphs showcasing the algorithm performances.

The three pickle files in [data](https://github.com/davidmvermillion/CSUGHomework/tree/main/CSC506/Module8/data) save the data for later to keep them out of memory. You can generate them yourself from the SampleGeneration notebook if you have concerns about cybersecurity in executing the hosted pickle files.

![Performance Comparison at 100 Iterations](https://github.com/davidmvermillion/CSUGHomework/tree/main/CSC506/Module8/PerformanceComparisonat100Iterations.png) shows the slightly-better-than $O(n^2)$ performance of bidirectional bubble sort while showing how much better the $nlogn$ algorithms perform. This is with each iteration growing the random sorting list size by $N*10$ until it reached a maximum size of 1,010 random integers.

![Performance Comparison at 1000 Iterations](https://github.com/davidmvermillion/CSUGHomework/tree/main/CSC506/Module8/PerformanceComparisonat100Iterations.png) shows the curve a little better. Not exactly linear, but not exactly $O(n^2)$, either. It also shows an interesting hiccup at around 500 iterations. Additionally, I noticed my notation mistake with the capitalized N that was fixed to a lower case n for this chart.