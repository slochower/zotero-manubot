# pip install pyzotero
from pyzotero import zotero
import subprocess
import argparse

# From https://www.zotero.org/settings/keys
library_id = "YOUR LIBRARY ID HERE"

# From https://www.zotero.org/settings/keys/new
api_key = "YOUR API KEY HERE"
library_type = "user"


def get_doi(item):
    if "DOI" not in item["data"].keys():
        return None
    if item["data"]["DOI"] == "":
        return None
    if "," in item["data"]["DOI"]:
        return "doi:" + item["data"]["DOI"].split(",")[0]
    else:
        return "doi:" + item["data"]["DOI"]


def get_isbn(item):
    if "ISBN" not in item["data"].keys():
        return None
    else:
        return "isbn:" + item["data"]["ISBN"]


def get_url(item):
    if "url" not in item["data"].keys():
        return None
    else:
        return "url:" + item["data"]["url"]


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--tag", help="Zotero library tag", required=False)
    ap.add_argument("-q", "--query", help="Zotero library query", required=False)
    ap.add_argument("-o", "--output", help="Formatted output file", required=True)

    args = vars(ap.parse_args())

    zot = zotero.Zotero(library_id, library_type, api_key)
    if args["tag"]:
        zot.add_parameters(tag=args["tag"], sort="date")
    elif args["query"]:
        zot.add_parameters(q=args["query"], sort="date")
    else:
        raise NotImplementedError

    items = zot.items()
    string_of_identifiers = ""

    for item in items:
        title = item["data"]["title"]
        identifer = get_doi(item)
        if not identifer:
            identifer = get_isbn(item)
        if not identifer:
            identifer = get_url(item)
        if not identifer:
            print(f"{title[0:30]:<40}... Error finding DOI, ISBN, or URL for item.")
            continue

        print(f"{title[0:30]:<40}... {identifer}")
        string_of_identifiers += identifer
        string_of_identifiers += " "

    command = f"""
    manubot \
    cite \
    --render \
    --format markdown \
    {string_of_identifiers} \
    > {args['output']}
    """
    subprocess.call(command, shell=True)
