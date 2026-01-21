import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x = np.asarray(x, dtype=float)


    if x.ndim == 0:
        x = x.reshape(1)

    y = np.tanh(x)

    
    eps = np.finfo(float).eps
    y = np.clip(y, -1 + eps, 1 - eps)

    return y

    