import argparse
import json
import sys

from .core import inspect_url
from .fixture_check import check


def main(argv=None):
    parser = argparse.ArgumentParser(description="Inspect a URL and its query parameters without fetching it.")
    parser.add_argument("url", nargs="?")
    parser.add_argument("--check-fixtures", metavar="JSONL")
    args = parser.parse_args(argv)
    try:
        if args.check_fixtures:
            if args.url is not None:
                parser.error("Use a URL or --check-fixtures, not both")
            print("Verified {} synthetic fixtures.".format(check(args.check_fixtures, inspect_url)))
        else:
            if args.url is None:
                parser.error("Supply a URL")
            print(json.dumps(inspect_url(args.url), ensure_ascii=True, indent=2))
        return 0
    except ValueError as error:
        print("error: " + str(error), file=sys.stderr)
        return 2
    except OSError as error:
        print("error: " + str(error), file=sys.stderr)
        return 1
