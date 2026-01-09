def moles_to_grams(moles, molecular_weight):
    return moles * molecular_weight

def moles_to_kilograms(moles, molecular_weight):
    return moles_to_grams(moles, molecular_weight) / 1000

def moles_to_molecules(moles):
    avogadro_number = 6.022e+23
    return moles * avogadro_number

def moles_to_liters(moles):
    # Assuming STP conditions: 22.4 liters per mole
    return moles * 22.4

def calculate_molarity(moles, volume_liters):
    return moles / volume_liters

def print_options():
    print("Options:")
    print("1. Moles to Grams")
    print("2. Moles to Kilograms")
    print("3. Moles to Molecules")
    print("4. Moles to Liters (STP)")
    print("5. Calculate Molarity")

def print_welcome_message():
    print("Welcome to the Chemistry Conversion and Molarity Calculator!")
    print("This tool helps you convert chemical quantities and calculate molarity.")

def main():
    print_welcome_message()

    # Dictionary mapping user choice to corresponding conversion function
    conversion_functions = {
        1: moles_to_grams,
        2: moles_to_kilograms,
        3: moles_to_molecules,
        4: moles_to_liters,
        5: calculate_molarity
    }
    
    units = ['grams', 'kilograms', 'molecules', 'liters']

    while True:
        try:
            print_options()
            choice = int(input("Select an option (1-5): "))

            # Validate user's choice
            if choice not in conversion_functions:
                print("Invalid choice. Please choose a number between 1 and 5.")
                continue

            moles = float(input("Enter number of moles: "))
            
            # Handle different conversion options
            if choice in [1, 2]:
                molecular_weight = float(input("Enter molecular weight (g/mol): "))
                result = conversion_functions[choice](moles, molecular_weight)
                output = f"{result} {units[choice-1]}"
                
            elif choice in [3, 4]:
                result = conversion_functions[choice](moles)
                output = f"{result} {units[choice - 1]}"
                
            else:
                volume_liters = float(input("Enter solution volume (liters): "))
                result = conversion_functions[choice](moles, volume_liters)
                output = f"{result} mol/L"
                
            print(f"Result: {output}")

        except ValueError:
            print("Invalid input. Please enter numeric values only.")
    
        continue_program = input("Would you like to continue? (yes/no): ").lower()
        if continue_program != 'yes':
            print("Exiting the program. Thank you!")
            break
        
if __name__ == "__main__":
    main()