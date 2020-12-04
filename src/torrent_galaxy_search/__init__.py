from typing import List
from torrent_galaxy_search.search import Search, Result


def main():
    results: List[Result] = Search.by_IMDB_ID("tt0095016")

    for r in results:
        print("----------------------")
        print(r.views)
        print(r.magnet_url)


if __name__ == "__main__":
    main()
