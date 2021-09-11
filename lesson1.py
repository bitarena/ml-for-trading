import pandas as pd

# import matplotlib.pyplot as plt
# df["High"].plot()
# plt.show()

def get_mean_volume(symbol: str):
    df = pd.read_csv("data/{}.csv".format(symbol))

    return df["Volume"].mean()

def get_max_close(symbol: str):
    df = pd.read_csv("data/{}.csv".format(symbol))

    return df["Close"].max()

def test_run():
    for symbol in ["AAPL", "IBM"]:
        print("Max Close")
        print(symbol, get_max_close(symbol))

        print("Mean Volume")
        print(symbol, get_mean_volume(symbol))

if __name__ == "__main__":
    test_run()