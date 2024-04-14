import json
import xmltodict


class JSONConverter:
    def to_json(self, data):
        return json.dumps(data)

    def from_json(self, json_string):
        return json.loads(json_string)


class XMLConverter:
    def to_xml(self, data):
        return xmltodict.unparse({"data": data}, pretty=True)

    def from_xml(self, xml_string):
        return xmltodict.parse(xml_string)["data"]


class JSONToXMLAdapter:
    def __init__(self, json_converter):
        self.json_converter = json_converter

    def convert(self, json_data):
        json_string = self.json_converter.to_json(json_data)
        xml_converter = XMLConverter()
        return xml_converter.to_xml(self.json_converter.from_json(json_string))


class XMLToJSONAdapter:
    def __init__(self, xml_converter):
        self.xml_converter = xml_converter

    def convert(self, xml_data):
        xml_converter = XMLConverter()
        return xml_converter.from_xml(xml_data)


json_converter1 = JSONConverter()
xml_converter1 = XMLConverter()
json_data1 = {"name": "Molly", "age": 25}

json_to_xml_adapter = JSONToXMLAdapter(json_converter1)
xml_data1 = json_to_xml_adapter.convert(json_data1)
print(xml_data1)

xml_data1 = "<data><name>Molly</name><age>25</age></data>"
xml_to_json_adapter = XMLToJSONAdapter(xml_converter1)
json_data1 = xml_to_json_adapter.convert(xml_data1)
print(json_data1)
