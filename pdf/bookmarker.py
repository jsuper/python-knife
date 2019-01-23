# coding:utf-8
# 给pdf文件添加书签，命令行工具入口
from pdf_utils import MyPDFHandler,PDFHandleMode as mode
from configparser import ConfigParser
import argparse
import os.path

def main():
    
    parser = argparse.ArgumentParser()

    parser.add_argument('-c',required=False, help='Book configuration file path which store book and it\'s bookmarks metadata')
    parser.add_argument('-p',required=False,help='The pdf file path')
    parser.add_argument('-b',required=False,help='The bookmarks file')
    parser.add_argument('-o',required=False,help='Directory of generated file. Same folder if not specified.')
    parser.add_argument('--offset', required=False,help='The page offset in pdf document')
    parser.add_argument('-f',required=False,help='File name of generated file')

    args = parser.parse_args()
    book_path=None
    offset=0
    bookmark_path=None
    output_path=None
    output_file_name = None

    if args.c == None:
        # Using command line arguments
        book_path = args.p
        bookmark_path = args.b
        output_file_name = args.f
        if args.offset:
            offset = int(args.offset)
    else:
        # Using configuration files
        if os.path.isfile(args.c):
            cf = ConfigParser()
            cf.read(args.c)
            book_path = cf.get('info','pdf_path')
            bookmark_path = cf.get('info','bookmark_file_path')
            offset = cf.getint('info','page_offset')
            output_file_name = cf.get('info','new_pdf_file_name') 
        else:
            print('Invalid configuration file.')

    
    if book_path==None or bookmark_path == None:
        parser.print_help()
        return -1

    if not os.path.isfile(book_path):
        print('Book file doesn\'t exist.')
        parser.print_help()
        return -1

    if not os.path.isfile(bookmark_path):
        print('Bookmark file doesn\'t exist.')
        parser.print_help()
        return -1
    
    if args.o == None and os.path.isdir(args.o):
        # not specified output directory. 
        output_path = os.path.dirname(book_path)
    else:
        output_path = args.o
        
    if output_file_name ==None:
        fn = os.path.basename(book_path)
        output_file_name = fn[:fn.rindex('.')]+'-bookmarked.pdf'

    output_file = output_path+"/"+output_file_name
    pdf_handler = MyPDFHandler(book_path,mode = mode.NEWLY)
    pdf_handler.add_bookmarks_by_read_txt(bookmark_path,page_offset = offset)
    pdf_handler.save2file(output_file)
    print('Done')


if __name__ == "__main__":
    main()