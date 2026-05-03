"""
Simple Interest Calculator
A Python application to calculate simple interest given principal, rate, and time.
"""

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    
    Formula: Simple Interest = (P * R * T) / 100
    
    Args:
        principal (float): The principal amount (initial investment)
        rate (float): The annual interest rate (in percentage)
        time (float): The time period (in years)
    
    Returns:
        float: The calculated simple interest
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time cannot be negative")
    
    simple_interest = (principal * rate * time) / 100
    return simple_interest


def calculate_total_amount(principal, rate, time):
    """
    Calculate total amount (principal + interest).
    
    Args:
        principal (float): The principal amount (initial investment)
        rate (float): The annual interest rate (in percentage)
        time (float): The time period (in years)
    
    Returns:
        float: The total amount (principal + interest)
    """
    interest = calculate_simple_interest(principal, rate, time)
    total = principal + interest
    return total


def main():
    """Main function to run the simple interest calculator."""
    print("=" * 50)
    print("    SIMPLE INTEREST CALCULATOR")
    print("=" * 50)
    
    try:
        # Get user input
        principal = float(input("\nEnter Principal Amount (P): ₹ "))
        rate = float(input("Enter Annual Interest Rate (R) in %: "))
        time = float(input("Enter Time Period (T) in Years: "))
        
        # Calculate simple interest
        interest = calculate_simple_interest(principal, rate, time)
        total_amount = calculate_total_amount(principal, rate, time)
        
        # Display results
        print("\n" + "=" * 50)
        print("CALCULATION RESULTS:")
        print("=" * 50)
        print(f"Principal Amount    : ₹ {principal:,.2f}")
        print(f"Annual Interest Rate: {rate}% p.a.")
        print(f"Time Period         : {time} years")
        print("-" * 50)
        print(f"Simple Interest     : ₹ {interest:,.2f}")
        print(f"Total Amount        : ₹ {total_amount:,.2f}")
        print("=" * 50)
        
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please enter valid numerical values.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
