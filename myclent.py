from suds.client import Client  # 导入suds.client 模块下的Client类

wsdl_url = "http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?WSDL"
#pip install suds-py3

def say_hello_test(url, getMobileCodeInfoSoapIn1):
    client = Client(url)  # 创建一个webservice接口对象
    client.service.getMobileCodeInfo(getMobileCodeInfoSoapIn1)  # 调用这个接口下的getMobileCodeInfo方法，并传入参数
    req = str(client.last_sent())  # 保存请求报文，因为返回的是一个实例，所以要转换成str
    response = str(client.last_received())  # 保存返回报文，返回的也是一个实例
    print(req)
    print(response)



if __name__ == '__main__':
    say_hello_test(wsdl_url, '13602747060')
    import sys
    import logging

    logger = logging.getLogger('suds')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logging.basicConfig(level=logging.DEBUG,\
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # logging.basicConfig函数对日志的输出格式及方式做相关配置
    # 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
    logging.info('this is a loggging info message')
    logging.debug('this is a loggging debug message')
    logging.warning('this is loggging a warning message')
    logging.error('this is an loggging error message')
    logging.critical('this is a loggging critical message')