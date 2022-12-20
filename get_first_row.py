def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   a = data.split('\n')
   return a[1]

# Read the csv file
f = open('data.csv')
w = f.read()
print(get_first_row(w))