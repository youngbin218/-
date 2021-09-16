import pandas as pd

filename = "ex.xlsx"
sheet_name = "stats_104102"
book = pd.read_excel(filename, sheet_name = sheet_name, header = 1, engine = 'openpyxl')

book = book.sort_values(by = 2018, ascending = False)
print(book)
