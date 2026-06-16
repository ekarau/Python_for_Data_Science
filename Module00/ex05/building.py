import sys

def print_usage(space_count, upper_count, lower_count, digit_count, punctuation_count):
    """Prints the usage statistics of the text."""
    sum = space_count + upper_count + lower_count + digit_count + punctuation_count
    print(f"The text contains {sum} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")

def text_calculator():
    """Calculates the usage statistics of the text provided as an argument or input."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 1:
            text = input("What is the text to count?\n")
        else:
            text = sys.argv[1]
        space_count = 0
        upper_count = 0
        lower_count = 0
        digit_count = 0
        punctuation_count = 0
        for c in text:
            if c.isupper():
                upper_count += 1
            elif c.islower():
                lower_count += 1
            elif c.isdigit():
                digit_count += 1
            elif c.isspace():
                space_count += 1
            else:
                punctuation_count += 1
        print_usage(space_count, upper_count, lower_count, digit_count, punctuation_count)
        return 0
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1
    except EOFError:
        print("EOFError")
        return 1

if __name__ == "__main__":
    text_calculator()