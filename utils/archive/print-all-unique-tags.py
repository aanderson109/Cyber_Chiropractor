from lxml import etree

def list_unique_tags(file_path):
    unique_tags = set()

    try:
        tree = etree.parse(file_path)
        for element in tree.iter():
            unique_tags.add(element.tag)
    except etree.XMLSyntaxError as e:
        print(f"Error parsing the XML: {e}")

    for tag in sorted(unique_tags):
        print(tag)

# Example usage
file_path = "../STIGs/U_Google_Chrome_V2R9_STIG_SCAP_1-2_Benchmark.xml"
list_unique_tags(file_path)
