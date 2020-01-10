import comcrawl as cc
from pprint import pprint


def test_comcrawl():
    results = cc.search("https://index.commoncrawl.org/*", indexes=["2019-51"])

    assert results.shape == (3, 12)

    print("\n")
    print(f"Shape: {results.shape}")
    print(results)

    results = results.sort_values(by="timestamp")
    results = results.drop_duplicates("urlkey", keep="last")

    assert results.shape == (2, 12)

    print("\n")
    print(f"Shape: {results.shape}")
    print(results)

    results["html"] = cc.download(results)
    pprint(results["html"])
