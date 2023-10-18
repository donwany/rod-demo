import pandas as pd
from utils import argpass
from utils import square


args = argpass()

epochs = args.epochs
learning_rate = args.lr
model = args.model

sq = square(args.square)


config = {"epochs": epochs, "learning_rate": learning_rate, "model": model, "square": sq}

pd.DataFrame.from_dict([config]).to_csv("data.csv", index=False, header=True)

if __name__ == '__main__':
    print(config)