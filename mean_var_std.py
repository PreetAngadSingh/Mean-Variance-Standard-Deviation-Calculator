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