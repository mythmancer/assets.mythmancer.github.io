Static assets for Mythmancer

# DBs

Contains large json blobs we don't want or need floating around directly in the main JS of
mythmancer.com.

## Spells

All spells from [OSRIC Wiki](https://osricwiki.presgas.name/doku.php?id=osric:chapter2)

Parsed using [this script](https://github.com/mythmancer/mythmancer.github.io/blob/main/scripts/parse_spells_html.py)

### Differences from OSRIC

Mythmancer overrides and adds some concepts to the original spells from OSRIC.

The jsons will remain as-is, with an additional `mythmancer_overrides.json` serving
as a documentation of all ways in which we diverge from OSRIC.

The final spell database will be generated using these, and that will be what we finally use as
the asset
