# gong
## 一、介绍
快速搭建Flask框架

## 二、使用
下面是linux的使用步骤：

```
git clone https://github.com/zhanggong16/gong.git
#gong依赖click包
pip install click
cd gong
#建立Flask项目的部署路径（basedir），如果没有建立，是不能自动部署的
mkdir -p /tmp/cto
#执行gong的主命令，需要输入项目名称（name）和部署目录（path），部署路径basedir=$path/$name
./gong.py
package name: cto
package path: /tmp
====================
framework: flask, package name: cto, package path: /tmp/cto
confirm(y,n): y
#执行完成后，进入项目的部署路径
cd /tmp/cto/
source venv/bin/activate
pip install -r requirement.txt
启动Flask
honcho start
09:26:10 system   | server.1 started (pid=129951)
09:26:10 server.1 |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
09:26:10 server.1 |  * Restarting with stat
09:26:10 server.1 |  * Debugger is active!
09:26:10 server.1 |  * Debugger PIN: 206-500-370
```
至此Flask项目已经成功启动。

## 三、验证
通过浏览器访问http://localhost:5000，显示Hello, World!

## 四、目录

```
cto/
├── app.py #入口
├── cto
│   ├── app.py #Flask主程序
│   ├── app.pyc
│   ├── config.py #读取.env的配置文件
│   ├── config.pyc
│   ├── error
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── views.py
│   │   └── views.pyc
│   ├── index
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── views.py
│   │   └── views.pyc
│   ├── __init__.py
│   ├── __init__.pyc
│   └── templates
│       └── index.html
├── .env #配置文件，包括端口等
├── Procfile # honcho启动文件
└── requirement.txt
```
