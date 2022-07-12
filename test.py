
from selenium import webdriver

# 如果driver沒有添加到了環境變量，則需要將driver的絕對路徑賦值給executable_path參數
# driver = webdriver.Chrome(executable_path='/home/worker/Desktop/driver/chromedriver')

# 如果driver添加了環境變量則不需要設置executable_path
driver = webdriver

# 向一個url發起請求
driver.get("http://www.itcast.cn/")

# 把網頁保存爲圖片，69版本以上的谷歌瀏覽器將無法使用截圖功能
# driver.save_screenshot("itcast.png")

print(driver.title) # 打印頁面的標題

# 退出模擬瀏覽器
driver.quit() # 一定要退出！不退出會有殘留進程！
