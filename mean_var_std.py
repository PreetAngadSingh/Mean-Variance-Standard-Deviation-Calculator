import numpy as np

def calculate(list):
    if len(list)<9:
        raise ValueError('List must contain nine numbers.')
    else:
        x = np.array(list).reshape(3, 3);

    mean = [x.mean(axis=0).tolist(),x.mean(axis=1).tolist(),x.mean()]
    variance = [x.var(axis=0).tolist(),x.var(axis=1).tolist(),x.var()]
    std_dev = [x.std(axis=0).tolist(),x.std(axis=1).tolist(),x.std()]
    maximum = [x.max(axis=0).tolist(),x.max(axis=1).tolist(),x.max()]
    minimum = [x.min(axis=0).tolist(),x.min(axis=1).tolist(),x.min()]
    sumCal = [x.sum(axis=0).tolist(),x.sum(axis=1).tolist(),x.sum()]

    calculations = {
        'mean' : mean,
        'variance' : variance,
        'standard deviation': std_dev,
        'max' : maximum,
        'min' : minimum,
        'sum' : sumCal

    }

    return calculations

    {
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}