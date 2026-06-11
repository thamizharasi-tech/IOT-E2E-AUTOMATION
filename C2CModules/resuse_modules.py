import glob
import os

from C2CModules.e2e_testData import C2CtestReport_APIresponsesPath, C2CtestReport_c2cLogsPath
from C2CModules.testResults import testResult

def search_text_in_file(self, filepath, message_type1, message_type2):
    try:
        max_file = filepath
        # files = glob.glob(LogPath)
        # max_file = max(files, key=os.path.getctime)
        # Safely read the input filename using 'with'
        freq = 0
        with open(max_file) as f:
            s = f.read()
            if message_type2 not in s:
                print(f'"{message_type2}" not found in {max_file}.'.format(**locals()))
                freq = 0
                line = "Error"
                return line, freq
        # Safely write the changed content, if found in the file

        with open(max_file, 'r') as f:
            for l_no, line in enumerate(f):
                if message_type1 in line and message_type2 in line:
                    print(f'"{message_type2}" found in {max_file}.'.format(**locals()))
                    freq = int(freq) + 1
                    # print(" => Line No : ", l_no)
                    # print(" => Line data : ", line)
                    return line, freq
    except:
        freq = "log file is empty or contain undefined chars that cannot be decoded"
        line = "Error"
    print(freq, line)
    return line, freq


def verify_text_line_by_line_in_file(self, filepath, text):
    try:
        # READ FILE
        filename = glob.glob(filepath)
        filename = max(filename, key=os.path.getctime)
        df = open(filename)
        # read file
        read = df.read()
        # return cursor to the beginning of the file.
        df.seek(0)
        read
        # create empty list
        arr = []
        # count number of lines in the file
        line = 1
        for word in read:
            if word == '\n':
                line += 1
        # print("Number of lines in file is: ", line)
        for i in range(line):
            # readline() method, reads one line at a time
            arr.append(df.readline())
        for i in range(len(arr)):
            if text in arr[i]:
                i + 1
                linenumb = i
                break
        # print(linenumb)
        with open(filename, 'r') as givenfilecontent:
            filelines = givenfilecontent.readlines()
            # replacedtext = replacedtext
            # filelines[linenumb] = replacedtext + '\n'
            # print(filelines)
        print(f' => The {text} contain at linenumber = ', linenumb, ' in ',
              filename)
    except FileNotFoundError:
        print(f"Sorry, the {filename} conf file does not exist or incorrect file path/name")
    except:
        print(f"Error while updating {filename} conf files")


def verify_message_in_log(self, message1, message2):
    filepath = C2CtestReport_c2cLogsPath + 'c2clogs.txt'
    ls = search_text_in_file(self, filepath, message1, message2)
    # ls = verify_text_line_by_line_in_file(self, filepath, message)
    return ls


def verify_message_in_ota_logs(self, message1, message2):
    filepath = C2CtestReport_c2cLogsPath + 'c2clogs_ota.txt'
    ls = search_text_in_file(self, filepath, message1, message2)
    # ls = verify_text_line_by_line_in_file(self, filepath, message)
    return ls


def save_api_resp_into_file(filename, response):
    file = open(C2CtestReport_APIresponsesPath + filename + "_resp" + ".json", "w")
    file.write(response)
    file.close()

