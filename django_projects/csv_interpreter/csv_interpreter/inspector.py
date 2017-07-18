from goodtables import Inspector
import csv


class CSVInspector():

    def inspection(self, csv):
        CSV = csv
        inspector = Inspector(row_limit=1000000, error_limit=1000000, checks="MOCK_DATA.json")
        inspector_string = (inspector.inspect(CSV))
