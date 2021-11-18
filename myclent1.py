from suds.client import Client

wsdl_url = "http://localhost:8181/?wsdl"


def say_hello_test(url, name, times):
    client = Client(url)
    client.service.say_hello(name, times)
    req = client.last_sent()
    response = client.last_received()
    print(req.str())
    print(response.str())


if __name__ == '__main__':
    say_hello_test(wsdl_url, 'test', 2)