
from fastapi import FastAPI,Query
import uvicorn
from sendoa.sendoa import sendoa
from typing import Tuple,List,Dict

# 类似于 app = Flask(__name__)
app = FastAPI()

# 绑定路由和视图函数
@app.get("/")
async def index():
	sendoa('aaaa11','11608')
	return "成功发送数据"
@app.get("/str")
async def index2():
	print("aiiw")
	return "古明地觉"

@app.get("/sendoa/")
async def read_items(content:str,q: List[str] = Query(None)):
    query_items = {"q": q}
    sendcont=content
    code=query_items.get('q')
    print(code[0])
    
    if q !=None:
    	code=tuple(q)
    	print(code[1])
    	result=sendoa(sendcont,*code)
    	return result
    print(query_items)
    return "信息发送失败,请检查相关问题"


# 在 Windows 中必须加上 if __name__ == "__main__"，否则会抛出 RuntimeError: This event loop is already running
if __name__ == "__main__":
    # 启动服务，因为我们这个文件叫做 main.py，所以需要启动 main.py 里面的 app
    # 第一个参数 "main:app" 就表示这个含义，然后是 host 和 port 表示监听的 ip 和端口
    uvicorn.run("myfastapi:app", host="192.168.0.7", port=8085,reload=True)