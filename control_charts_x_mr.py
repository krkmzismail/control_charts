#! /usr/bin/env python3

'''
Script to read a csv file and create XmR control charts.

The csv file should have two columns: index with label, data with label.

./control_charts_x_mr.py | tee x_mr.txt
'''

import pandas as pd
import matplotlib.pyplot as plt

from datasense import X, mR


def get_input():
    csvfile = input('File name of csv file to read? -> ')
    subgroup_size = int(input('Subgroup size?                 -> '))
    index_column = input('Name of index column?          -> ')
    chart_data = pd.read_csv(csvfile, index_col=index_column).iloc[:, 0:]
    print('\n\nCSV file:     ', csvfile)
    print('Subgroup size:', subgroup_size)
    print('Index column: ', index_column)
    return subgroup_size, chart_data


def control_chart_x(x):
    print('\nX chart')
    print('Upper control limit ', x.ucl, sep=' = ')
    print('Average moving range', x.mean, sep=' = ')
    print('Lower control limit ', x.lcl, sep=' = ')
    print(f'Sigma(X)', x.sigma, sep=' = ')
    for i in range(-3, 4):
        print(f'{i} Sigma', ' '.join(map(str, [x.sigmas[i]])), sep=' = ')
    ax1 = x.ax
    ax1.set_title('X control chart' + '\n' 'Subtitle')
    ax1.set_ylabel('Response (units)')
    ax1.set_xlabel('X axis label')
    ax1.figure.savefig('x.svg', format='svg')
    plt.clf()


def control_chart_mr(x):
    mr = mR(chart_data, subgroup_size)
    print('\nmR chart')
    print('Upper control limit ', mr.ucl, sep=' = ')
    print('Average moving range', mr.mean, sep=' = ')
    print('Lower control limit ', mr.lcl, sep=' = ')
    print(f'Sigma(X)', mr.sigma, sep=' = ')
    for i in range(-3, 4):
        print(f'{i} Sigma', ' '.join(map(str, [mr.sigmas[i]])), sep=' = ')
    ax2 = mr.ax
    ax2.set_title('mR control chart' + '\n' 'Subtitle')
    ax2.set_ylabel('Response (units)')
    ax2.set_xlabel('X axis label')
    ax2.figure.savefig('mr.svg', format='svg')
    plt.clf()


if __name__ == '__main__':
    subgroup_size, chart_data = get_input()
    x = X(chart_data, subgroup_size)
    control_chart_x(x)
    control_chart_mr(x)
