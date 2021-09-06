#!venv/bin/python3
import os
import time
import pexpect
import argparse


def get_input() -> dict:
    '''
        获取终端的输入
    '''
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('-port', type=str, default = None)
    parser.add_argument('-username', type=str, default = None)
    parser.add_argument('-password', type=str, default = None)
    args = parser.parse_args()
    data = {}
    data['port'] = args.port
    data['username'] = args.username
    data['password'] = args.password
    return data


def bt_init(port: str, username: str, password: str) -> bool:
    '''
        初始化宝塔，设置 端口号，用户名，密码
    '''
    #改面板端口
    print('正在设置面板端口')
    child = pexpect.spawn('bt')
    child.expect('.*：'.encode('utf-8'))
    child.sendline('8')
    child.expect('面板端口：'.encode('utf-8'))
    child.sendline(port)
    child.expect('已将面板端口修改'.encode('utf-8'))
    #改面板用户名
    print('正在设置面板用户名')
    child = pexpect.spawn('bt')
    child.expect('.*：'.encode('utf-8'))
    child.sendline('6')
    child.expect('面板用户名'.encode('utf-8'))
    child.sendline(username)
    child.expect('新用户名'.encode('utf-8'))
    #改面板密码
    print('正在设置面板密码')
    child = pexpect.spawn('bt')
    child.expect('.*：'.encode('utf-8'))
    child.sendline('5')
    child.expect('面板密码：'.encode('utf-8'))
    child.sendline(password)
    child.expect('新密码'.encode('utf-8'))
    
    return True


def main():
    data = get_input()
    
    #检测端口是否合法
    try:
        port = int(data['port'])
        if 0 <= port <= 65535:
            port = str(port)
    except:
        print('您输入的端口号有误，请重新创建 Docker 容器并输入正确端口号')
        return False
    
    #检测用户名是否合法
    if len(data['username']) < 3:
        print('密码长度不能小于 3 位，请重新创建 Docker 容器并输入正确用户名')
        return False    
    #检测密码是否合法
    if len(data['password']) < 5:
        print('密码长度不能小于 5 位，请重新创建 Docker 容器并输入正确密码')
        return False
    
    #判断是否是第一次初始化
    if not os.path.isfile('init.txt'):
        bt_init(data['port'], data['username'], data['password'])
        os.system('touch init.txt')
        print('设置成功\n')
    os.system('/etc/init.d/bt start')
    print('\n宝塔面板已启动\n')
    result = os.popen('echo "$(ping ${HOSTNAME} -c 1 | grep -o -E [0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+ | head -n 1)"')
    ip = result.read().replace('\n', '')
    print('面板链接: http://' + ip + ':' + data['port'])
    print('用户名: ' + data['username'])
    print('密码: ' + data['password'])
    
    while True:
        time.sleep(60 * 60 * 24 * 365 * 100)


if __name__ == '__main__':
    main()
