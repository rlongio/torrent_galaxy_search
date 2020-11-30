import torrent_galaxy_search
import requests

from bs4 import BeautifulSoup
from torrent_galaxy_search.result import Result


def main():
    results = requests.get(
        "https://torrentgalaxy.to/torrents.php?search=tt4154796"
    ).text

    soup = BeautifulSoup(results, "html.parser")

    for link in soup.find_all("div", class_="tgxtablerow"):
        print(Result(str(link)))


if __name__ == "__main__":
    main()
