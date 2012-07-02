"""Original synthetic URL cases, using reserved example domains and no network."""
import argparse
import json


def make_case(index):
    label = "synthetic-url-{:04d}".format(index)
    path = "/sample/{}".format(index)
    url = "https://example.com" + path + "?tag=python&tag=web&q=case+{}&empty=#notes".format(index)
    kind = index % 12
    if kind == 0:
        url = "file:///sample/{}".format(index)
    elif kind == 1:
        url = "https://user:secret@example.com" + path
    elif kind == 2:
        url = "https://example.com:99999" + path
    elif kind == 3:
        url += " bad space"
    elif kind == 4:
        url = "https://example.com" + path + "?q=%GG"
    elif kind == 5:
        url = "https://example.com" + path + "?q=%FF"
    else:
        return {"id": label, "input": url, "expected": {"scheme": "https", "host": "example.com", "port": 443,
            "path": path, "fragment": "notes", "query": {"tag": ["python", "web"], "q": ["case {}".format(index)], "empty": [""]}}}
    return {"id": label, "input": url, "expected_error": True}


def main():
    parser = argparse.ArgumentParser(description="Print synthetic URL cases as JSONL.")
    parser.add_argument("--count", type=int, default=20)
    args = parser.parse_args()
    if not 1 <= args.count <= 10000:
        parser.error("Count must be between 1 and 10000")
    for index in range(args.count):
        print(json.dumps(make_case(index), ensure_ascii=True, sort_keys=True))


if __name__ == "__main__":
    main()
