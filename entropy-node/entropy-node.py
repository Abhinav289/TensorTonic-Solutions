import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    n = len(y)
    if n==0:
        return 0.0
    f_y = {}
    for l in y:
        if l not in f_y:
            f_y[l] = 1
        else:
            f_y[l] += 1
    
    
    # _,f_y = np.unique(y, return_counts= True)
    p,sum,h = 0.0,0.0,0.0
    
    
    for num in f_y.values():
    
        p = (num/n)
        
        sum = p*(np.log2(p))
        h += sum
    h = -h
    return float(h)
    
    
        
        



    print(f_y)