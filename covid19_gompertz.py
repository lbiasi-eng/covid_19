from scipy import optimize
import numpy as np
from datetime import datetime

class CovidGompertz:

    def fit(self, x_train, y_train):
        FMT = '%Y-%m-%dT%H:%M:%S'
        x_train = x_train.map(lambda x: (datetime.strptime(x, FMT) - datetime.strptime("2020-01-01T00:00:00", FMT)).days)
        popt, pcov = optimize.curve_fit(self.gompertz_model, x_train, y_train,maxfev=2000)
        print(popt)
        return x_train, popt

    def gompertz_model(self, x, a,b,c):
        return np.exp(a - b*(np.power(c, x)))

    def gompertz_model3(self,x, A, u, d, v, y0):
        """Gompertz growth model.

        Proposed in Zwietering et al., 1990 (PMID: 16348228)
        """
        y = (A * np.exp(-np.exp((((u * np.e) / A) * (d - x)) + 1))) + y0
        return y

    def gompertz_model2(self, x, k, c, r):
        return k * (np.exp(c * (np.exp(-r * x))))
