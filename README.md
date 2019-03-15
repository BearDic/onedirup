# OneDirUp

onedrivecmd Directory Upload

onedrivecmd 的目录上传脚本

## 功能

使用递归的方式弥补了 onedrivecmd 不带目录上传的功能, 且能够在失败时自动重试. 

此处的失败仅限于: python 抛出异常, 或者提示 `Annotations must be specified before other elements in a JSON object`. 重试次数目前为无限次. 

## 安装

需要先安装 onedrivecmd 和 python3, 然后把 onedirup.py 克隆到本地即可.

## 使用

运行

`python3 onedirup.py "/tmp/hello" "od:/foo/bar/" [--dry-run] [--no-try-again]`

其中: 

`--dry-run`: 测试上传, 列出要上传的文件以及命令, 但是不执行.

`--no-try-again`: 禁用在失败时自动重试功能.  

原地址和目标地址的引号**最好加上**, 路径中有空格时必须加上. 

**源**可以是文件夹, 也可以是文件, 结尾的斜杠 `/` 可加可不加. 

**目标地址**一定是一个 OneDrive 中的文件夹, 结尾的斜杠也可随意.

**运行结果**: 无论是文件还是文件夹, `hello` 都会被上传到 `od:/foo/bar/` 下, 也就是 `od:/foo/bar/hello`. 



