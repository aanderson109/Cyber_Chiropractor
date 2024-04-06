from lxml import etree

def enumerate_objects(file_path):
    try:
        # Load and parse the XML file
        tree = etree.parse(file_path)
        root = tree.getroot()

        # Assuming namespaces are the same as previously defined
        ns = {
            'oval_def': 'http://oval.mitre.org/XMLSchema/oval-definitions-5',
            'win_def': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows'
        }

        # Assuming definitions and tests processing code already exists here...

        # Process objects
        objects = root.findall('.//oval_def:objects', namespaces=ns)
        for obj in objects:
            registry_objects = obj.findall('.//win_def:registry_object', namespaces=ns)
            print(f"Found {len(registry_objects)} registry objects.")
            
            for registry_object in registry_objects:
                object_id = registry_object.get('id')
                version = registry_object.get('version')
                hive_element = registry_object.find('.//win_def:hive', namespaces=ns)
                key_element = registry_object.find('.//win_def:key', namespaces=ns)
                name_element = registry_object.find('.//win_def:name', namespaces=ns)

                hive = hive_element.text if hive_element is not None else "None"
                key = key_element.text if key_element is not None else "None"
                name = name_element.text if name_element is not None else "None"

                print(f"Object ID: {object_id}")
                print(f"Version: {version}")
                print(f"Hive: {hive}")
                print(f"Key: {key}")
                print(f"Name: {name}")
                print("----------\n")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
#file_path = "../STIGs/U_Google_Chrome_V2R9_STIG_SCAP_1-2_Benchmark.xml"
#print_scap_stig_contents(file_path)
