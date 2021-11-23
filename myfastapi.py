
from fastapi import FastAPI,Query,Request
import uvicorn
from sendoa.sendoa import sendoa
from typing import Tuple,List,Dict,Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware



# 类似于 app = Flask(__name__)
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8085",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
# 绑定路由和视图函数
@app.get("/")
async def index():
	ss='''<img src="http://www.mastergroup.com.cn/images/index/pic_04.jpg">'''
	sendoa(ss,'11608')
	return "成功发送数据"
@app.get("/str")
async def index2(request:Request):
	print("aiiw")
	print(request.headers)
	return "古明地觉"

@app.get("/sendoa/")
async def read_items(content:str,q: List[str] = Query(None)):
    query_items = {"q": q}
    sendcont=content
    code=query_items.get('q')
    # print(code[0])
    
    if q !=None:
    	code=tuple(q)
    	# print(code[1])
    	result=sendoa(sendcont,*code)
    	return result
    print(query_items)
    return "信息发送失败,请检查相关问题"

class Girl(BaseModel):
    """数据验证是通过 pydantic 实现的，我们需要从中导入 BaseModel，然后继承它"""
    name: str
    age: Optional[str] = None
    length: float=None
    hobby: List[str]=None  # 对于 Model 中的 List[str] 我们不需要指定 Query（准确的说是 Field）


@app.post("/aiiw")
async def read_girl(girl: Girl):
    # girl 就是我们接收的请求体，它需要通过 json 来传递，并且这个 json 要有上面的四个字段（age 可以没有）
    # 通过 girl.xxx 的方式我们可以获取和修改内部的所有属性
    return dict(girl)  # 直接返回 Model 对象也是可以的

@app.post("/girl")
async def read_girl(request: Request):
    # 是一个协程，所以需要 await
    data = await request.body()
    print(data)


# 在 Windows 中必须加上 if __name__ == "__main__"，否则会抛出 RuntimeError: This event loop is already running
if __name__ == "__main__":
    # 启动服务，因为我们这个文件叫做 main.py，所以需要启动 main.py 里面的 app
    # 第一个参数 "main:app" 就表示这个含义，然后是 host 和 port 表示监听的 ip 和端口
    uvicorn.run("myfastapi:app", host="192.168.0.7", port=8085,reload=True)