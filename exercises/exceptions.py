#TODO: Either validate manually arguments, or catch a potential exception. Follow the
# hints in the comments.
def sum_positive_numbers(*args):
    # what if any provided item is not a number?
    return sum(num for num in args if num > 0)

    
def get_longest_remote_entry(ip_addr, file_path):
    import subprocess
    # assume that 'subprocess.run' can raise some error
    # what else can go wrong?
    cmd = f"ssh {ip_addr} cat {file_path}"
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          encoding="utf-8")
    rows = proc.stdout.split('\n')
    longest_entry = rows[0]
    for i in range(1, len(rows)):
        if len(rows[i]) > len(longest_entry):
            longest_entry = rows[i]
    
    print(longest_entry)
