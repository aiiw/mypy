import xml.etree.ElementTree as ET
tree = ET.parse('xx.xml')
root = tree.getroot()
print(root)
for i in root:
	print(i.tag)