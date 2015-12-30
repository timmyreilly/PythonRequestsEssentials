import httpretty
import requests

from sure import expect


@httpretty.activate
def setting_header_example():
    httpretty.register_uri(httpretty.GET,
                           "http://api.example.com/some/path",
                           body='{"success": true}',
                           status=200,
                           content_type='text/json')

    response = requests.get("http://api.example.com/some/path")

    expect(response.json()).to.equal({'success': True})
    expect(response.status_code).to.equal(200)
