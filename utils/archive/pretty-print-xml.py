from lxml import etree

def pretty_print_xml(file_path):
    try:
        tree = etree.parse(file_path)
        print(etree.tostring(tree, pretty_print=True).decode())
    except IOError as e:
        print(f"Error opening the file: {e}")
    except etree.XMLSyntaxError as e:
        print(f"Error parsing the XML: {e}")

# Example usage
file_path = "../STIGs/U_Google_Chrome_V2R9_STIG_SCAP_1-2_Benchmark.xml"
pretty_print_xml(file_path)
