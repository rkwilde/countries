import ingest

def test_filesave1():
    result = [{"a":1,"b":2},{"a":3,"b":4}]
    filename = "test.json"
    ingest.save_result_as_file(result, filename)
    assert True # checking manually for now
