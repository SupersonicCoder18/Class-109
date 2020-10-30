import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import csv

df = pd.read_csv("Student.csv")
Height = df["Height(Inches)"].to_list()
Weight = df["Weight(Pounds)"].to_list()

HeightMean = statistics.mean(Height)
WeightMean = statistics.mean(Weight)

HeightMedian = statistics.median(Height)
WeightMedian = statistics.median(Weight)

HeightMode = statistics.mode(Height)
WeightMode = statistics.mode(Weight)

print("Mean, median, and mode of Height is {}, {}, {} respectively".format(HeightMean, HeightMedian, HeightMode))
print("Mean, median, and mode of Weight is {}, {}, {} respectively".format(WeightMean, WeightMedian, WeightMode))

fig = ff.create_distplot([Height], ["Height"], show_hist = False)
fig2 = ff.create_distplot([Weight], ["Weight"], show_hist = False)
fig.show()
fig2.show()

HeightStd = statistics.stdev(Height)
WeightStd = statistics.stdev(Weight)

print("Standard deviation of Height and Weight are {} and {} respectively".format(HeightStd, WeightStd))

HeightStd1Start, HeightStd1End = HeightMean - HeightStd, HeightMean + HeightStd
HeightStd2Start, HeightStd2End = HeightMean - ( 2* HeightStd), HeightMean + (2 * HeightStd)
HeightStd3Start, HeightStd3End = HeightMean - (3* HeightStd), HeightMean + (3* HeightStd)

WeightStd1Start, WeightStd1End = WeightMean - WeightStd, WeightMean + WeightStd
WeightStd2Start, WeightStd2End = WeightMean - ( 2* WeightStd), WeightMean + (2 * WeightStd)
WeightStd3Start, WeightStd3End = WeightMean - (3* WeightStd), WeightMean + (3* WeightStd)

WeightFirstStd = [result for result in Weight if result > WeightStd1Start and result < WeightStd1End]
WeightSecondStd = [result for result in Weight if result > WeightStd2Start and result < WeightStd2End]
WeightThirdStd = [result for result in Weight if result > WeightStd3Start and result < WeightStd3End]

HeightFirstStd = [result for result in Height if result > HeightStd1Start and result < HeightStd1End]
HeightSecondStd = [result for result in Height if result > HeightStd2Start and result < HeightStd2End]
HeightThirdStd = [result for result in Height if result > HeightStd3Start and result < HeightStd3End]

print("{} % of HeightData lies with FirstStd".format(len(HeightFirstStd)*100/len(Height)))
print("{} % of HeightData lies with SecondStd".format(len(HeightSecondStd)*100/len(Height)))
print("{} % of HeightData lies with ThirdStd".format(len(HeightThirdStd)*100/len(Height)))
print("{} % of WeightData lies with FirstStd".format(len(WeightFirstStd)*100/len(Weight)))
print("{} % of WeightData lies with SecondStd".format(len(WeightSecondStd)*100/len(Weight)))
print("{} % of WeightData lies with ThirdStd".format(len(WeightThirdStd)*100/len(Weight)))