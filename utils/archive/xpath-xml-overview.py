from lxml import etree

def print_overview_of_xml_tree(file_path):
    try:
        tree = etree.parse(file_path)
        root = tree.getroot()

        # Print the root tag
        print(f"Root: {root.tag}")

        # Iterate through the direct children of the root and print their tags
        for child in root:
            print(f" - Child: {child.tag}")
            # If you also want to see grandchildren or further, you can add more nested loops here
            # For a simple overview, we're only going one level deep

    except IOError as e:
        print(f"Error opening the file: {e}")
    except etree.XMLSyntaxError as e:
        print(f"Error parsing the XML: {e}")

# Example usage
file_path = "../STIGs/U_Google_Chrome_V2R9_STIG_SCAP_1-2_Benchmark.xml"
print_overview_of_xml_tree(file_path)
