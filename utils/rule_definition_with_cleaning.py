import re
from lxml import etree
from html import unescape

def enumerate_rules(file_path):
    try:
        # Load and parse the SCAP (XCCDF) XML file
        tree = etree.parse(file_path)
        root = tree.getroot()

        # Define the namespaces, XCCDF is often used in STIGs
        ns = {
            'xccdf': 'http://checklists.nist.gov/xccdf/1.2'
        }

        # Regular expression to match and remove the unwanted pattern from rule IDs
        pattern = re.compile(r'xccdf_mil\.disa\.stig_rule_(.*?)_rule')

        # Print general information about the benchmark (STIG)
        title = root.find('.//xccdf:title', ns)
        description = root.find('.//xccdf:description', ns)
        print(f"{title.text if title is not None else 'N/A'}")
        print(f"\n{description.text if description is not None else 'N/A'}\n")

        # Iterate through the rules
        for rule in root.findall('.//xccdf:Rule', ns):
            rule_id = rule.get('id')

            # Clean up the rule ID using the regular expression
            clean_rule_id = pattern.sub(r'\1', rule_id)

            rule_version = rule.find('xccdf:version', ns)
            rule_title = rule.find('xccdf:title', ns)
            rule_weight = rule.get('weight')
            rule_severity = rule.get('severity')
            rule_description = rule.find('.//xccdf:description', ns)
            rule_idents = rule.findall('.//xccdf:ident', ns)
            rule_fixtext = rule.find('xccdf:fixtext', ns)
            rule_fixref = rule_fixtext.get('fixref')

            print(f"Rule ID: {clean_rule_id}")
            print(f"Version: {rule_version.text}")
            print(f"Title: {rule_title.text if rule_title is not None else 'N/A'}")
            print(f"Weight: {rule_weight}")
            print(f"Severity: {rule_severity}")
            #print(f"Description: {rule_description}")
            #print(f"Description: {rule_description.text if rule_description is not None else 'N/A'}")
            
            if rule_description is not None and rule_description.text:
                # unescape to convert to actual tags
                desc_text = unescape(rule_description.text)
                # parse the unescaped description text as HTML/XML
                desc_tree = etree.fromstring(f"<root>{desc_text}</root>")
                
                print("Description:")
                # iterate through the parsed description's child elements
                for child in desc_tree:
                    child_tag = child.tag
                    child_text = child.text.strip() if child.text and child.text.strip() else 'N/A'
                    formatted_text = re.sub(r'\s+', ' ', child_text)
                    print(f" - {child_tag}: {formatted_text}")
            else:
                print("N/A")
            
            # iterate through and print all <xccdf:ident> elements
            print("Identifiers:")
            for ident in rule_idents:
                system = ident.get('system')
                ident_value = ident.text.strip() if ident.text else 'N/A'
                print(f" - {ident_value}")
            
            # print the fixtext and reference element for each rule
            print(f"Fix Ref.: {rule_fixref}")
            print(f"Fix Text: {rule_fixtext.text}")

            print("----------\n")

    except Exception as e:
        print(f"Error processing rules: {e}")
    
    try:

        # iterate through definitions
        print("DEFINITIONS:")
        definitions = root.findall('.//oval_definitions', ns)
        for definition in definitions:
            def_id = definition.get('id')
            def_version = definition.get('version')
            def_class = definition.get('class')

            print(f"Definition ID: {def_id}")
            print(f"Version: {def_version}")
            print(f"Class: {def_class}")

    except IOError as e:
        print(f"Error opening the file: {e}")
    except etree.XMLSyntaxError as e:
        print(f"Error parsing the XML: {e}")

# Example usage
#file_path = "../STIGs/U_Google_Chrome_V2R9_STIG_SCAP_1-2_Benchmark.xml"
#print_scap_stig_contents(file_path)