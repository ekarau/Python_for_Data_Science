import sys

def main():
    try :
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 1:
            print("")
            return 0
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1
    else :
        try :
            num = int(sys.argv[1])
            if num % 2 == 0:
                print("I'm Even.")
                return 0
            else :
                print("I'm Odd.")
                return 0
        except ValueError:
            print("AssertionError: argument is not an integer")
            return 1            

if __name__ == "__main__":
    main()