
def main():
    data = """    
    # The latest IANA port assignments can be gotten from
    #       http://www.iana.org/assignments/port-numbers
    # The Well Known Ports are those from 0 through 1023.
    # The Registered Ports are those from 1024 through 49151
    # The Dynamic and/or Private Ports are those from 49152 through 65535
    """
    print(data)
    private = "    # According to standards set forth in Internet Engineering Task Force (IETF)\n" \
              "    # document RFC-1918 , the following IPv4 address ranges are reserved by the IANA\n" \
              "    # for private internets, and are not publicly routable on the global internet:\n" \
              "    # 10.0.0.0/8     IP addresses: 10.0.0.0    – 10.255.255.255\n" \
              "    # 172.16.0.0/12  IP addresses: 172.16.0.0  – 172.31.255.255\n" \
              "    # 192.168.0.0/16 IP addresses: 192.168.0.0 – 192.168.255.255\n" \
              "    # SOURCE: https://www.arin.net/reference/research/statistics/address_filters/"
    print(private)


if __name__ == "__main__":
    main()