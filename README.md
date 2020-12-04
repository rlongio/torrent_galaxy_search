# A Torrent Galaxy Search

<img src="https://github.com/rlongio/torrent_galaxy_search/blob/master/docs/img/detective.png?raw=true" alt="drawing" width="200"/>

![Python application](https://github.com/rlongio/torrent_galaxy_search/workflows/Python%20application/badge.svg)

Library for interfacing with **torentgalaxy**.

### Example

```python
from typing import List
from torrent_galaxy_search.search import Search, Result


def main():
    results: List[Result] = Search.by_IMDB_ID("tt0095016")

    for r in results:
        print(r)


if __name__ == "__main__":
    main()
 ```
 
 ### Output
 ```
Die.Hard.1988.720p.BluRay.999MB.HQ.x265.10bit-GalaxyRG: HD English 1,003.26 MB 61
Die Hard (1988) (1080p BDRip x265 10bit EAC3 5.1 - xtrem3x) [TAoE].mkv: HD English 6.09 GB 20
Die Hard (1988) (1080p BDRip x265 10bit DTS-HD MA 5.1 - xtrem3x) [TAoE].mkv: HD English 7.79 GB 3524
Die Hard (1988)Mp-4 X264 Dvd-Rip 480p AAC[DSD]: SD English 1.24 GB 10
Die.Hard.1988.720p.BrRip.x264.bitloks.YIFY.mp4: HD English 906.55 MB 21
Die Hard - Trappola di cristallo (1988).SD.H265.Ita.Eng.Ac3-5.1.sub.ita.eng-BaMax71-MIRCre...: SD English 1.79 GB 10
```
