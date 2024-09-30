# test_conversions.py

from conversions import inches_to_mm, feet_to_fathom

def test_inches_to_mm(inches, expected):
    """
    Test the conversion from inches to millimeters.
    
    Args:
        inches (float): The length in inches to convert.
        expected (float): The expected length in millimeters.
        
    Returns:
        None: Prints the actual and expected results.
    """
    actual = inches_to_mm(inches)
    print(f"Testing inches to mm: {inches} inches is {actual} mm (expected: {expected} mm)")

def test_feet_to_fathoms(feet, expected):
    """
    Test the conversion from feet to fathoms.
    
    Args:
        feet (float): The length in feet to convert.
        expected (float): The expected length in fathoms.
        
    Returns:
        None: Prints the actual and expected results.
    """
    actual = feet_to_fathom(feet)
    print(f"Testing feet to fathoms: {feet} feet is {actual} fathoms (expected: {expected} fathoms)")

def main():
    """
    Main function to run the test cases for conversion functions.
    
    Returns:
        None
    """
    # Test cases for inches to millimeters
    test_inches_to_mm(-24, 25.4)
    test_inches_to_mm(10, 254.0)
    test_inches_to_mm(0.5, 12.7)
    
    # Test cases for feet to fathoms
    test_feet_to_fathoms(6, 178.0)
    test_feet_to_fathoms(12, 2.0)
    test_feet_to_fathoms(3, 45.5)

if __name__ == "__main__":
    main()
