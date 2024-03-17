# AI接口大全

[中文](#jump1)
[English](#jump2)



## <span id="jump1">中文文档</span>



### PIKA接口

环境为python3.x，依赖版本适配python3即可

> 项目目录

```markdown
│  api.py             //对外接口，项目启动器
│  cookie.txt				     //你的账号cookie
│  generate.py				    //发送视频生成请求
│  authorization.txt  //账号token
└─static					         //下载后的视频存储
```



> 部署

- 先将本项目pika下载到本地
- 在cookie.txt填写你的账号的cookie，在authorization.txt填写token
- 到api.py的测试下发送请求

 ![pika-1](doc/images/pika-1.png)

>参生后的数据为一个falsk本地请求连接用于访问，自己部署falsk项目

 ![pika-2](doc/images/pika-2.png)

>本地存储在static目录下

 ![pika-3](doc/images/pika-3.png)
###  ChatGPT接口

> 待写

***国内用户需要魔法代理***















### <span id="jump2">English Documentation</span>



### PIKA interface

The environment is python3.x, and the dependency version can be adapted to python3

> Project directory


```markdown
│  api.py           // External interface, project launcher
│  cookie.txt				  // Your account cookie
│  generate.py				 //Send a video generation request
│  authorization.txt  //Your account authorization
└─static					 //Video storage after download
```

> Deployment

- Download the pika of the project to your local computer
- Fill in the cookie of your account in the cookie.txt and the token in the authorization.txt
- Send the request under the test to the api.py

 ![pika-1](doc/images/pika-1.png)

> the data after the birth is a FALSK local request connection for access, and you can deploy the FALSK project yourself , and port is 8081

 ![pika-2](doc/images/pika-2.png)

> stored locally in the static directory


 ![pika-3](doc/images/pika-3.png)
###  ChatGPT interface

> To be written

