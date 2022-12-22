def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    data = data.split('\n')
    column = []
    for i in data:
        column.append(i.split(',')[0])

    return column
# Read the csv file
f = open('data.csv')
w = f.read()
print(get_first_column(w))