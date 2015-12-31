import httpretty
import requests

from sure import expect


@httpretty.activate
def rotating_responses_example():
    URL = "http://example.com/some/path"
    RESPONSE_1 = "This is Response 1."
    RESPONSE_2 = "This is Response 2."
    RESPONSE_3 = "This is Last Response."

    httpretty.register_uri(httpretty.GET,
                           URL,
                           responses=[
                               httpretty.Response(body=RESPONSE_1,
                                                  status=201),
                               httpretty.Response(body=RESPONSE_2,
                                                  status=202),
                               httpretty.Response(body=RESPONSE_3,
                                                  status=201)])

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
