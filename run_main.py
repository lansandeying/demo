import unittest   
from HTMLTestRunner_cn import HTMLTestRunner 
import time 
# from public.send_email import email_user
# from test_mybags import MyTestlogin
  
#定义测试用例的目录为当前目录  


  
if __name__=="__main__":  
    test_dir = r'C:\Users\hp\eclipse-workspace\zVke\case\other'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py')
  
  
    #按照一定的格式获取当前的时间  
    now = time.strftime("%Y-%m-%d %H-%M-%S")  
      
    #定义报告存放路径  
    filename = r"C:\Users\hp\eclipse-workspace\zVke\report\htm" + now + '_test_result.html'  
      
    fp = open(filename,"wb")  
    #定义测试报告  
    runner = HTMLTestRunner(stream =  fp,  
                            title = "接口测试报告",  
                            description = "测试用例执行情况：",
                            verbosity=2, #控制台风格
                            retry=1)   #失败重跑一次
    time.sleep(3)

    #运行测试  
    runner.run(discover)  
    fp.close() #关闭报告文件