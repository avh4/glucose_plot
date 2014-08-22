import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

df = pd.read_csv('EGV_DATA.csv', index_col='display_time', parse_dates=True)
df = df.sort()

g = df[df.glucose > 20]['glucose']

print(df)

def daterange(data, number_of_days, end_days_ago=0):
  end_date = datetime.now() - timedelta(days=end_days_ago)
  start_date = end_date - timedelta(days=number_of_days-1)
  return g[start_date.date().isoformat():end_date.date().isoformat()]

def show_histogram(number_of_days, end_days_ago=0):
  data = daterange(g, number_of_days, end_days_ago)
  data.hist(bins=50)
  plt.show()

def show_modal_day(number_of_days, end_days_ago=0):
  days = range(end_days_ago, end_days_ago+number_of_days)
  gs = []
  for d in days:
    data = daterange(g, 1, d).groupby(lambda x: x.time()).agg(lambda s: s[0])
    gs.append(data)
  plt.figure()
  with pd.plot_params.use('x_compat', True):
    for gg in gs:
      gg.plot(style='D')
  plt.show()

show_histogram(7)

show_modal_day(7)
