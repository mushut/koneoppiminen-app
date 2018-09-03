# Program for building training, test and validation data sets
# Aki Sipovaara 2018

import csv

# Read csv file
def read_csv(filename):
    with open(filename, newline='') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=';')
        titles = next(data_reader)

        # Training data set

        # Validation data set

        # Test data set

        # For testing purposes
        return titles


def main():
    print('Build data set')
    # Tested printing titles of csv file
    print(read_csv('..\dataset\Online_Retail.csv'))


main()