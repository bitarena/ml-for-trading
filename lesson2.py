import pandas as pd

start_date="2010-01-22"
end_date="2010-01-22"

dates = pd.date_range(start_date, end_date)

df1 = pd.DataFrame(index=dates)

dfSPY = pd.read_csv("data/SPY.csv", index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])

# dfSPY.rename(columns={'Adj Close':'SPY'})

df1 = df1.join(dfSPY, how='inner')

# Clean NaN
df1 = df1.dropna()