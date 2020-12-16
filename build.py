#coding=utf-8

import zipfile
import sys
import time
import os
import shutil

PATH = '/Users/ofweek/Desktop/sh'
APPName = 'OFweekPhone'
#xcode bulid 生成的文件
SCRAPP = r'{path}/{name}.app'.format(path=PATH, name=APPName)
#存放ipa文件的目录
Dir = r'{path}'.format(path=PATH)

DESdir = os.path.join(Dir,'APP/Payload/{name}.app'.format(name=APPName))
def moveFile(scrdir,desdir):
    print('*' * 50)
    if not os.path.isdir(scrdir):
        print("%s not exist" % scrdir)
    else:
        if os.path.isdir(desdir):
            shutil.rmtree(desdir)
            print('{name}.app文件存在删除'.format(name=APPName))

        shutil.copytree(scrdir, desdir)
        print('复制文件成功%s' % desdir)

def zipDir():
    print('*' * 50)
    global Dir
    if not os.path.isdir(Dir):
        print('压缩的文件夹不存在')
    else:
        print('压缩开始')
        os.chdir('%s/APP'%Dir)
        os.system('zip -r myfile.zip ./*')
        print('压缩完成')
        os.rename('myfile.zip','myfile.ipa')

def changeName(typeInt=0):
    print('*' * 50)
    print('重命名开始')
    typeStr = 'dev{name}.ipa'.format(name=APPName)
    if typeInt == 2:
        typeStr = 'dis{name}.ipa'.format(name=APPName)
    elif typeInt == 1:
        typeStr = 'ydev{name}.ipa'.format(name=APPName)

    desPath = os.path.join(Dir,typeStr)
    if os.path.exists(desPath):
        os.remove(desPath)
        print('删除：%s'%desPath)
        
    shutil.move('%s/APP/myfile.ipa'%Dir,desPath)
    print('重命名完成')
    ipapath = desPath
    res = os.path.getctime(ipapath)
    size = os.path.getsize(ipapath)

    time_local = time.localtime(res)
    dt = time.strftime('%Y-%m-%d %H:%M:%S', time_local)
    print('%s' % ipapath)
    print ('IPA文件大小：%.2f'%float(size))
    print(dt)

def main(typeInt=0):
    moveFile(SCRAPP,DESdir)
    zipDir()
    changeName(typeInt)

if __name__ == '__main__':
    '''
    1:预发布     (cmd: python3 build 1)
    2：正式      (cmd: python3 build 2)
    3:测试        (cmd: python3 build )
   使用用例：
  
    '''
    print('开始执行...')

    if (len(sys.argv) == 2):
        typeInt = sys.argv[1]
        main(int(typeInt))
    else:
        main()
