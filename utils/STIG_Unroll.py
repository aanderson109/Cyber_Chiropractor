from definitions_test import process_definitions
from objects_enum import enumerate_objects
from rule_definition_with_cleaning import enumerate_rules
from tests_enum import enumerate_tests
import art

def main(file_path):
    art.tprint("name & rules", font="small")
    enumerate_rules(file_path)
    art.tprint("OVAL", font="small")
    process_definitions(file_path)
    art.tprint("TESTS", font="small")
    enumerate_tests(file_path)
    art.tprint("OBJECTS", font="small")
    enumerate_objects(file_path)

if __name__ == "__main__":
    art.tprint("stig unroller", font="slant")
    file_path = "../STIGs/U_Google_Chrome_V2R9_STIG_SCAP_1-2_Benchmark.xml"
    main(file_path)