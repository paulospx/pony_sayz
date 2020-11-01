"""Console script for pony_sayz."""
import argparse
import sys


def main():
    """Console script for pony_sayz."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "pony_sayz.cli.main")

    
    return 0


def load_file():
    print('Load pony data file here.')


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
