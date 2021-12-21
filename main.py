import pandas as pd


def state_census_problem():
    csv_data = pd.read_csv('D:/BrizePython/IndianStatesCencusProblem/IndianCensus - Sheet1.csv')
    print(csv_data.shape)
    print(csv_data)


data = state_census_problem()

print(data)

