from lxml import etree as ET
import pandas as pd
import argparse
import warnings
warnings.filterwarnings("ignore")
parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', help='filename 属性,文件路径，必要属性',default="FoodServiceData.csv")
parser.add_argument('--output', '-o', help='filename 属性,文件路径，必要属性',default="FoodServiceData.xml")
args = parser.parse_args()
def csv2xml(input_file, output):
    data = pd.read_csv(input_file)
    root = ET.Element('foodservices')
    columns = [column for column in data]
    for index in data.index:
        child = ET.SubElement(root,'foodservice')
        for column in columns:
            if not pd.isnull(data.loc[index,column]):
                grand_child = ET.SubElement(child,column)
                grand_child.text = str(data.loc[index,column])
    tree= ET.ElementTree(root)
    tree.write(output,pretty_print=True, xml_declaration=True, encoding='utf-8')
if __name__ == '__main__':
    csv2xml(args.input,args.output)
