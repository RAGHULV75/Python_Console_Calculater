# Python_Console_Calculater
Terminal Based Calculater Using Python

The provided Python code defines a function called `cal()` that implements a simple calculator. Here's a breakdown of its functionality:

**Explanation:**

1. **Welcome Message:**
   - Prints a welcome message to the user.

2. **Menu:**
   - Prints a menu displaying available operations:
      - Addition (Press 1)
      - Subtraction (Press 2)
      - Multiplication (Press 3)
      - Division (Press 4)
      - Modulo (Press 5)

3. **User Input:**
   - Prompts the user to enter the first number (`a`).
   - Prompts the user to select an operation (1-5).
   - Prompts the user to enter the second number (`b`).

4. **Calculation:**
   - Based on the chosen operation (`option`):
      - Addition: Calculates `c = a + b`.
      - Subtraction: Calculates `c = a - b`.
      - Multiplication: Calculates `c = a * b`.
      - Division: Calculates `c = a / b`. (**Note:** Division by zero is not handled)
      - Modulo: Calculates `c = a % b`.
   - Prints the result (`c`).

5. **Looping:**
   - Prompts the user to enter 's' to restart the calculator or anything else to exit.
   - If 's' is entered:
      - Calls the `cal()` function again using recursion to restart the calculator.
   - If anything other than 's' is entered:
      - Prints a goodbye message and exits the program.

**Improvements:**

- **Error Handling:** The code can be improved by adding error handling for invalid user inputs (e.g., non-numeric input, division by zero).
- **Modularity:** The calculation logic can be separated into individual functions for each operation (add, subtract, multiply, etc.) for better code organization.
- **Welcome Message:** The welcome message can be enhanced to include information about supported operations or how to use the calculator.

Overall, this code provides a basic functional calculator. The suggested improvements can make it more robust and user-friendly. 


![image](https://github.com/RAGHULV75/Python_Console_Calculater/assets/168255383/1529a0e0-80a6-4de4-9e89-122e7b8fb918)
