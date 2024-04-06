import re
from lxml import etree

def print_scap_stig_contents(file_path):
    try:
        # Load and parse the SCAP (XCCDF) XML file
        tree = etree.parse(file_path)
        root = tree.getroot()

        # Define the namespaces, XCCDF is often used in STIGs
        ns = {
            'xccdf': 'http://checklists.nist.gov/xccdf/1.2'
        }

        # Regular expression to match and remove the unwanted pattern
        pattern = re.compile(r'xccdf_mil\.disa\.stig_rule_(.*?)_rule')

        # Print general information about the benchmark (STIG)
        title = root.find('.//xccdf:title', ns)
        description = root.find('.//xccdf:description', ns)
        print(f"Benchmark Title: {title.text if title is not None else 'N/A'}")
        print(f"Description: {description.text if description is not None else 'N/A'}\n")

        # Iterate through the rules
        for rule in root.findall('.//xccdf:Rule', ns):
            rule_id = rule.get('id')

            # Use regular expression to clean up the rule ID
            clean_rule_id = pattern.sub(r'\1', rule_id)

            rule_title = rule.find('xccdf:title', ns)
            rule_weight = rule.get('weight')
            rule_severity = rule.get('severity')
            rule_description = rule.find('.//xccdf:description', ns)

            print(f"Rule ID: {clean_rule_id}")
            print(f"Title: {rule_title.text if rule_title is not None else 'N/A'}")
            print(f"Weight: {rule_weight}")
            print(f"Severity: {rule_severity}")
            print(f"Description: {rule_description.text if rule_description is not None else 'N/A'}\n")
            print("----------\n")

    except IOError as e:
        print(f"Error opening the file: {e}")
    except etree.XMLSyntaxError as e:
        print(f"Error parsing the XML: {e}")

# Example usage
file_path = "../STIGs/U_Google_Chrome_V2R9_STIG_SCAP_1-2_Benchmark.xml"
print_scap_stig_contents(file_path)
