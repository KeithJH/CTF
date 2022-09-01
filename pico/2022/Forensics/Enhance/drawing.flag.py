#!/usr/bin/env python3
import xml.etree.ElementTree as ET

tree = ET.parse("./drawing.flag.svg")
root = tree.getroot()
flagParts = [i.text.replace(" ", "") for i in root.findall(".//{*}tspan")]

flag = ''.join(flagParts)
print(flag)

