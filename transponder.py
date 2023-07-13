def convert_columns_to_rows(self):
  """Converts the data in the spreadsheet from columns to rows.
  This method takes the data in the spreadsheet and converts it so that
  each row is a list of values, where the index of the value in the list
  corresponds to the column that the value is in.
  Returns:
    A list of lists, where each inner list is a row of values.
  """
  rows = []
  for column in self.columns:
    row = []
    for value in column:
      row.append(value)
    rows.append(row)
  return rows
def convert_rows_to_columns(self):
  """Converts the data in the spreadsheet from rows to columns.
  This method takes the data in the spreadsheet and converts it so that
  each column is a list of values, where the index of the value in the list
  corresponds to the row that the value is in.
  Returns:
    A list of lists, where each inner list is a column of values.
  """
  columns = []
  for row in self.rows:
    column = []
    for value in row:
      column.append(value)
    columns.append(column)
  return columns
