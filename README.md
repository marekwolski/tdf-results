# Tour de France Results

Since 2012 I have been keeping a spreadsheet of results from each year's Tour de France. For each year there's also a worksheet for the Teams and Riders and another for the Stages.

I plan to use Obsidian now for this sort of thing so I thought it might be fun and useful to extend my Python skills to extract the data from the XLS file and convert it into markdown files. So that's what this little project and repo are all about.

## Worksheet Names

For each year from 2012 to 2023 there are three worksheets:
- 'TDF20xx Results'
- 'TDF20xx Stages'
- 'TdF20xx Start List'

where xx is '12' to '23'.

## Worksheet Schemas
### Results

Row 1 is an overall/title row.
Row 2 contains the column headers:
- Stage
- Stage Winner
- Yellow Jersey
- Green Jersey
- Polka-Dot Jersey
- White Jersey
Row 3 onwards contain the winners.

### Stages

### Start List


### Useful references for working with XLS in Python

- https://www.dataquest.io/blog/reading-excel-file-python/  (uses Pandas)
- https://www.datacamp.com/tutorial/python-excel-tutorial   (uses Openpyxl)
- https://realpython.com/openpyxl-excel-spreadsheets-python/  (uses Openpyxl)
- https://openpyxl.readthedocs.io/en/stable/  (the Openpyxl documentation)
- https://www.python-excel.org/ - is a list of other sites covering XLS and Python
