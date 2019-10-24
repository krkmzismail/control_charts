#! /usr/bin/env python3

'''
Script to read a csv file and create XmR control charts.

The csv file should have two columns: index with label, data with label.

./control_charts_x_mr.py | tee x_mr.txt
'''

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from datasense import X, mR


def get_input():
    csvfile = input('File name of csv file to read? -> ')
    subgroup_size = int(input('Subgroup size?                 -> '))
    index_column = input('Name of index column?          -> ')
    # chart_data = pd.read_csv(csvfile, index_col=index_column).iloc[:, 0:]
    chart_data = pd.read_csv(csvfile, index_col=index_column)
    print('\n\nCSV file:     ', csvfile)
    print('Subgroup size:', subgroup_size)
    print('Index column: ', index_column)
    return subgroup_size, chart_data


def control_chart_x(x):
    x_chart_title = 'X Control Chart'
    x_chart_subtitle = 'Subtitle'
    x_chart_ylabel = 'Response (units)'
    x_chart_xlabel = 'Sample'
    print('\nd2', x._d2, sep=' = ')
    print('sigma(X)', x.sigma, sep=' = ')
    print('\nX chart')
    print('Upper control limit ', x.ucl, sep=' = ')
    print('Average moving range', x.mean, sep=' = ')
    print('Lower control limit ', x.lcl, sep=' = ')
    print(f'Sigma(X)', x.sigma, sep=' = ')
    for i in range(-3, 4):
        print(f'{i} Sigma', ' '.join(map(str, [x.sigmas[i]])), sep=' = ')
    ax = x.ax
    ax.set_title(x_chart_title + '\n' + x_chart_subtitle)
    ax.set_ylabel(x_chart_ylabel)
    ax.set_xlabel(x_chart_xlabel)
    ax.figure.savefig('x.svg', format='svg')
    plt.clf()


def control_chart_mr(x):
    mr_chart_title = 'mR Control Chart'
    mr_chart_subtitle = 'Subtitle'
    mr_chart_ylabel = 'Response (units)'
    mr_chart_xlabel = 'Sample'
    print('\nd2', mr._d2, sep=' = ')
    print('d3', mr._d3, sep=' = ')
    print('sigma(mR)', mr.sigma, sep=' = ')
    print('\nmR chart')
    print('Upper control limit ', mr.ucl, sep=' = ')
    print('Average moving range', mr.mean, sep=' = ')
    print('Lower control limit ', mr.lcl, sep=' = ')
    print(f'Sigma(X)', mr.sigma, sep=' = ')
    for i in range(-3, 4):
        print(f'{i} Sigma', ' '.join(map(str, [mr.sigmas[i]])), sep=' = ')
    ax = mr.ax
    ax.set_title(mr_chart_title + '\n' + mr_chart_subtitle)
    ax.set_ylabel('Response (units)')
    ax.set_xlabel('X axis label')
    ax.figure.savefig('mr.svg', format='svg')
    plt.clf()


if __name__ == '__main__':
    subgroup_size, chart_data = get_input()
    x = X(chart_data, subgroup_size)
    mr = mR(chart_data, subgroup_size)
    control_chart_x(x)
    control_chart_mr(x)
