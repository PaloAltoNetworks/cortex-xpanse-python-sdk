# SDK Doc generate

## Install Dependencies
1. Install `requirements-docs.txt` using `pip install -r requirements-docs.txt`.

## Sphinx Sources
1. Run `make buildapi` from this directory.
2. You should see a bunch of new `.rst` docs in `docs/_source`.
3. Use these to generate human-readable docs with the commands below.

## HTML Docs
1. Run `make html` from this directory.
2. You should see a bunch of new html docs in `docs/_build/html`.
3. You can open in your local browser and see docs locally.

## PDF Docs
**Note: This has only been tested on macOS and requires mactex**
1. Run `make latexpdf` from this directory
2. Open `_build/latex/xpanse.pdf`