"""
======
Input: yield curve
Output: zero curve
======
"""

import math
from datetime import date
import collections

class BootstrapZeroCurve(object):

    def __init__(self):
        self.instruments = dict()
        self.zero_curve = dict()

    def add_instrument(self, T, rate, zero_conpon):
        self.instruments[T] = (rate, zero_conpon)

    def add_zero(self, T, rate):
        self.zero_curve[T] = (rate)

    def bootstrapping():
        for T in self.instruments




if __name__ == "__main__":

    valuation_date = date(2016, 9, 2)

    print("initial instrument curve ...")
    zero_curve = BootstrapZeroCurve()
    zero_curve.add_instrument(date(2016,9,16), 0.9909, True)
    zero_curve.add_instrument(date(2016,12,16), 0.99065, True)
    zero_curve.add_instrument(date(2017,3,16), 0.9906, True)
    zero_curve.add_instrument(date(2017,6,17), 0.99055, True)
    zero_curve.add_instrument(date(2017,9,17), 0.9905, True)
    zero_curve.add_instrument(date(2017,12,17), 0.9904, True)
    zero_curve.add_instrument(date(2018,9,2), 0.9476, False)
    zero_curve.add_instrument(date(2019,9,2), 0.9619, False)
    zero_curve.add_instrument(date(2020,9,2), 0.9796, False)
    zero_curve.add_instrument(date(2021,9,2), 1.0031, False)
    zero_curve.add_instrument(date(2022,9,2), 1.0372, False)
    zero_curve.add_instrument(date(2023,9,2), 1.0888, False)

    print("creating zero curve ...")
    zero_curve.bootstrapping()



    print("testing ...")
    od = collections.OrderedDict(sorted(zero_curve.instruments.items()))

    for T in od.keys():
        if(zero_curve.instruments[T][1]):
            print((T - valuation_date).days/365," - True - ",zero_curve.instruments[T])
        else:
            print((T - valuation_date).days/365," - False - ",zero_curve.instruments[T])
