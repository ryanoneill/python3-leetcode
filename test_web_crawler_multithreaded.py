from html_parser import HtmlParser
from web_crawler_multithreaded import Solution
from typing import List


class ExampleHtmlParser(HtmlParser):
    def __init__(self, urls: List[str], edges: List[List[int]]):
        self.urls = urls
        self.links = {i: set() for i in range(len(urls))}
        for edge in edges:
            i, j = edge
            self.links[i].add(j)
        self.index_by_url = {url: index for index, url in enumerate(urls)}

    def getUrls(self, url: str) -> List[str]:
        results = []
        if url in self.index_by_url:
            index = self.index_by_url[url]
            results = [self.urls[j] for j in self.links[index]]
        return results


def test_ex1():
    urls = [
        "http://news.yahoo.com",
        "http://news.yahoo.com/news",
        "http://news.yahoo.com/news/topics/",
        "http://news.google.com",
        "http://news.yahoo.com/us",
    ]
    edges = [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]]
    startUrl = "http://news.yahoo.com/news/topics/"
    html_parser = ExampleHtmlParser(urls, edges)
    solution = Solution()
    results = solution.crawl(startUrl, html_parser)
    results.sort()
    expected = [
        "http://news.yahoo.com",
        "http://news.yahoo.com/news",
        "http://news.yahoo.com/news/topics/",
        "http://news.yahoo.com/us",
    ]
    assert results == expected


def test_ex2():
    urls = [
        "http://news.yahoo.com",
        "http://news.yahoo.com/news",
        "http://news.yahoo.com/news/topics/",
        "http://news.google.com",
    ]
    edges = [[0, 2], [2, 1], [3, 2], [3, 1], [3, 0]]
    startUrl = "http://news.google.com"
    html_parser = ExampleHtmlParser(urls, edges)
    solution = Solution()
    results = solution.crawl(startUrl, html_parser)
    results.sort()
    expected = ["http://news.google.com"]
    assert results == expected
