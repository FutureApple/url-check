# URL状态检测

> 本工具依赖Python Requests库，在Python 3版本中运行

本工具可以批量区分大量链接中正常的链接和不能正常使用的链接

将要检测的URL写入进 **url-in.txt** 然后运行即可

URL写入示范

```
一行一个
https://lo-li.icu
https://lo-li.icu/404
https://cloudflare.com
```

输出文件 **url-out.txt** 中会输出返回200的URL，一行一个
