import xml.etree.ElementTree as etree

tree = etree.parse("8_xmlFile.xml")

root = tree.getroot()

for child in root:
  print("\n",child.tag, child.attrib)
  
  for i in range (len(child)):
    print(child[i].tag," : ",child[i].text)

