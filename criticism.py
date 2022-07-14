import re
import random
import datetime
from faker import Factory
from faker import Faker
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def match_count(str_object,match_object):
    count = len(re.findall(match_object,str_object))
    return count

#模板
def criticism_moudle(to_name,beginbody,mainbody,endbody,from_name,datestr):
     maincontent = '''
亲爱的{}：

    {} 
    {} 
    {}
检讨人：{}
{}     
    '''.format(to_name,beginbody,mainbody,endbody,from_name,datestr)

     return maincontent
#获取开头
def get_beginbody():
    file = r'D:\学习\编程\练习\2022\20220713-检讨书生成\begin.txt'
    with open(file,'r',encoding='utf-8') as f:
        linelist = f.readlines()
        begintxt = random.choice(linelist)

    return begintxt

#获取正文
def get_mainbody(num):
    maintxts = ""
    file = r'D:\学习\编程\练习\2022\20220713-检讨书生成\content.txt'
    with open(file,'r',encoding='utf-8') as f:
        linelist = f.readlines()

        while len(maintxts) <= num:
            tmptxt = random.choice(linelist)
            if match_count(maintxts,tmptxt) <= 0:
                maintxts = maintxts + tmptxt + '    '

    return maintxts
    
#获取结尾
def get_endbody():
    file = r'D:\学习\编程\练习\2022\20220713-检讨书生成\end.txt'
    with open(file,'r',encoding='utf-8') as f:
        linelist = f.readlines()
        endtxt = random.choice(linelist)

    return endtxt

def main(num,becriticismer,criticismer):

    beginbody = get_beginbody()
    endbody = get_endbody()
    mainbody = get_mainbody(num)

    t = datetime.datetime.today()
    datestr = t.strftime('%Y/%m/%d')

    content = criticism_moudle(becriticismer,beginbody,mainbody,endbody,criticismer,datestr)

    return content

def next_content():
    fake = Faker('zh_CN')
    # 随机生成女性名字
    becriticismer = fake.name_female()
    # 男性名字
    criticismer = fake.name_male()
    content = main(800,becriticismer,criticismer)
    text.delete("0.0", 'end')  # 删除内容
    text.insert('insert', content)



if __name__ == '__main__':
    #num = int(input("请输入生成字数："))
    #becriticismer = input("请输入被检讨人：")
    #criticismer = input("请输入检讨人：")
    #main(num,becriticismer,criticismer)
    fake = Faker('zh_CN')
    # 随机生成女性名字
    becriticismer = fake.name_female()
    # 男性名字
    criticismer = fake.name_male()

    content = main(800,becriticismer,criticismer)
    root = ttk.Window(size=(1000,700),title='女朋友检讨书生成器--亮仔出品')
    ttk.Button(root, text="换一个", bootstyle=SUCCESS,command=next_content).place(x=450,y=630)
    text = ttk.Text(root, )
    text.pack(padx=10, pady=10, fill=BOTH)
    text.delete("0.0", 'end')  # 删除内容
    text.insert('insert', content)
    #text.see(ttk.END)  # 光标跟随着插入的内容移动
    root.mainloop()