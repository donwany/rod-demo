import argparse

def argpass():
    parser = argparse.ArgumentParser(description="Model Hyperparameters")
    parser.add_argument("--epochs", '-e', type=int, default=100, help='Number of epochs')
    parser.add_argument("--lr", '-l', type=float, default=0.0001, help='Learning rate')
    parser.add_argument("--model", '-m', type=str, default="LogisticRegression", help='Type of Model')
    #parser.add_argument("--output", '-o', type=argparse.FileType('w'), help='Output of model config')
    parser.add_argument("--square", '-s', type=int, help='calculate the square of a number')
    #parser.add_argument("--filename", '-f', type=str, help='Filename to save to')
    parser.add_argument("--verbosity", '-v', type=int, choices=[0, 1, 2], help='Logging levels')
    args = parser.parse_args()
    return args


def square(number: int):
    return number * number



# python app.py --epochs=10 --lr=0.05 --model="LogisticRegression"
# python app.py -ee=10 -l=0.05 -m="LogisticRegression"