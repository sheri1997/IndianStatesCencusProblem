import csv

import pandas as pd
from IndianStatesCensusException import IndianStatesCensusException


class IndianStatesCensus:

    def state_census_problem(self, csv_data):
        '''This Method Is Used To Load
            The CSV File'''
        data = pd.read_csv(csv_data)
        print(data)

    def count_records(self, csv_data):
        '''This method is used to count
            the number of records present in the csv file'''
        data = pd.read_csv(csv_data)
        print(data.shape)

    def csv_file_correct(self, csv_data):
        data = open(csv_data, 'r')
        if data.name.endswith(".csv"):
            return data
        else:
            raise IndianStatesCensusException("Invalid File Name")

    def delimitor(self, csv_data):
        data = open(csv_data)
        sniffer = csv.Sniffer()
        sniff_data = sniffer.sniff(data.read())
        if not sniff_data.delimiter == ',':
            raise IndianStatesCensusException("Delimitor Not Matched")
        else:
            return sniff_data.delimiter


if __name__ == '__main__':
    csv_data = IndianStatesCensus()
    file = 'D:/BrizePython/IndianStatesCencusProblem/IndianCensus - Sheet1.csv'
    print(csv_data.count_records(file))
    print(csv_data.csv_file_correct(file))
    print(csv_data.delimitor(file))

