import matplotlib.pyplot
import requests
import time
import pandas
from matplotlib import pyplot as plt

articles = ["bruh", "bruh+moment", "Carlos+has+died", "Carlos+lives"]  # Fake, True, Fake, True
times = {}

try:
	df = pandas.read_csv("test")
except:
	for i in range(4):
		for j in range(100):
			print(j)
			start = time.time()
			response = requests.get("http://serve-sentiment-env.eba-vgm3gmfu.us-east-2.elasticbeanstalk.com/model?news=" + articles[i])
			end = time.time()
			if j == 0:
				times[articles[i]] = [end-start]
			else:
				times[articles[i]].append(end-start)

	df = pandas.DataFrame(times)
	df.to_csv("test")

df.boxplot(column=articles)
plt.xlabel("Article sentiment request time")
plt.ylabel("Time (s)")
plt.title("Article")
plt.show()
