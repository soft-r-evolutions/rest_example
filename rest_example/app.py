import sys
from rest_example import truth_is_out_there


def main():
    print(truth_is_out_there())
    return 0


if __name__ == "__main__":
    errorCode = main()
    sys.exit(errorCode)
