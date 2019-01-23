# PDF处理工具

目前包含如下两个pdf工具
- 给PDF添加书签
- 合并多个pdf文件为一个

## 给PDF工具添加书签
方便为pdf文件生成对应的书签，只需要编写好对应的书签文件即可，使用方式如下：
```bash
# python bookmarker.py

usage: bookmarker.py [-h] [-c C] [-p P] [-b B] [-o O] [--offset OFFSET] [-f F]

optional arguments:
  -h, --help       show this help message and exit
  -c C             Book configuration file path which store book and it's
                   bookmarks metadata
  -p P             The pdf file path
  -b B             The bookmarks file
  -o O             Directory of generated file. Same folder if not specified.
  --offset OFFSET  The page offset in pdf document
  -f F             File name of generated file
```

## 合并PDF文件
见代码 pdf_merge.py