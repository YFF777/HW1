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
    grades_dic = {}
    for child in childs:
        for children in child.getchildren():
            if children.tag == 'Grade':
                if children.text in grades_dic:
                    grades_dic[children.text] += 1
                else:
                    grades_dic[children.text] = 1
    print(sorted(grades_dic.items(), key = lambda x:x[1],reverse = True))
if __name__ == '__main__':
    count(args.input)

