## 1 Apache:Dynamic Content with CGI
### 1.1 配置Apache开启CGI模块

**ScriptAlias**

安装Apache到默认位置，可以在/etc/httpd/conf/httpd.conf配置文件中开启CGI模块，使用`ScriptAlias`命令，将本地存放CGI程序的特定目录映射为一个URL前缀。

`ScriptAlias "/cgi-bin/" "/usr/local/apache2/cgi-bin/"`

还有一种情况是CGI程序没有放在ScriptAlias特定目录中，可以通过两步可以解决这个问题。
1. 使用`AddHandler`或`SetHandler`命令激活cgi-script处理器。
2. 在`Options`命令中指定ExecCGI

```
<Directory "/home/*/public_html">
    Options +ExecCGI
    AddHandler cgi-script .cgi
</Directory>
```
这个配置是把public_html目录下所有以`.cgi`结尾的文件当作CGI程序执行。

```
<Directory "/home/*/public_html/cgi-bin">
    Options ExecCGI
    SetHandler cgi-script
</Directory>
```
这个配置是把cgi-bin目录所有的文件当作CGI程序执行。

### 1.2 编写CGI程序
```python
#!/usr/bin/env python
# encoding: utf-8

print('Content-type: text/html\n\n')
print('Hello, World.')
```

![](http://i65.tinypic.com/jfypv4.jpg)

第一行指定使用的解释器；第四行输出一个`MIME-type`头(是一种描述正在传输的文档类型的方法，一些类型有：text/html, image/gif, and application/octet-stream，在HTTP中，它在Content-type头中传输)，它告诉客户端接收的内容类型。通常是HTML文档，但是也有可能编写一个CGI程序，输出gif图片或非HTML内容。

编写完CGI程序后，给它赋予执行权限，因为服务器启动时，它是以非特权用户运行的。如果CGI程序需要从其他文件读入或向其他文件写数据，那么它也要有这些文件的可读、可写权限。

通过Web服务器运行CGI程序和在命令行运行是不一样的，在命令行运行可能不会考虑传递给shell的信息，比如`PATH`，但是CGI程序运行时会找不到这些变量，所以在程序中要指定一个完整的解释器路径。

影响Apache HTTP服务器的环境变量有两类：一种是底层操作系统控制的环境变量，比如PATH、hostname、username等，它们可以通过`PassEnv`传递给CGI程序；第二种是Apache中存储信息的变量也称为环境变量，比如在CGI事物期间，服务器和浏览器也设置了环境变量，以便它们可以互相通信，这些变量包括浏览器类型(Netscape, IE, Lynx)、服务器类型(Apache, IIS, WebSite)、CGI程序名等。这些变量对CGI程序都是可用的，它们构成客户端-服务器通信的一半。

服务器与客户端之间的通信发生在标准输入(STDIN)和标准输出(STDOUT)间。通常，STDIN意味着键盘或用来执行的一个程序文件，STDOUT意味着控制台或屏幕。当POST一个表单到CGI程序时，表单数据被打包成特殊格式通过STDIN交付给CGI程序。程序然后处理数据，就像这些数据来自键盘或一个文件。

“特殊格式”非常简单，字段名和它的值用等号(=)连成一对，数值对之间用&符号连接，对于空格、其他符号，将它们转为16进制表示。比如下面这样：
`name=Rich%20Bowen&city=Lexington&state=KY&sidekick=Squirrel%20Monkey`
在URL后面附加类似的字符串，叫做GET请求。服务器收到后，会把字符串存储到`QUERY_STRING`环境变量中。通过设置`FORM`标签中的`METHOD`属性，决定表单使用GET还是POST方法交付数据。

## 2 Web中的角色
![](http://i68.tinypic.com/x21onc.jpg)
