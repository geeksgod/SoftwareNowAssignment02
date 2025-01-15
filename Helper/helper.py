def get_valid_float(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Input must be at least {min_value}. Please try again.")
            elif max_value is not None and value > max_value:
                print(f"Input must be at most {max_value}. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Input must be at least {min_value}. Please try again.")
            elif max_value is not None and value > max_value:
                print(f"Input must be at most {max_value}. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def is_in_range(char, start, end):
    return ord(start) <= ord(char) <= ord(end)