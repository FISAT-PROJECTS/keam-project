# import tabula

# tabula.convert_into("/home/amanks/Downloads/10_l.pdf", "output.csv", output_format="csv", pages='all')

# import pandas as pd

# df = pd.read_csv("output.csv", error_bad_lines=False)

# df.head(10)

import camelot

tables = camelot.read_pdf("/home/amanks/Downloads/10_l.pdf", pages='all')

# print(tables)
tables.export('foo.csv', f='csv', compress=True)
# print(tables[1].df)