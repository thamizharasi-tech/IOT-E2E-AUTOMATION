import glob
import json
import os
import openpyxl

from C2CModules.e2e_testData import xlsx_apiTestData_file

list_status = []


# ===============================
# get row no based on test case name (first column value) from test data excel
# ===============================

def get_rowNo_from_excel(workbook, sheetname, name):
    #print(workbook, sheetname, name)
    files = glob.glob(workbook)
    #print(files)
    max_file = max(files, key=os.path.getctime)
    wb_obj = openpyxl.load_workbook(max_file)
    wsheet = wb_obj[sheetname]

    row_count = wsheet.max_row
    col_count = wsheet.max_column

    # print("No. of rows in excel sheet : ", row_count)
    # print("No. of columns in excel sheet : ", col_count)

    # get row no based on api name to read test data
    for col in wsheet.iter_cols(min_col=1, max_col=col_count, min_row=1, max_row=row_count):
        for cell in col:
            if cell.value == name:
                rowNo = int(cell.row)
    return wb_obj, wsheet, rowNo


class XlsxReader:

    @staticmethod
    def getRowCount(file, sheetName):
        workbook = openpyxl.load_workbook(file)
        #print(file, sheetName)
        sheet = workbook[sheetName]
        return (sheet.max_row)

    @staticmethod
    def getColumnCount(file, sheetName):
        workbook = openpyxl.load_workbook(file)
        sheet = workbook[sheetName]
        return (sheet.max_column)

    @staticmethod
    def readData(file, sheetName, rownum, columnno):
        workbook = openpyxl.load_workbook(file)
        sheet = workbook[sheetName]
        return sheet.cell(row=rownum, column=columnno).value

    @staticmethod
    def writeData(file, sheetName, rownum, columnno, data):
        workbook = openpyxl.load_workbook(file)
        sheet = workbook[sheetName]
        sheet.cell(row=rownum, column=columnno).value = data
        workbook.save(file)

    # ===============================
    # Read test data from excel file
    # ===============================

    @staticmethod
    def read_api_testData_from_excel(sheetname, apiName):
        wb_obj, wsheet, rowNo = get_rowNo_from_excel(sheetname, apiName)
        list_status.clear()
        for row in wsheet[rowNo]:
            list_status.append(row.value)
        # print("Selected row  values: ", list_status)
        resp1 = json.dumps({'testData': list_status})
        resp = json.loads(resp1)
        return resp

    # ===============================
    # Save response/results in excel file
    # ===============================

    @staticmethod
    def save_api_actual_resp_in_excel(sheetname, apiName, colNo, resp):
        wb_obj, wsheet, rowNo = get_rowNo_from_excel(sheetname, apiName)
        c1 = wsheet.cell(row=rowNo, column=colNo)
        c1.value = resp
        wb_obj.save(xlsx_apiTestData_file)

def read_api_data_from_excel(self, sheet_name, testcase_name):
    wb_obj, wsheet, rowNo = get_rowNo_from_excel(xlsx_apiTestData_file, sheet_name, testcase_name)
    dictionary = {}
    workbook = openpyxl.load_workbook(xlsx_apiTestData_file)
    #worksheet = workbook.active
    row_count = wsheet.max_row
    col_count = wsheet.max_column
    for col in wsheet.iter_cols(min_col=1, max_col=col_count, min_row=1, max_row=row_count):
        for cell in col:
            if cell.value == testcase_name:
                rowNo = int(cell.row)
                for i in range(1, row_count + 1):
                    print("\n")
                    for j in range(1, col_count + 1):
                        cell_obj = wsheet.cell(row=1, column=j)
                        cell_obj1 = wsheet.cell(row=rowNo, column=j)
                        dictionary[cell_obj.value] = cell_obj1.value
    #print(dictionary)
    return dictionary

def save_api_resp_in_excel(self, sheet_name, testcase_name, data):
    wb_obj, wsheet, rowNo = get_rowNo_from_excel(xlsx_apiTestData_file, sheet_name, testcase_name)
    dictionary = {}
    workbook = openpyxl.load_workbook(xlsx_apiTestData_file)
    worksheet = workbook.active
    row_count = wsheet.max_row
    col_count = wsheet.max_column
    sheet = workbook[sheet_name]
    for col in wsheet.iter_cols(min_col=1, max_col=col_count, min_row=1, max_row=row_count):
        for cell in col:
            if cell.value == testcase_name:
                rowNo = int(cell.row)

    sheet.cell(row=rowNo, column=8).value = data
    workbook.save(xlsx_apiTestData_file)

def save_api_header_in_excel(self, sheet_name, testcase_name, data):
    wb_obj, wsheet, rowNo = get_rowNo_from_excel(xlsx_apiTestData_file, sheet_name, testcase_name)
    dictionary = {}
    workbook = openpyxl.load_workbook(xlsx_apiTestData_file)
    worksheet = workbook.active
    row_count = wsheet.max_row
    col_count = wsheet.max_column
    sheet = workbook[sheet_name]
    for col in wsheet.iter_cols(min_col=1, max_col=col_count, min_row=1, max_row=row_count):
        for cell in col:
            if cell.value == testcase_name:
                rowNo = int(cell.row)

    sheet.cell(row=rowNo, column=5).value = data
    workbook.save(xlsx_apiTestData_file)


def save_data_in_excel(self, sheet_name, testcase_name, columnNo, data):
    wb_obj, wsheet, rowNo = get_rowNo_from_excel(xlsx_apiTestData_file, sheet_name, testcase_name)
    dictionary = {}
    workbook = openpyxl.load_workbook(xlsx_apiTestData_file)
    worksheet = workbook.active
    row_count = wsheet.max_row
    col_count = wsheet.max_column
    sheet = workbook[sheet_name]
    for col in wsheet.iter_cols(min_col=1, max_col=col_count, min_row=1, max_row=row_count):
        for cell in col:
            if cell.value == testcase_name:
                rowNo = int(cell.row)

    sheet.cell(row=rowNo, column=int(columnNo)).value = data
    workbook.save(xlsx_apiTestData_file)