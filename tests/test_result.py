# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package


from torrent_galaxy_search.result import Result


class TestResult:
    @classmethod
    def get_result(cls):
        def _get_result_from_file_or_closure(data=None):
            if data is not None:
                return data

            with open("./tests/test_data/tgxtablerow.html") as _file:
                data = Result(_file.read())
                return data

        return _get_result_from_file_or_closure()

    def test_language(self):
        result = self.get_result()
        assert result.language == "English"

    def test_name(self):
        result = self.get_result()
        print(result.name)
        assert result.name == "Chick.Fight.2020.720p.WEBRip.800MB.x264-GalaxyRG"

    def test_quality(self):
        result = self.get_result()
        assert result.quality == "HD"

    def test_magnet_url(self):
        result = self.get_result()
        assert (
            result.magnet_url
            == "magnet:?xt=urn:btih:d63270caa865ae6eb439a7a4cbe3e9455670e71c&dn=Chick.Fight.2020.720p.WEBRip.800MB.x264-GalaxyRG&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fipv4.tracker.harry.lu%3A80%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.demonii.si%3A1337%2Fannounce"
        )

    def test_username(self):
        result = self.get_result()
        assert result.username == "GalaxyRG"

    def test_views(self):
        result = self.get_result()
        assert result.views == "33,030"

    def test_seeders(self):
        result = self.get_result()
        assert result.seeders == "379"

    def test_leachers(self):
        result = self.get_result()
        assert result.leachers == "462"

    def test_health(self):
        result = self.get_result()
        assert result.health == "379462"

    def test_size(self):
        result = self.get_result()
        assert result.size == "993.86 MB"

    def test___repr__(self):
        result = self.get_result()
        assert "<Result:" in repr(result)

    def test___str__(self):
        result = self.get_result()
        assert (
            str(result)
            == "Chick.Fight.2020.720p.WEBRip.800MB.x264-GalaxyRG: HD English 993.86 MB 379462"
        )
