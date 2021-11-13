import soaplib
from soaplib.core.service import rpc, DefinitionBase
from soaplib.core.model.primitive import String, Integer, Boolean
from soaplib.core.server import wsgi
from soaplib.core.model.clazz import Array
from soaplib.core.service import soap
from soaplib.core.model.clazz import ClassModel


class Rules(ClassModel):
    __namespace__ = "Rules"
    username = String
    emotion = String


class HelloWorldService(DefinitionBase):
    @soap(String, Integer, _returns=Array(String))
    def say_hello(self, name, times):
        results = []
        for i in range(0, times):
            results.append('Hello, %s' % name)
        return results

    @soap(Rules, _returns=Boolean)
    def get_recommend(self, rules):
        print
        rules.username
        print("aaaaaa")
        111
        print("aaaaaa")
        rules.emotion

        return 1


if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server

        soap_application = soaplib.core.Application([HelloWorldService], 'tns')
        wsgi_application = wsgi.Application(soap_application)
        server = make_server('localhost', 7789, wsgi_application)
        server.serve_forever()
    except ImportError:
        print("aaaaaa")