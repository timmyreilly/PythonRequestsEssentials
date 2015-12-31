import httpretty
import requests

from time import sleep
from sure import expect


def mock_streaming_repos(repos):
    for repo in repos:
        sleep(.5)
        yield repo


@httpretty.activate
def streaming_responses_example():
    URL = "https://api.github.com/orgs/python/repos"
    REPOS = ['{"name": "repo-1", "id": 1}\r\n',
             '\r\n',
             '{"name": "repo-2", "id": 2}\r\n']

    httpretty.register_uri(httpretty.GET,
                           URL,
                           body=mock_streaming_repos(REPOS),
                           streaming=True)

    response = requests.get(URL,
                            data={"track": "requests"})

    line_iter = response.iter_lines()
    for i in xrange(len(REPOS)):
        expect(line_iter.next().strip()).to.equal(REPOS[i].strip())
