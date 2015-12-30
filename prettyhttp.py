import httpretty
import requests
from time import sleep
from sure import expect

@httpretty.activate
def example():
    httpretty.register_uri(httpretty.GET, "http://google.com/", body="This is a mocked body", status=201)

    response = requests.get("http://google.com/")
    print response
    expect(response.status_code).to.equal(201)

@httpretty.activate
def setting_header_example():
    httpretty.register_uri(httpretty.GET, 
                           "http://api.example.com/some/path", 
                           body='{"success": true}', 
                           status=200, 
                           content_type='text/json') 

    response = requests.get("http://api.example.com/some/path")
    print response.content 
    expect(response.json()).to.equal({'success': True})
    expect(response.status_code).to.equal(200)

@httpretty.activate
def rotating_responses_example():
    URL = "http://example.com/some/path"
    RESPONSE_1 = "This is response 1"
    RESPONSE_2 = "This is response 2"
    RESPONSE_3 = "This is last response"

    httpretty.register_uri(httpretty.GET, 
                           URL,
                           responses=[
                               httpretty.Response(body=RESPONSE_1, status=201),
                               httpretty.Response(body=RESPONSE_2, status=202),
                               httpretty.Response(body=RESPONSE_3, status=201)])

    response_1 = requests.get(URL)
    expect(response_1.status_code).to.equal(201)
    expect(response_1.text).to.equal(RESPONSE_1)

    response_2 = requests.get(URL)
    expect(response_2.status_code).to.equal(202)
    expect(response_2.text).to.equal(RESPONSE_2)

    response_3 = requests.get(URL)
    expect(response_3.status_code).to.equal(201)
    expect(response_3.text).to.equal(RESPONSE_3)

    response_4 = requests.get(URL)
    expect(response_4.status_code).to.equal(201)
    expect(response_4.text).to.equal(RESPONSE_3)

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

    response = requests.get(URL, data={"track": "requests"})

    line_iter = response.iter_lines()
    for i in xrange(len(REPOS)):
        expect(line_iter.next().strip()).to.equal(REPOS[1].strip())


def dynamic_responses_example():
    def request_callback(method, uri, headers):
        return (200, headers, "The {} response from {}".format(method, uri))

    httpretty.register_uri(
        httpretty.GET, "http://example.com/sample/path",
        body=request_callback)

    response = requests.get("http://example.com/sample/path")

    expect(response.text).to.equal(' http://example.com/sample/path')

if __name__ == '__main__': 
    example()
    setting_header_example() 
    rotating_response_example()
   

