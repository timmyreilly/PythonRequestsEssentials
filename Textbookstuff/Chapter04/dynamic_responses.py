import httpretty
import requests

from sure import expect


@httpretty.activate
def dynamic_responses_example():
    def request_callback(method, uri, headers):
        return (200, headers, "The {} response from {}".format(method, uri))
    httpretty.register_uri(
        httpretty.GET, "http://example.com/sample/path",
        body=request_callback)

    response = requests.get("http://example.com/sample/path")

    expect(response.text).to.equal('The GET response from \
                                   http://example.com/sample/path')
