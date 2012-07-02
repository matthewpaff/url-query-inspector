# URL Query Lab

Inspect an HTTP(S) URL and decode its query parameters without fetching anything.

This original small project uses **Python 3.10+ and only its standard library**.
No packages, virtual environment, service, or network access are required.

## Run

From this repository directory:

```console
python url_query.py --help
python url_query.py "https://example.com/search?q=python+tips&tag=web&tag=reading"
python url_query.py --check-fixtures fixtures/cases.jsonl
python -m unittest discover -s tests -v
```

Repeated query keys retain their values in input order, and blank values are retained. Query keys sort in output. Plus signs decode to spaces; percent escapes must be valid UTF-8. Credentials, invalid ports, whitespace, and backslashes are rejected. At most 100 query fields and an 8192-character URL are accepted. This is an inspection exercise, not a browser URL validator or a security authorization mechanism.

Output is JSON (or a fixture-check summary). Exit codes are 0 for success,
1 for file failures, and 2 for invalid input. Errors go to stderr.
For file-based tools, `-` reads stdin. Use UTF-8 input files.

## Structure and branches

- `url_query_lab/core.py`: pure parsing or analysis logic.
- `url_query_lab/cli.py`: command arguments and file input/output.
- `url_query_lab/generate_fixtures.py`: deterministic original sample cases.
- `url_query_lab/fixture_check.py`: expected-result/error validation.
- `fixtures/cases.jsonl`: 366 synthetic cases, one added per artificial dated commit.
- `tests/`: independently chosen boundary cases plus corpus validation.

`feature/core` and `feature/cli` retain the corresponding development snapshots.
`data/synthetic-fixtures` marks the completed corpus; `docs/usage` and `main` contain
the final documentation and tests. There are no copied upstream commits.

## Generate examples

```console
python generate_fixtures.py --count 20
```

This prints reproducible JSONL and **does not create or date Git commits**. The
historical-looking Git timeline is a separate, documented simulation. Many cases
vary generated values; they do not imply separate design decisions or features.

Keep contributions focused, add a regression test for changed behavior, and run
the standard-library tests. Never add real private data or credentials. Record
actual dates for new work. Licensed under [MIT](LICENSE).

[History and provenance](HISTORY.md).
