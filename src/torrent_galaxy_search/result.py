from typing import List, Union
from bs4 import BeautifulSoup, element


class Result:
    """Encapsulates a search result."""

    def __init__(self, data: Union[str, element.Tag]):
        self.soup = self._get_soup(str(data))

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.soup}>"

    def __str__(self) -> str:
        return f"{self.name}: {self.quality} {self.language} {self.size} {self.health}"

    def __getitem__(self, key):
        return getattr(Result, key)

    def _get_soup(self, _html: str) -> BeautifulSoup:
        return BeautifulSoup(_html, "html.parser")

    @property
    def language(self) -> str:
        return self.soup.find_all("div", class_="tgxtablecell")[2].find("img")["title"]

    @property
    def name(self) -> str:
        hrefs = self.soup.find_all("div", class_="tgxtablecell")[3].div.find_all("a")
        return (hrefs[0] if len(hrefs) < 3 else hrefs[1]).b.text

    @property
    def quality(self) -> str:
        return (
            self.soup.find_all("div", class_="tgxtablecell")[0]
            .small.text.split(":")[1]
            .strip()
        )

    @property
    def magnet_url(self) -> str:
        return self.soup.find_all("div", class_="tgxtablecell")[4].find_all("a")[1][
            "href"
        ]

    @property
    def username(self) -> str:
        return self.soup.find_all("div", class_="tgxtablecell")[6].span.a.span.text

    @property
    def size(self) -> str:
        return self.soup.find_all("div", class_="tgxtablecell")[7].span.text

    @property
    def views(self) -> str:
        return self.soup.find_all("div", class_="tgxtablecell")[9].span.text.strip()

    @property
    def seeders(self) -> str:
        return (
            self.soup.find_all("div", class_="tgxtablecell")[10]
            .span.find_all("b")[0]
            .text.strip()
        )

    @property
    def leachers(self) -> str:
        return (
            self.soup.find_all("div", class_="tgxtablecell")[10]
            .span.find_all("b")[1]
            .text.strip()
        )

    @property
    def health(self) -> str:
        return self.seeders + self.leachers

    @classmethod
    def sort(cls, results: List["Result"], property: str) -> List["Result"]:
        results.sort(key=lambda x: str(x[property]), reverse=True)
        return results
