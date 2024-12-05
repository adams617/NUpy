# mm_to_cc.py

INCHES_TO_MM = 25.4

def inches_to_mm(inches):
    """
    Convert inches to millimeters.
    
    Args:
        inches (float): The length in inches.
        
    Returns:
        float: The length in millimeters.
    """
    return round(inches * INCHES_TO_MM, 1)

def millimeters_to_cc(length, width, height):
    """
    Function: millimeters_to_cc(length, width, height)
    
    Given length & width in millimeters, and height in inches:
    return the volume of rainfall in cubic centimeters (cc), rounded to 1 decimal place.
    Result should be NON-NEGATIVE values only.
    
    Args:
        length (float): The length of the container in millimeters.
        width (float): The width of the container in millimeters.
        height (float): The height of the rainfall in inches.
        
    Returns:
        float: The volume of rainfall in cubic centimeters.
    
    docTest:
    >>> millimeters_to_cc(1000, - ,500, 2)
    25400.0
    
    >>> millimeters_to_cc(1000, 500, 0)
    0.0
    """
    # Convert height from inches to millimeters
    height_mm = inches_to_mm(height)
    
    # Calculate the volume in cubic centimeters
    volume_cc = (length * width * height_mm) / 1000
    
    # Ensure the result is non-negative and round to 1 decimal place
    return round(max(volume_cc, 0), 1)

# Optional: You can include more helper functions here if necessary

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)




