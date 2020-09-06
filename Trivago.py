import os
import csv
import copy
import datetime
import string
import re



class clense:

    def __init__(self):
        self.path = 'C:/Users/Anoop.paul/Downloads/trivago/'

    def clense_fn(self):
        files = os.listdir(self.path)
        for f in files:
            print(f)
            error_msg = self.filename_check(f)
            if error_msg:
                print(error_msg)
                continue

            empty_file = os.stat(self.path + f).st_size == 0
            if empty_file:
                error_msg = "file size is empty"
                print(error_msg)
                continue

            error_msg = self.read_csv(f)
            if error_msg:
                print(error_msg)
                continue

            print("file got no issues")



    def read_csv(self, filename):
        error_msg = ""
        with open(self.path + filename) as csv_file:
            error_msg = self.check_delimiter_header(csv_file)
            if error_msg:
                print(error_msg)
            csv_file.seek(0)
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                error_msg = self.check_comma(row)
                if error_msg:
                    print(row)
                    return error_msg

                # remove_characters = [",", "_"]
                # for char in remove_characters:
                #     special_chars = set(string.punctuation.replace(char, ""))
                #
                # bool = False
                # for each in row[1]:
                #     if each in special_chars:
                #         bool = True
                #         break
                # if bool:
                #     error_msg = "contains invalid characters"
                # return error_msg

                special_char = False
                regexp = re.compile(r"[^!@_ a-zA-Z0-9-]")      #'/^(?=.*[a-z0-9])[a-z0-9!@#$%&*.]{7,}$')
                if regexp.search(row[1]):
                    print(row[1])
                    special_char = True
                    error_msg = "contains special characters"
                    return error_msg




    def check_delimiter_header(self, file):
        error_msg = ""
        try:
            dialect = csv.Sniffer().sniff(file.read(1024*16), delimiters = ",")
        except Exception as T:
            print(T)
            error_msg = "Wrong Delimiter"
            return error_msg
        file.seek(0)
        try:
            has_headers = csv.Sniffer().has_header(file.read(1024))
        except Exception as T:
            print(T)
            has_headers = True
        if not has_headers:
            error_msg = "Wrong Header"
        return error_msg




    def filename_check(self, filename):
        error_msg = ""
        parts = filename.split('.')
        if parts[1] == 'csv':
            parts = filename.split('_')
            if len(parts) == 4:
                parts1 = parts[3].split('.')[0]
                try:
                    datetime.datetime.strptime(parts1, '%Y%m%d')
                except ValueError:
                    error_msg = "Incorrect filename: data format, should be YYYYMMDD"
            else:
                error_msg = "Incorrect filename: check filename"
        else:
            error_msg = "Not a csv file"
        return error_msg




    def check_comma(self, row):
        error_msg = ""
        if len(row)>=3:
            error_msg = "Incorrect csv: unexpected column count"
        return error_msg



obj = clense()
obj.clense_fn()
