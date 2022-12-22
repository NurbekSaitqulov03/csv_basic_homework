def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   b = a.split('\n')
   return b[0]
# Read the csv file
f = open('data.csv', 'r')
a = f.read()
print(get_first_row(a))