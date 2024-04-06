from lxml import etree

def process_definitions(file_path):
    try:
        # Load and parse the XML file
        tree = etree.parse(file_path)
        root = tree.getroot()

        # Update the namespace dictionary with the OVAL namespace
        ns = {
            'oval_def': 'http://oval.mitre.org/XMLSchema/oval-definitions-5',
            'oval_com': 'http://oval.mitre.org/XMLSchema/oval-common-5'
        }

        # Now searching for oval_definitions and definitions with the correct namespace
        definitions = root.findall('.//oval_def:definitions/oval_def:definition', namespaces=ns)
        print(f"Found {len(definitions)} definitions.")
        
        for definition in definitions:

            # ID basic info
            def_id = definition.get('id')
            def_class = definition.get('class')
            title = definition.find('.//oval_def:metadata/oval_def:title', namespaces=ns).text
            description = definition.find('.//oval_def:metadata/oval_def:description', namespaces=ns).text
            
            # now the affected info
            affected_family = "N/A"
            platforms_list = []
            affected = definition.find('.//oval_def:metadata/oval_def:affected', namespaces=ns)
            if affected is not None:
                affected_family = affected.get('family')
                platforms = affected.findall('.//oval_def:platform', namespaces=ns)
                platforms_list = [platform.text for platform in platforms]
          
            # criteria information
            criteria = definition.find('.//oval_def:criteria', namespaces=ns)
            if criteria is not None:
                for criterion in criteria.findall('.//oval_def:criterion', namespaces=ns):
                    test_ref = criterion.get('test_ref')
                    comment = criterion.get('comment')



            # print definition details
            print(f"Definition ID: {def_id}")
            print(f"Class: {def_class}")
            print(f"Affected Family: {affected_family}")
            print("Platforms:")
            for platform in platforms_list:
                print(f" - {platform}")
            print(f"Title: {title}")
            print("Description:")
            print(description)
            print("Criteria:")
            print(f" - Test Ref.: {test_ref}")
            print(f" - Comment: {comment}")
            print("----------\n")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
#file_path = "../STIGs/U_Google_Chrome_V2R9_STIG_SCAP_1-2_Benchmark.xml"
#print_scap_stig_contents(file_path)
