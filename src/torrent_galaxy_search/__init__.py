from torrent_galaxy_search.result import Result


def main():
    results = Result.search("tt0095016")

    for r in results:
        print("----------------------")
        print(r)
        print(r.magnet_url)


if __name__ == "__main__":
    main()
