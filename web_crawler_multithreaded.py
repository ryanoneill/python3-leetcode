from html_parser import HtmlParser

from concurrent.futures import ThreadPoolExecutor
from collections import deque
from typing import List


class Solution:
    def get_hostname(self, url: str) -> str:
        return url.lstrip("http://").rsplit("/")[0]

    def crawl(self, startUrl: str, htmlParser: "HtmlParser") -> List[str]:
        hostname = self.get_hostname(startUrl)

        queue = deque()
        seen = set()
        queue.append(startUrl)
        seen.add(startUrl)

        with ThreadPoolExecutor() as pool:
            while queue:
                results = pool.map(htmlParser.getUrls, queue)
                queue.clear()
                for items in results:
                    for item in items:
                        if item not in seen and self.get_hostname(item) == hostname:
                            seen.add(item)
                            queue.append(item)

        return list(seen)
