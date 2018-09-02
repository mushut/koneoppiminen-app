# Program for building training, test and validation datasets
# Aki Sipovaara 2018

import csv


def read_csv(filename):
    with open(filename, newline='') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=';')
        titles = next(data_reader)

        return titles


def main():
    print('Test')
    print(read_csv('..\dataset\Online_Retail.csv'))


main()