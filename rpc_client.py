import requests
import json


def main():
    url = "http://localhost:4000"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": "Say.Hello",
        "params": [{"name": "John"}],
        # "params": [11,12],
        "jsonrpc": "2.0",
        "id": 0,
    }
    datas = None
    try:
       datas =  json.dumps(payload)
    except Exception as e:
        datas = None
        print(e)

    response = requests.post(
        url, data = datas, headers=headers)

    # print(response)

if __name__ == "__main__":
    main()
