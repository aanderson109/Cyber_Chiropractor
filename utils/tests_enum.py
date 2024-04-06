from lxml import etree

def enumerate_tests(file_path):
    try:
        # Load and parse the XML file
        tree = etree.parse(file_path)
        root = tree.getroot()

        # Assuming namespaces are the same as previously defined
        ns = {
            'oval_def': 'http://oval.mitre.org/XMLSchema/oval-definitions-5',
            'win_def': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows'
        }

        # Process definitions (assuming this code already exists)
        # ...

        # Process tests
        tests = root.findall('.//oval_def:tests', namespaces=ns)
        for test in tests:
            registry_tests = test.findall('.//win_def:registry_test', namespaces=ns)
            print(f"Found {len(registry_tests)} registry tests.")
            
            for registry_test in registry_tests:
                test_id = registry_test.get('id')
                comment = registry_test.get('comment')
                check_existence = registry_test.get('check_existence')
                check = registry_test.get('check')
                object_ref = registry_test.find('.//win_def:object', namespaces=ns).get('object_ref')
                state_refs = [state.get('state_ref') for state in registry_test.findall('.//win_def:state', namespaces=ns)]

                print(f"Test ID: {test_id}")
                print(f"Comment: {comment}")
                print(f"Check Existence: {check_existence}")
                print(f"Check: {check}")
                print(f"Object Ref: {object_ref}")
                print("State Refs:")
                for state_ref in state_refs:
                    print(f" - {state_ref}")
                print("----------\n")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
#file_path = "../STIGs/U_Google_Chrome_V2R9_STIG_SCAP_1-2_Benchmark.xml"
#print_scap_stig_contents(file_path)
