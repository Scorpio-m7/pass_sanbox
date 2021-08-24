# CS免杀&沙箱绕过

本文采用python，rc4加密，图片混淆，双分离绕过杀软，可以采用特定文件检测判断沙箱，也可以用自定义密码解锁

通过cs生成的python类型的shellcode

把shellcode通过脚本加密混淆到图片中`Usage:python generator.py YourRC4Key imgName`（图片尾部是shellcode）

```
E:\code\python\hack>python2 generator.py 123456 img1.jpg
Payload has write to shellcode_img1.jpg
```

把shellcode图片上传到github（云端）

将加载器通过脚本加密混淆到图片上传，可以直接使用load_img1.jpg

将sanbox_pass.py脚本上传目标

更改key1（shellcode的rc4密码）

更改key2（加载器的rc4密码）

更改shellcode的图片位置PayloadFileLocation

更改加载器的图片位置LoaderFileLocation

可以将my_exit中的1.txt改成只在真实机器才有的系统文件，来绕过沙箱

python2.7运行上线cs

可以使用pyinstalller打包成exe，替换windows图片混淆

得到shell后可以远程调用ps脚本欺骗用户卸载杀软，注意使用sublime修改编码格式为gbk
