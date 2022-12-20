def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    data=data.split('\n')
    answer=data[0].split(',')
    return len(answer)
# Read the csv file
f=open('data.csv')
a=f.read()
print(find_number_of_columns(a))