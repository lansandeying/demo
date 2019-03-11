import unittest   
from HTMLTestRunner_cn import HTMLTestRunner 
import time 
# from public.send_email import email_user
# from test_mybags import MyTestlogin
  
#瀹氫箟娴嬭瘯鐢ㄤ緥鐨勭洰褰曚负褰撳墠鐩綍  


  
if __name__=="__main__":  
    test_dir = r'F:\my_job\zVke\case_chrome'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py',top_level_dir=None)
  
  
    #鎸夌収涓�瀹氱殑鏍煎紡鑾峰彇褰撳墠鐨勬椂闂�  
    now = time.strftime("%Y-%m-%d %H-%M-%S")  
    
    #瀹氫箟鎶ュ憡瀛樻斁璺緞  
    filename = r"F:\my_job\zVke\report\htm" + now + '_test_result.html'  
      
    fp = open(filename,"wb")  
    #瀹氫箟娴嬭瘯鎶ュ憡  
    runner = HTMLTestRunner(stream =  fp,  
                            title = u"测试报告",  
                            description = u"测试用例执行情况",
                            verbosity=2, #鎺у埗鍙伴鏍�
                            retry=1)   #澶辫触閲嶈窇涓�娆�
    time.sleep(3)

    #杩愯娴嬭瘯  
    runner.run(discover)  
    fp.close() #鍏抽棴鎶ュ憡鏂囦欢