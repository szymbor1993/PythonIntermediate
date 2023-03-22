#TODO: Either validate manually arguments, or catch a potential exception. Follow the
# hints in the comments.
def sum_positive_numbers(*args):
    # hint: what if any provided item is not a number?
    return sum(num for num in args if num > 0)

    
def get_longest_remote_entry(ip_addr, file_path):
    import subprocess
    # hint: assume that 'subprocess.run' can raise some error
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


if __name__ == "__main__":
    # If you want to test these function here, you can do it on your own,
    # as especially for exercises 1, cases prepared by me would be too big hint for you
    # ;) and in 2nd exercise I cannot provide any reliable test case, because of fact
    # that you don't have the same machines/OS/configuration.
    pass
