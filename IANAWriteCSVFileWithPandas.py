import os
from datetime import datetime
try:
    import pandas as pd
except ImportError as error:
    raise ImportError(f"Problems with Pandas Module; Check if is installed\n \tERROR:\n\t{error}")


def write_csv_ports_services_pandas():
    """
    This function, will try to download csv file from IANA, containing WELL KNOWN PORTS AND SERVICES
    Will try to store the file in the hard drive

    :return: <Pandas.DataFrame> with data loaded from csv_file
    """

    # Method 2
    # simple method
    # # reading csv file from url

    # Where to get the csv FILE
    _url = "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv"

    # LOAD DATA FROM WEB TO PANDAS
    data_frame = pd.read_csv(_url)
    print(data_frame.head(20))
    print(data_frame.tail(20))

    date_time = datetime.now().strftime("%G%m%d_%H%M%S%f")
    csv_file_name = date_time + "_" + "WellKnownPortsAndServicesPANDASMODE.csv"
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
    return data_frame


if __name__ == "__main__":
    write_csv_ports_services_pandas()