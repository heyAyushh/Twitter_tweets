import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()

verboseprint = print if args.verbose else lambda *a, **k: None 

verboseprint("gwllo")