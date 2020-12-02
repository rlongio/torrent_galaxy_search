from typing import List
import requests

from bs4 import BeautifulSoup
from torrent_galaxy_search.result import Result


def main():
    request_results = requests.get(
        "https://torrentgalaxy.to/torrents.php?search=tt4154796"
    ).text

    soup: BeautifulSoup = BeautifulSoup(request_results, "html.parser")

    results: List["Result"] = []
    for link in soup.find_all("div", class_="tgxtablerow"):
        results.append(Result(link))

    x = Result.sort(results, "sizee")
    for r in x:
        print(r)


if __name__ == "__main__":
    main()
