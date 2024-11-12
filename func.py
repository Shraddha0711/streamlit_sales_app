import requests

url = 'https://pipecat-default-example-wispy-cloud-99.fly.dev/'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}



def start_bot(prompt:str, voice_id:str):
    data = {
        "speed": "normal",
        "emotion": [
            "positivity:high",
            "curiosity"
        ],
        "prompt": prompt,
        "voice_id": voice_id,
        "session_time": 3600
    }

    response = requests.post(url, headers=headers, json=data)

    # Print response status and content
    print("Status Code:", response.status_code)
    print("Response:", response.json())

    return response.json()


if __name__=="__main__":
    start_bot(prompt="you are a friendly assistant")
