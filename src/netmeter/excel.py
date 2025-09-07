import time
import pyexcel
import os

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_day_index(day_name):
    return DAYS.index(day_name)

def load_or_create_book(path):
    if os.path.exists(path):
        book = pyexcel.get_book_dict(file_name=path)
        sheet = book.get("Default")
        # If sheet is missing or malformed, recreate
        if not sheet or len(sheet) != 25 or len(sheet[0]) != 8:
            sheet = None
    else:
        sheet = None
    if not sheet:
        header_row = [""] + DAYS
        sheet = [header_row]
        for h in range(24):
            sheet.append([f"{h:02d}h"] + [None]*7)
    return {"Default": sheet}

def testConn():
    # Dummy implementation, replace with actual connectivity test
    # Return True if service is up, False otherwise
    return True

def updateBook(path):
    res = testConn()
    day, week, hour = time.strftime("%A,%W,%H", time.localtime()).split(",")
    day_idx = get_day_index(day) + 1  # +1 for header
    hour_idx = int(hour) + 1          # +1 for header
    book = load_or_create_book(path)
    sheet = book["Default"]
    value = 1 if res else 0
    sheet[hour_idx][day_idx] = value
    book["Default"] = sheet
    pyexcel.save_book_as(bookdict=book, dest_file_name=path)
    print("service assuré" if res else "service non assuré")
    return book