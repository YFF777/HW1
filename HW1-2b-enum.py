from lxml import etree
import argparse
import warnings
warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', help='filename 属性,文件路径，必要属性',default="FoodServiceData.xml")
args = parser.parse_args()
def count(input_file):
    root = etree.parse(input_file).getroot()
    childs = root.getchildren()
    types_dic = {}
    for child in childs:
        for children in child.getchildren():
            if children.tag == 'TypeDescription':
                if children.text in types_dic:
                    types_dic[children.text] += 1
                else:
                    types_dic[children.text] = 1
    print(sorted(types_dic.items(), key = lambda x:x[1],reverse = True))
if __name__ == '__main__':
    count(args.input)


