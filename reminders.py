import redis, json, uuid

# Depending on the way redis handles multiple connections, this might be okay the way it is.  However, with another DB (RDBMS or NoSQL),
#  we would want to leverage a singleton pattern to avoid spamming the DB with connections when we leverage multiple threads / containers / pods
def get_connection():
    r = redis.Redis(host='redis', port=6379, decode_responses=True)
    return r

def add_to_redis(r, data):
    try:
      id = str(uuid.uuid1())
      r.mset({id: data})
    except:
      return 1 # Silly error coding, but demonstrating that we should throw errors with explanation / coding back up to the application
    return 0

def get_all(r):
    retList = []
    for key in r.scan_iter():
      retList.append(json.loads(r.get(key)))
    return retList