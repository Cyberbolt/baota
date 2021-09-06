### Docker 部署宝塔面板

此方案可能是全网最快的 宝塔面板 部署方案。该镜像基于 宝塔Linux正式版 7.7.0（官方纯净版，可升级） 制作。维护脚本使用 Python 开发，源码和 Dockerfile 均已上传至 [GitHub](https://github.com/Cyberbolt/baota)（欢迎您的 Star）。

本镜像仅保留了最精简的 宝塔面板，未安装任何插件。初始化容器后，您可以根据需要选择安装插件。"Simple is better than complex!" 此外，如果您在生产环境下部署宝塔面板，请务必参考 **方案二** 创建容器。

使用方法如下:

(注：为了方便部署，该镜像去除了安全入口，您可以自行配置)

### 方案一（最快化部署）

```
docker run -itd --net=host --restart=always --name baota cyberbolt/baota:latest -port 端口号 -username 用户名 -password 密码
```
示例如

```
docker run -itd --net=host --restart=always --name baota cyberbolt/baota:latest -port 8888 -username cyberbolt -password abc123456
```

--net=host : 容器和主机使用同一网络

--restart=always: 守护进程，容器挂掉将自动重启

-port : 填写宝塔面板运行的端口号

-username: 填写宝塔面板的用户名

-password : 填写宝塔面板的密码

```
该方法的登录方式:

登陆地址: http://{{服务器的ip地址}}:{{您输入的端口号}}

账号: 您填写的用户名

密码: 您填写的密码

```
**如果您未自定义用户名和密码，直接使用的如下命令**

```
docker run -itd --net=host --restart=always --name baota cyberbolt/baota:latest
```

**宝塔面板也会自动创建，此时可通过默认信息登录，默认信息为**

```

登陆地址: http://{{服务器的ip地址}}:8888

账号: cyber

密码: abc12345

```

### 方案二（生产环境部署）

生产环境中，为了避免极小概率的数据丢失，我们将容器内的宝塔文件映射到宿主机的目录中（您之后安装的 Nginx、MySQL 等服务均会挂载到宿主机目录）。该方法是 Docker 部署宝塔面板的最优方案，可以在生产环境中运行。

首先按最简方案创建一个测试容器（为保存宝塔文件到宿主机目录中）

输入命令创建测试容器（这里仅为测试容器，为避免出错，后面几步请原封不动地复制粘贴）

```
docker run -itd --net=host --name baota-test cyberbolt/baota:latest -port 26756 -username cyberbolt -password abc123456
```

将 Docker 容器中的 /www 目录 拷贝至宿主机的 /www

```
docker cp baota-test:/www /www
```

拷贝完成后删除创建的测试容器

```
docker stop baota-test && docker rm baota-test
```

创建宝塔面板容器，并将宿主机目录映射至容器中（自行输入面板的 端口号、用户名 和 密码 后即可完成部署）

```
docker run -itd -v /www:/www --net=host --restart=always --name baota cyberbolt/baota:latest -port 端口号 -username 用户名 -password 密码
```

示例如

```
docker run -itd -v /www:/www --net=host --restart=always --name baota cyberbolt/baota:latest -port 8888 -username cyberbolt -password abc123456
```

--net=host : 容器和主机使用同一网络

--restart=always: 守护进程，容器挂掉将自动重启

-port : 填写宝塔面板运行的端口号

-username: 填写宝塔面板的用户名

-password : 填写宝塔面板的密码

```
该方法的登录方式:

登陆地址: http://{{服务器的ip地址}}:{{您输入的端口号}}

账号: 您填写的用户名

密码: 您填写的密码

```

部署成功！

电光笔记官网 [https://www.cyberlight.xyz/](https://www.cyberlight.xyz/)