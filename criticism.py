import random
import datetime

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

def get_beginbody():
    file = r'D:\学习\编程\练习\2022\20220713-检讨书生成\begin.txt'
    with open(file,'r',encoding='utf-8') as f:
        linelist = f.readlines()
        begintxt = random.choice(linelist)

    return begintxt


def get_mainbody(num):
    maintxts = ""
    file = r'D:\学习\编程\练习\2022\20220713-检讨书生成\content.txt'
    with open(file,'r',encoding='utf-8') as f:
        linelist = f.readlines()

        while len(maintxts) <= num:
            maintxts = maintxts + random.choice(linelist) + '    '

    return maintxts

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

    print(content)

if __name__ == '__main__':
    num = int(input("请输入生成字数："))
    becriticismer = input("请输入被检讨人：")
    criticismer = input("请输入检讨人：")
    main(num,becriticismer,criticismer)