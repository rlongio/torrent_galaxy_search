# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package


from typing import List
from bs4 import BeautifulSoup
from torrent_galaxy_search import Search, Result


class TestMain:
    def test_language(self):
        result = get_result()
        assert result.language == "English"

    def test_name(self):
        result = get_result()
        print(result.name)
        assert result.name == "Chick.Fight.2020.720p.WEBRip.800MB.x264-GalaxyRG"

    def test_quality(self):
        result = get_result()
        assert result.quality == "HD"

    def test_magnet_url(self):
        result = get_result()
        assert (
            result.magnet_url
            == "magnet:?xt=urn:btih:d63270caa865ae6eb439a7a4cbe3e9455670e71c&dn=Chick.Fight.2020.720p.WEBRip.800MB.x264-GalaxyRG&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fipv4.tracker.harry.lu%3A80%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.demonii.si%3A1337%2Fannounce"
        )

    def test_username(self):
        result = get_result()
        assert result.username == "GalaxyRG"

    def test_views(self):
        result = get_result()
        assert result.views == "33,030"

    def test_seeders(self):
        result = get_result()
        assert result.seeders == "379"

    def test_leachers(self):
        result = get_result()
        assert result.leachers == "462"

    def test_health(self):
        result = get_result()
        assert result.health == "379462"

    def test_size(self):
        result = get_result()
        assert result.size == "993.86 MB"

    def test___repr__(self):
        result = get_result()
        assert "<Result:" in repr(result)

    def test___str__(self):
        result = get_result()
        assert (
            str(result)
            == "Chick.Fight.2020.720p.WEBRip.800MB.x264-GalaxyRG: HD English 993.86 MB 379462"
        )

    def test_sort_byName_returnsCorrectListReversed(self):
        sorted = Search.sort(get_results(), "name", True)
        expected = {
            "Chick.Fight.2020.1080p.WEB-DL.DD5.1.H.264-EVO[TGx]",
            "Chick.Fight.2020.720p.WEBRip.800MB.x264-GalaxyRG",
            "Chick.Fight.2020.HDRip.XviD.AC3-EVO[TGx]",
        }
        assert expected == set(x.name for x in sorted)

    def test_sort_byName_returnsCorrectList(self):
        sorted = Search.sort(
            get_results(),
            "name",
        )
        expected = {
            "Chick.Fight.2020.HDRip.XviD.AC3-EVO[TGx]",
            "Chick.Fight.2020.720p.WEBRip.800MB.x264-GalaxyRG",
            "Chick.Fight.2020.1080p.WEB-DL.DD5.1.H.264-EVO[TGx]",
        }
        assert expected == set(x.name for x in sorted)

    def test_search(self, mocker):
        mocked_get_soup = mocker.patch("torrent_galaxy_search.search._get_soup")
        mocked_get_soup.return_value = get_soup()

        results = Search.by_IMDB_ID("nonsensename")
        assert len(results) == 3


def get_result() -> Result:
    with open("./tests/test_data/tgxtablerow.html") as _file:
        data = Result(_file.read())
        return data


def get_results():
    results: List[Result] = []
    with open("./tests/test_data/output.html") as _file:
        soup = BeautifulSoup(_file.read(), features="html.parser")
        for link in soup.find_all("div", class_="tgxtablerow"):
            results.append(Result(link))

    return results


def get_soup():
    with open("./tests/test_data/output.html") as _file:
        return BeautifulSoup(_file.read(), features="html.parser")
