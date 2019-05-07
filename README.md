# Quickly create Markdown bibliographies from Zotero using Manubot

## How it works

This script uses `pyzotero` and `manubot` to generate formatted bibliographies, given a search string and Zotero library. In particular, the script:

0. Establishes a connection to a user library using the Zotero API.
1. Searches the library using a tag or search query.
2. Looks for DOI, ISBN, or URL metadata -- in that order -- for each item in the library that matches the query.
3. Passes the list of DOI, ISBN, or URL identifiers to `manubot` and renders the citations as Markdown.

The following [terminal recording](https://asciinema.org/a/aQxeuXq7RW35lSDM1mezUR9TV?speed=2) demonstrates creating a bibliography of all papers tagged with "cyclodextrin" in my personal library, ordered by date.

![fetch_papers demonstration](media/fetch_papers..gif)

## Usage

```
usage: fetch_papers.py [-h] [-t TAG] [-q QUERY] -o OUTPUT

optional arguments:
  -h, --help            show this help message and exit
  -t TAG, --tag TAG     Zotero library tag
  -q QUERY, --query QUERY
                        Zotero library query
  -o OUTPUT, --output OUTPUT
                        Formatted output file
```

The main program will accept either a `tag` or general search `query` as input and a file name for the formatted bibliography. It shouldn't be hard to search by other formats accepted by the [`Zotero.add_parameters()`](https://pyzotero.readthedocs.io/en/latest/index.html?highlight=search#zotero.Zotero.add_parameters) function.

There may limitations on the number of results imposed by the API, as noted in the `pyzotero` documentation. No attempt is made to work around those limitations.

## Installation

1. Install `manubot` following the [instructions](https://github.com/manubot/manubot#installation) at the Manubot [repository](https://github.com/manubot/manubot).

2. Install `pyzotero` following the [instructions](https://github.com/urschrei/pyzotero#quickstart), paying attention to the steps necessary to get a **personal library ID** and **API key** from Zotero.

## Testing

There are no tests yet. This was written quickly, as a prototype, to be built upon.

To cite the Manubot project or for more information on its design and history, see:

> **Open collaborative writing with Manubot**
Daniel S. Himmelstein, Vincent Rubinetti, David R. Slochower, Dongbo Hu, Venkat S. Malladi, Casey S. Greene, Anthony Gitter
(2019-04-22) <https://greenelab.github.io/meta-review/>
