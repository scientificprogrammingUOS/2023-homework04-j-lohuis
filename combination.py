import numpy as np 

# implement your function to combine two numpy arrays 

def combination(arr1, arr2, axis=0):
    arr1 = np.squeeze(arr1)
    arr2 = np.squeeze(arr2)
    
    try:
        combined_array = np.concatenate((arr1, arr2), axis=axis)
    except ValueError as e:
        raise ValueError("Input arrays cannot be combined along the given axis.") from e
        
    return combined_array

if __name__ == "__main__":
    # use this for your own testing!

    pass
