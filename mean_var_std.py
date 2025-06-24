import numpy as np


def calculate(numbers):
 
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    m = np.array(numbers).reshape(3, 3)

    # Helper to avoid repetitive code
    def stats(func):

        return [func(m, axis=0).tolist(),
                func(m, axis=1).tolist(),
                func(m).item()]

    return {
        'mean':              stats(np.mean),
        'variance':          stats(np.var),
        'standard deviation': stats(np.std),
        'max':               stats(np.max),
        'min':               stats(np.min),
        'sum':               stats(np.sum)
    }
