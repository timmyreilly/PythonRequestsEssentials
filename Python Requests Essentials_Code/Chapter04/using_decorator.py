import httpretty
import requests

from sure import expect


@httpretty.activate
def example():
    httpretty.register_uri(httpretty.GET, "http://google.com/",
                           body="This is the mocked body",
                           status=201)
    response = requests.get("http://google.com/")
    expect(response.status_code).to.equal(201)
