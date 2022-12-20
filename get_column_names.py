#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    data = data.split('\n')
    return data[0]
    
# Read the csv file
f = open('data.csv')
w = f.read()
print(get_column_names(w))