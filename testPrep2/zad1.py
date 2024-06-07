import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np

data = {'value': [], 'x': []}
xs = np.linspace(-3, 3, 13)

for i in range(13):
    data['value'].append(math.sin(xs[i]) * xs[i])
    data['x'].append(xs[i])

df = pd.DataFrame(data)
chart = df.plot(x='x', y='value', title='Wykres sinx * x')
chart.set_xlabel('x')
chart.set_ylabel('f(x)')
plt.show()