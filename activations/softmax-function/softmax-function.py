import numpy as np

def softmax(x,temp=1.0):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    if temp <= 0:
        raise ValueError("Temperature must be positive")

    # x = np.asarray(x)

    if x.ndim == 1:
        # 1D case
        x_scaled = x / temp
        x_shifted = x_scaled - np.max(x_scaled)
        exp_x = np.exp(x_shifted)
        return exp_x / np.sum(exp_x)

    elif x.ndim == 2:
        # 2D case (row-wise softmax)
        x_scaled = x / temp
        x_shifted = x_scaled - np.max(x_scaled, axis=1, keepdims=True)
        exp_x = np.exp(x_shifted)
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)

    else:
        raise ValueError("Input must be a 1D or 2D NumPy array")
    


