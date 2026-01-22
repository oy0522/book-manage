import pytest
from main import query_book

def test_query_existing_book(monkeypatch):
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write("9787020168890,A Dream of Red Mansions,Cao Xueqin\n")
    monkeypatch.setattr('builtins.input', lambda _: "9787020168890")
    query_book()

def test_query_non_existing_book(monkeypatch):
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write("9787020168890,A Dream of Red Mansions,Cao Xueqin\n")
    monkeypatch.setattr('builtins.input', lambda _: "123456")
    query_book()

if __name__ == "__main__":
    pytest.main(["-v"])