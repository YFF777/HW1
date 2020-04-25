from lxml import etree
import sys

sys_args = sys.argv

in_book = sys_args[1]
out_book = sys_args[2]

with open(in_book, 'r', encoding='utf-8') as fp:
    html = fp.read()

dom = etree.HTML(html)
lis = dom.xpath('//div[@class="AllEditionsItem-tile Recipe-default"]')

root = etree.Element("books")

for li in lis:

    if 'Add to Cart' not in li.xpath("string(.)"):
        continue

    title = li.xpath('string(./div[1]/div[1])').strip()
    book = etree.SubElement(root, "book")

    etree.SubElement(book, 'title').text = title

    author = li.xpath('string(./div[1]/div[2])').strip()
    etree.SubElement(book, 'author').text = author

    price = li.xpath('./div[2]/div/div[2]/div[1]/div[1]/div[2]/text()')[0].strip()
    etree.SubElement(book, 'price').text = price

    _format = li.xpath('./div[2]/div/div[2]/div[2]/div[1]/strong/text()')[0].strip()
    etree.SubElement(book, 'format').text = _format

    condition = li.xpath('./div[2]/div/div[2]/div[2]/div[2]/strong/text()')[0].strip()
    etree.SubElement(book, 'condition').text = condition

    # print([title, author, price, _format, condition])


tree = etree.ElementTree(root)
tree.write(out_book, pretty_print=True, xml_declaration=True, encoding='utf-8')

print('over')