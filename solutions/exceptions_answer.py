def sum_positive_numbers_variant1(*args):
    try:
        return sum(num for num in args if num > 0)
    except TypeError:
        print("Some of arguments are not an integer")
        return 0


def sum_positive_numbers_variant2(*args):
    for item in args:
        if type(item) is not int:
            print(f"Argument {item} is not an integer")
            return 0

    return sum(num for num in args if num > 0)


def get_longest_remote_entry_variant1(ip_addr, file_path):
    import subprocess

    cmd = f"ssh {ip_addr} cat {file_path}"
    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              encoding="utf-8")
        rows = proc.stdout.split('\n')
    except Exception as ex:
        print(ex)
        return

    try:
        longest_entry = rows[0]
    except IndexError:
        print("List of entries is empty")
        return

    for i in range(1, len(rows)):
        if len(rows[i]) > len(longest_entry):
            longest_entry = rows[i]
    
    print(longest_entry)


def get_longest_remote_entry_variant2(ip_addr, file_path):
    import subprocess

    cmd = f"ssh {ip_addr} cat {file_path}"
    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              encoding="utf-8")
        rows = proc.stdout.split('\n')
    except Exception as ex:
        print(ex)
        return

    if not rows:
        print("List of entries is empty")
        return

    longest_entry = rows[0]
    for i in range(1, len(rows)):
        if len(rows[i]) > len(longest_entry):
            longest_entry = rows[i]
    
    print(longest_entry)
