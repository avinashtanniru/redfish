import random
import string

def get_password():
    # get random string of letters and digits
    source = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(source) for i in range(12)))
    return result_str
    # Output vZkOkL97

def export(filename, data, mode='a'):
    import csv
    if mode == 'h':
        xmode = 'w'
    else:
        xmode = mode
    with open(filename, xmode) as csvfile:
        fieldnames = ['HostName', 'Password']
        writer = csv.writer(csvfile)
        if mode == 'h':
            # writer.writeheader()
            writer.writerow(fieldnames)
        else:
            writer.writerow(data)
