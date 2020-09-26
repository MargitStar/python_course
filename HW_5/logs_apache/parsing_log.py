import re


def parse_log(path):
    ips = []
    browsers = {}
    with open(path, 'r') as file:
        for line in file:
            ip = get_ip(line)
            if ip:
                ips.append(ip)

            browser = get_browser(line)
            if browser:
                if browser in browsers:
                    browsers[browser] += 1
                else:
                    browsers[browser] = 1

    return ips, browsers


def get_ip(line):
    ip_reg = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    match = re.match(ip_reg, line)
    if not match:
        return
    return line[match.start():match.end()]


def get_browser(line):
    br_reg = r'[\w_-]+\/[\d\.]+'
    result = re.findall(br_reg, line)
    if not result:
        return
    return result[-1]


ip_list, browser_list = parse_log("access.log")
print("Amount of requests in file:")
print(len(ip_list))
print("Amount of unique ips: ")
print(len(set(ip_list)))
print("Amount of unique browsers: ")
print(browser_list.keys())

