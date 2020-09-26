def get_ips():
    import re
    ip_list = []
    ip_reg = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    with open("access.log", "r") as file:
        for index, line in enumerate(file):
            match = re.match(ip_reg, line)
            if not match:
                continue
            ip = line[match.start():match.end()]
            ip_list.append(ip)
    return ip_list


ips = get_ips()
print("Amount of requests in file:")
print(len(ips))

print("Amount of unique ip: ")
print(len(set(ips)))
