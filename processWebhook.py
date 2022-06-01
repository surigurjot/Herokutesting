import collections.abc
#hyper needs the four following aliases to be done manually.
collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.MutableSet = collections.abc.MutableSet
collections.MutableMapping = collections.abc.MutableMapping

from xml.dom import minidom

root = minidom.Document()

response = root.createElement('response')
root.appendChild(response)

sayElement = root.createElement('Say')
sayElement.setAttribute('voice', 'woman')

sayElementText = root.createTextNode('Please leave a message after the tone.')

recordElement = root.createElement('Record')
recordElement.setAttribute('maxLength', '20')

response.appendChild(sayElement)
sayElement.appendChild(sayElementText)
response.appendChild(recordElement)

xml_str = root.toprettyxml(indent ="\t")

print(xml_str)
