import json
import csv
import argparse
import sys
import os
# For MIME types

import mimetypes
from IANAWriteCSVFileWithPandas import write_csv_ports_services_pandas


try:
    import pandas as pd
except ImportError as error:
    sys.exit(f"PANDA IS NOT INSTALLED\n{error} We will try to inspect CSV file anyway.wit")


def final_search(file_name, term_for_search=None):
    # search_dict = {"TermToSearch": {"Transport Protocol": args.protocol}
    if term_for_search is None:
        raise ValueError("Nothing to search.")
    with open(file_name, mode="r", newline='') as csv_fstream:
        csv_reader = csv.DictReader(csv_fstream)
        full_csv_data = []
        # Service Name,Port Number,Transport Protocol,Description,Assignee,Contact,Registration Date,Modification Date,Reference,Service Code,Unauthorized Use Reported,Assignment Notes
        headers = csv_reader.fieldnames
        output_data = []

        for row in csv_reader:
            for key in term_for_search:

                if term_for_search[key] == row[key]:
                     output_data.append(row)

        return output_data


def is_there_a_file(dir_path):
    if os.path.exists(dir_path):
        if os.path.isdir(dir_path):
            files = os.listdir(dir_path)
            file_path = os.path.join(dir_path, sorted(files)[-1])  # if more than 1 file return most recent one (alpha)O
            if os.path.isfile(file_path):
                if mimetypes.MimeTypes().guess_type(file_path)[0] == "text/csv":
                    return file_path
                else:
                    return None


def get_csv_file_from_iana():
    try:
        from IANAWriteCSVFileWithPandas import write_csv_ports_services_pandas
        import IANAScrapper
        write_csv_ports_services_pandas()  # TRy to getin csv with pandas http cvs import
    except ImportError as error:
        try:
            import IANAScrapper
            IANAScrapper.init_scrapping_IANA()  # scrap IANA wit http requests and bs4
        except ImportError as error_1:
            return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='[ IANA ] Search for ports or services in IANA CSV FILE',
        epilog='''
                                            grep csv instead or regex it! 
                                            '''
    )
    parser.add_argument('--port',
                        required=False,
                        help='port to search: e.g. --port=443'
                        )
    parser.add_argument('--service_name',
                            required=False,
                            help='port to search: e.g. --service_name=dns'
                            )
    parser.add_argument('--protocol',
                            required=False,
                            help='port to search: e.g. --protocol=udp'
                            )

    args = parser.parse_args()

    #FILE_PATH = "CollectedData/20210620_120253098961_WellKnownPortsAndServicesPANDASMODE.csv"
    DIR_PATH = "CollectedData"
    FILE_PATH = is_there_a_file(DIR_PATH)
    print("-------------------------")
    print(FILE_PATH)

    def search_here(file_path, term_to_search):
        if file_path:
            # csv SEARCH QUERY WITH python csv tools
            # search(file_path, ["radius", "http", "https"])
            # search(file_path, [7680])
            data = final_search(file_path, term_to_search)
        else:

            get_csv_file_from_iana()
            file_path = is_there_a_file(DIR_PATH)
            print(file_path)
            if file_path:
                data = final_search(file_path, term_to_search)

        if data:
            for element in data:
                print(json.dumps(element, indent=4))


    search_dict = None
    if args:
        if args.port:
            search_dict =  {"Port Number": args.port}
        if args.service_name:
            search_dict = {"Service Name": args.service_name}
        if args.protocol:
            search_dict = {"Transport Protocol": args.protocol}

        if search_dict is not None:
            search_here(file_path=FILE_PATH, term_to_search=search_dict)
        else:
            print("We need  port, service_name or protocol")





    # TODO Later Aligator :
    #  search_with_pandas(file_path, ["radius", "http", "https"])
