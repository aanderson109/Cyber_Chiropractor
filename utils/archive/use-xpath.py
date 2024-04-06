from lxml import etree

def print_first_level_tags(file_path):
    try:
        tree = etree.parse(file_path)
        root = tree.getroot()
        # Direct children of the root
        for child in root:
            print(child.tag)
    except etree.XMLSyntaxError as e:
        print(f"Error parsing the XML: {e}")

# Example usage
file_path = "../STIGs/U_Google_Chrome_V2R9_STIG_SCAP_1-2_Benchmark.xml"
print_first_level_tags(file_path)
