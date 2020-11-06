"""Console script for pony_sayz."""
import argparse
import sys


def main():
    """Console script for pony_sayz."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    #print("Arguments: " + str(args._))
    #print("Replace this message by putting your code into "
    #      "pony_sayz.cli.main")
    msg = args._[0]
    nr_traces = len(msg) + 4
    traces = '-' * nr_traces

    filepath = './data/ace.pony'
    line_nr = 1
    with open(filepath, encoding='utf-8') as fp:
        lines = fp.readlines()
        for line in lines:
            if line_nr > 21:
                if ('balloon5' in line):
                    print(traces)
                    print(line.replace('balloon5',args._[0]).replace('$',''))
                    print(traces)
                else:
                    print(line.replace('\n','').replace('$','')) 
            line_nr += 1

    return 0


def load_file():
    print('Load pony data file here.')


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
