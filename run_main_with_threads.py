#coding:utf-8
import unittest   
from HTMLTestRunner_cn import HTMLTestRunner 
import time 
from tomorrow import threads
# from public.send_email import email_user
# from test_mybags import MyTestlogin
@threads(5)  
def run_case(discover,case_path): 
    #鎸夌収涓�瀹氱殑鏍煎紡鑾峰彇褰撳墠鐨勬椂闂�  
    now = time.strftime("%Y-%m-%d %H-%M-%S")  
      
    #瀹氫箟鎶ュ憡瀛樻斁璺緞  
    filename = r"F:\my_job\zVke\report\htm" + now  + case_path + '_test_result.html'  
      
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


  
if __name__=="__main__": 
    chrome_path="F:\my_job\zVke\case_chrome"
    firefox_path='F:\my_job\zVke\case_firefox'
    test_dirs = [chrome_path,firefox_path]
    
    for test_dir in test_dirs:
        print(test_dir)
        case_path=test_dir.split('\\')[-1]
        
        unittest.defaultTestLoader._top_level = None
        discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py')
        print(case_path)
#         run_case(discover,case_path)      