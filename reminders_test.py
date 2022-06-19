import pytest  
import reminders
import fakeredis, json
r = fakeredis.FakeStrictRedis(decode_responses=True)

# Test for basic requirements of prompt, function to add and function to get
# If I weren't concerned about time, I would have test driven this by writing these first
def test_get_empty():
    response = reminders.get_all(r)
    assert response == []

def test_add():
    response = reminders.add_to_redis(r, '{"time": "07:30", "message": "hello world"}')
    assert response == 0
    for key in r.scan_iter():
      assert r.get(key)=='{"time": "07:30", "message": "hello world"}'

def test_get_with_data():
    response = reminders.get_all(r)
    for item in response:
        assert json.dumps(item) == '{"time": "07:30", "message": "hello world"}'