import time
import pyexcel
import os
import pytest
from src.netmeter import excel

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

@pytest.fixture
def empty_book():
    # First row: ['', 'Monday', ..., 'Sunday']
    header_row = [""] + DAYS
    # First column: '00h', '01h', ..., '23h'
    sheet = [header_row]
    for h in range(24):
        row = [f"{h:02d}h"] + [None]*7
        sheet.append(row)
    return {"Default": sheet}

def test_itworks_writes_1(empty_book):
    book = empty_book.copy()
    day, _, hour = time.strftime("%A,%W,%H", time.localtime()).split(",")
    day_idx = DAYS.index(day) + 1  # +1 for header row
    hour_idx = int(hour) + 1       # +1 for header column
    excel.itworks(book)
    saved = pyexcel.get_book_dict(file_name="update.xlsx")
    assert saved["Default"][hour_idx][day_idx] == 1

def test_dontwork_writes_0(empty_book):
    book = empty_book.copy()
    day, _, hour = time.strftime("%A,%W,%H", time.localtime()).split(",")
    day_idx = DAYS.index(day) + 1
    hour_idx = int(hour) + 1
    excel.dontwork(book)
    saved = pyexcel.get_book_dict(file_name="update.xlsx")
    assert saved["Default"][hour_idx][day_idx] == 0

def teardown_module(module):
    if os.path.exists("update.xlsx"):
        os.remove("update.xlsx")


