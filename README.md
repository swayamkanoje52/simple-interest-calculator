# Simple Interest Calculator

A Python-based application to calculate simple interest and total amount based on principal, rate of interest, and time period.

## 📋 Description

This Simple Interest Calculator is a user-friendly command-line application that helps you calculate simple interest using the mathematical formula:

```
Simple Interest = (Principal × Rate × Time) / 100
Total Amount = Principal + Simple Interest
```

The application validates user input and displays results in a formatted, easy-to-read manner.

## 🎯 Features

- **Calculate Simple Interest**: Computes simple interest for given principal, rate, and time
- **Calculate Total Amount**: Automatically calculates the total amount (principal + interest)
- **Input Validation**: Validates that inputs are non-negative numbers
- **User-Friendly Interface**: Clear and formatted output with proper labels
- **Error Handling**: Handles invalid inputs gracefully with informative error messages
- **Function Library**: Provides reusable functions for integration into other projects

## 📂 Project Structure

```
simple-interest-calculator/
├── calculator.py           # Main application file
├── README.md              # This file
└── requirements.txt       # Python dependencies (if any)
```

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/simple-interest-calculator.git
   cd simple-interest-calculator
   ```

2. No installation steps needed - just run the script!

### Usage

Run the calculator with:

```bash
python calculator.py
```

#### Interactive Mode Example:

```
==================================================
    SIMPLE INTEREST CALCULATOR
==================================================

Enter Principal Amount (P): ₹ 10000
Enter Annual Interest Rate (R) in %: 5
Enter Time Period (T) in Years: 2

==================================================
CALCULATION RESULTS:
==================================================
Principal Amount    : ₹ 10,000.00
Annual Interest Rate: 5% p.a.
Time Period         : 2 years
--------------------------------------------------
Simple Interest     : ₹ 1,000.00
Total Amount        : ₹ 11,000.00
==================================================
```

## 💻 Using as a Library

You can also import and use the calculator functions in your own Python projects:

```python
from calculator import calculate_simple_interest, calculate_total_amount

# Calculate simple interest
interest = calculate_simple_interest(principal=10000, rate=5, time=2)
print(f"Interest: ₹{interest}")  # Output: Interest: ₹1000.0

# Calculate total amount
total = calculate_total_amount(principal=10000, rate=5, time=2)
print(f"Total Amount: ₹{total}")  # Output: Total Amount: ₹11000.0
```

## 📝 Formula

**Simple Interest Formula:**
```
SI = (P × R × T) / 100

Where:
- P = Principal (Initial Amount)
- R = Rate of Interest (per annum, in percentage)
- T = Time Period (in years)
```

**Total Amount Formula:**
```
A = P + SI

Where:
- A = Total Amount
- P = Principal
- SI = Simple Interest
```

## 🧪 Examples

### Example 1: Monthly Savings
- Principal: ₹5,000
- Rate: 4% p.a.
- Time: 3 years
- Simple Interest: ₹600
- Total Amount: ₹5,600

### Example 2: Investment
- Principal: ₹50,000
- Rate: 6% p.a.
- Time: 5 years
- Simple Interest: ₹15,000
- Total Amount: ₹65,000

## ✅ Input Validation

The calculator includes validation for:
- Negative values (Principal, Rate, Time cannot be negative)
- Non-numeric inputs
- Any other unexpected errors

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as an educational project to demonstrate:
- Python programming fundamentals
- Function definition and reusability
- Input/Output operations
- Error handling
- Documentation best practices

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report issues
- Submit pull requests
- Suggest improvements

## 📞 Contact

For questions or feedback about this project, please open an issue on the GitHub repository.

---

**Note:** This is a simple interest calculator. It does NOT calculate compound interest. For compound interest calculations, please refer to compound interest calculators.

Typo fix: added line for merge test.
