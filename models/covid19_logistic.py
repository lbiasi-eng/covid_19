from scipy import optimize
import numpy as np
from datetime import datetime


class CovidLogistic:

    def fit(self, x_train, y_train):
        FMT = '%Y-%m-%dT%H:%M:%S'
        x_train = x_train.map(lambda x: (datetime.strptime(x, FMT) - datetime.strptime("2020-01-01T00:00:00", FMT)).days)
        popt, pcov  = optimize.curve_fit(self.logistic_model, x_train, y_train, p0=[2, 100, 20000], maxfev=2000)
        return x_train, popt

    def logistic_model(self, x, a, b, c):
        '''
        :param x: time
        :param a: a refers to the infection speed
        :param b: b is the day with the maximum infections occurred
        :param c: c is the total number of recorded infected people at the infection’s end
        :return:
        '''
        return c / (1 + np.exp(-(x - b) / a))

    def gompertz_model(self, x, k, c, r):
        return k * np.exp(c * np.exp(-r * x))
    