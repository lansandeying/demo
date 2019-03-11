import unittest   
from HTMLTestRunner_cn import HTMLTestRunner 
import time 
from public.send_email import email_user
# from test_mybags import MyTestlogin
  
#瀹氫箟娴嬭瘯鐢ㄤ緥鐨勭洰褰曚负褰撳墠鐩綍  


  
if __name__=="__main__":  
    test_dir = r'F:\my_job\zVke\case\login'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py')
  
  
    #鎸夌収涓�瀹氱殑鏍煎紡鑾峰彇褰撳墠鐨勬椂闂�  
    now = time.strftime("%Y-%m-%d %H-%M-%S")  
      
    #瀹氫箟鎶ュ憡瀛樻斁璺緞  
    filename = r"F:\my_job\zVke\report\htm" + now + '_test_result.html'  
      
    fp = open(filename,"wb")  
    #瀹氫箟娴嬭瘯鎶ュ憡  
    runner = HTMLTestRunner(stream =  fp,  
                            title = u"测试报告",  
                            description = u"测试用例执行情况",
                            verbosity=2, #级别2
                            retry=1)   #失败重跑一次
    time.sleep(3)

    #杩愯娴嬭瘯  
    runner.run(discover)  
    fp.close() #鍏抽棴鎶ュ憡鏂囦欢
    sender="516015922@qq.com"
    psw="opvibqkkinnkcaai"
    receiver=["452949134@qq.com","18033084759@163.com"]
    print(receiver)
    way="QQ"
    x_email=email_user(sender,psw,receiver,way)
    subject=u"测试报告"
#     body=u"测试结果报告展示"
#     decode="plain"
#     x_email.email_body(subject, body, decode)
    x_email.email_body_flie(subject, file_path=filename)