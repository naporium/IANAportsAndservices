import sys
from time import sleep
from datetime import datetime
import os
try:
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
except ImportError as error:
    raise ImportError(f"ERROR WHILE IMPORTING EXTERNAL MODULES.\n\tERROR:\n\t{error}")


def get_table_headers_and_important_var_data():
    default_start_page_to_scrap = "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?&page=1"

    # Redundant for clarity
    url = default_start_page_to_scrap

    # Create a handle, page, to handle the contents of the website
    page = requests.get(url=url)

    if page.status_code == 200:
        print("Page is ready to parse.")
    else:
        sys.exit(f"Something went wrong.\nHtml Status Code: {page.status_code}")

    # START BEAUTIFUL SOUP
    soup_obj = BeautifulSoup(page.text, 'html.parser')

    table_headers = soup_obj.thead
    table_headers = table_headers.find_all("th")

    # List to store columns names
    table_headers_lst = []

    for count, element in enumerate(table_headers):
        # print(count, element.get_text())
        table_headers_lst.append(element.get_text())

    # print(table_headers_lst)

    # Find number_of pages_ in "pagination"
    pagination = soup_obj.find_all(class_='pagination')
    string_of_pages = pagination[0].get_text()
    number_of_pages = string_of_pages.split(" ")
    last_page_number = int(number_of_pages[-1])
    current_page_number = int(number_of_pages[1])
    # print("Current page:", current_page_number)
    # print("Last page:", last_page_number)
    #current_page_number = current_page_number + 1  # We started at page 1 SO LETS INCREMENT ONE

    # TODO
    # ITERATE OVER EACH PAGE... from current_page to last_page
    base_page_url = default_start_page_to_scrap.split("=")[0]
    current_page_id = int(default_start_page_to_scrap.split("=")[1])


    # print("Base_page_url", base_page_url)
    # print("Current_page_id page", current_page_id)
    pages = []
    for i in range(current_page_id, last_page_number + 1):
        # print(base_page_url + "=" + str(i))
        page_url = base_page_url + "=" + str(i)
        # print(f"page_id: {str(i)}; page_url:{page_url}")
        page_id = i
        pages.append((page_id, page_url))
    return table_headers_lst, pages


# FOR LOOP ON PAGES
def get_table_data_from_IANA(url_page_to_get_data):

    # Redundant for clarity
    url = url_page_to_get_data

    # Create a handle, page, to handle the contents of the website
    page = requests.get(url=url)

    if page.status_code == 200:
        print("Page is ready to parse.")
    else:
        sys.exit(f"Something went wrong.\nHtml Status Code: {page.status_code}")

    # START BEAUTIFUL SOUP
    soup_obj = BeautifulSoup(page.text, 'html.parser')

    # TRY TO EXTRACT BODY table
    table_body = soup_obj.tbody
    table_body_rows = table_body.find_all("tr")
    all_rows_data = []  # list containing all columns values

    for count, row_element in enumerate(table_body_rows):
        # print("=" * 30)
        # print("Start --- row printing")
        # print("\t\t\t\t\t\Len(row)", len(row_element))
        # print(count, row_element)
        _table_columns = row_element.find_all("td")

        # print(type(_table_columns))
        _c = []  # temporary list to store each row (columns values)
        for column_count, columns in enumerate(_table_columns):
            # print("-" * 15)
            try:
                # print(column_count, columns.get_text(), end="\t")
                # print(type(columns.get_text()))
                _c.append(columns.get_text())
            except:
                # print(" ", end="\t")
                _c.append("")
        # print("\n")
        all_rows_data.append(_c)
        # print(_c)
        _c = []  # reset temporary list for columns values

    # print("@" * 90)
    # for row in all_rows_data:
    #     print(row)
    return all_rows_data


def init_scrapping_IANA():
    """
    This function is dependent of 2 above functions:
        - get_table_data_from_IANA
        - get_table_headers_and_important_var_data

    It will write a csv file with all services names and ports,
    scrapped from IANA.org web page,
    And will also return a Dataframe, and a tupple

    :return: <pandas.DataFrame>
             <tuple> this tuple contains a python list with table headers(columns names),
             and a python list with data, corresponding to data rows
    """

    table_headers, pages_to_scrap_list = get_table_headers_and_important_var_data()
    print(f"Table Headers: {table_headers}")

    total_rows = [] # AN empty list to accommodate ALL REGISTRIES FROM ALL TABLES
    temporary_data_rows = []

    print("=" * 80)
    # ITERATE PAGES
    for page in pages_to_scrap_list:
        # page: (page_id, page_url)
        print(f"Scraping page_id number: {page[0]}; page_url: {page[1]}")
        # WE SHOULD sleep
        print(f"Total number of pages to scrap: {str(len(pages_to_scrap_list))}")
        print(f"Remaining number of pages to scrap: {str(len(pages_to_scrap_list) - int(page[0]))}")
        temporary_data_rows = get_table_data_from_IANA(url_page_to_get_data=page[1])
        print(f"Number of collect rows/registries from page id_{str(page[0])}: {len(temporary_data_rows)} ")
        print("Sleeping Mode Activated for 5 seconds.")
        sleep(5)  # TO NOT OVERLOAD SERVER WITH REQUESTS

        #  # Rationale for this:
        #         # IANA tables PAGINATION:
        #         # when we go to the next thml page, first row/element  in the html table,  is equal(REPEATED)
        #         # to last element/raw from previous page
        # Since we get all the rows from html table
        # with the function get_table_data_from_IANA,
        # we down need to copy the first element to the final/output list
        if page[0] == 1:
            total_rows.extend(temporary_data_rows)
        else:
            total_rows.extend(temporary_data_rows[1:])
        print("=" * 80)
        # if page[0] == 4:
        #     print(total_rows)
        #     break

    # print("Numero de rgistos conseguidos:", len(total_rows))

    # CONVERT DATA TO PANDAS.Dataframe
    data_frame = pd.DataFrame(total_rows, columns=table_headers)
    # print(data_frame)
    # print(data_frame.to_string())

    date_time = datetime.now().strftime("%G%m%d_%H%M%S%f")
    csv_file_name = date_time + "_" + "WellKnownPortsAndServices.csv"
    folder_name = "CollectedData"

    if os.path.exists(folder_name):
        if os.path.isdir(folder_name):
            csv_file_path = os.path.join(folder_name, csv_file_name)
    else:
        try:
            os.makedirs(folder_name)
            csv_file_path = os.path.join(folder_name, csv_file_name)

        except OSError as error:
            print(f"Couldn't create folder: {folder_name}\n error")
            csv_file_path = csv_file_name

    print("We will try to write on file:", csv_file_path)
    try:
        data_frame.to_csv(csv_file_path)
    except OSError as error:
        print(f"Error while creating csv file\nError: {error}")

    return data_frame, (table_headers, total_rows)


if __name__ == '__main__':
    _data_frame, table_list_data = init_scrapping_IANA()
    columns_name = table_list_data[0]
    rows_data = table_list_data[1]
    # print(f"NUMERO REGISTOS CONSEGUIDOS: {str(len(rows_data))}")
    # print(_data_frame.to_string())
    print(_data_frame.dtypes)
    print(_data_frame.info())
    print(_data_frame.head())
    print(_data_frame.tail())

    # data_frame_tojson
    # from json import loads, dumps
    # json_data = _data_frame.to_json()
    # js = loads(json_data)

