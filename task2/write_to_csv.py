from csv import writer

def csv_writer(filename: str, data: list, header = False, lines= 1):
    """
    Writes to a CSV-file, if header is added it processed automatically, default lines = 1, but multiple is possible
    """
    with open(f'{filename}.csv', 'a', encoding='UTF8') as f:
        write = writer(f, delimiter = ',')

        # write the header
        if header:
            write.writerow(header)

        # write multiple rows
        if lines > 1:
            write.writerows(data)
        else:
            write.writerow(data)