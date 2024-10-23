def get_class(ip_address):
    first_octet = int(ip_address.split(".")[0])
    if 0 < first_octet < 128:
        return "A"
    elif 128 <= first_octet < 192:
        return "B"
    elif 192 <= first_octet < 224:
        return "C"
    elif 224 <= first_octet < 240:
        return "D"
    elif 240 <= first_octet < 256:
        return "E"
    else:
        return "Invalid IPv4 address"


def get_subnet_mask(ip_class):
    if ip_class == "A":
        return '255.0.0.0'
    elif ip_class == "B":
        return '255.255.0.0'
    elif ip_class == "C":
        return '255.255.255.0'
    else:
        return 'Invalid IPv4 address'


def get_network_address(ip_address, subnet_mask):
    ip_octet = list(map(int, ip_address.split(".")))
    subnet_octet = list(map(int, subnet_mask.split(".")))
    network_address = [ip_octet[i] & subnet_octet[i] for i in range(4)]
    return ".".join(map(str, network_address))


def get_broadcast_address(ip_address, subnet_mask):
    ip_octet = list(map(int, ip_address.split('.')))
    subnet_octet = list(map(int, subnet_mask.split('.')))
    broadcast_address = [(ip_octet[i] | (~subnet_octet[i] & 255)) for i in range(4)]
    return '.'.join(map(str, broadcast_address))


def get_first_add(network_address):
    octet = list(map(int, network_address.split('.')))
    for i in range(3, -1, -1):
        if octet[i] < 255:
            octet[i] += 1
            break
        else:
            octet[i] = 0
    return '.'.join(map(str, octet))


def get_last_add(broadcast_address):
    octet = list(map(int, broadcast_address.split('.')))
    for i in range(3, -1, -1):
        if octet[i] > 0:
            octet[i] -= 1
            break
        else:
            octet[i] = 255
    return '.'.join(map(str, octet))


def main():
    ip_address = input("Enter IPv4 address (e.g., 192.168.1.1): ")
    ip_class = get_class(ip_address)
    print(f"Class: {ip_class}")

    subnet_mask = get_subnet_mask(ip_class)
    print(f"Subnet mask: {subnet_mask}")

    network_address = get_network_address(ip_address, subnet_mask)
    print(f"Network address: {network_address}")

    broadcast_address = get_broadcast_address(ip_address, subnet_mask)
    print(f"Broadcast address: {broadcast_address}")

    first_add = get_first_add(network_address)
    print(f"First address: {first_add}")

    last_add = get_last_add(broadcast_address)
    print(f"Last address: {last_add}")


if __name__ == "__main__":
    main()
