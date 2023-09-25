import sys
import time
import json
import requests
from prompts import calculator
from prompts import *

api_url = 'http://192.168.101.100:8080'

def post(prompt, temperature=0.6, top_k=1000, top_p=0.9, n_keep=0, n_predict=1024, stop=["[INST]"], stream=False):
    headers = {'Content-Type': 'application/json'}
    payload = {
        'prompt': prompt,
        'temperature': temperature,
        'top_k': top_k,
        'top_p': top_p,
        'n_keep': n_keep,
        'n_predict': n_predict,
        'stop': stop,
        'stream': stream}
    resp = requests.post(f'{api_url}/completion', headers=headers, data=json.dumps(payload))
    return json.loads(resp.content)

def prompt(sys_msg)-> str:
    text = "<s>" + B_INST + B_SYS + sys_msg + E_SYS
    text += " Respond to the following in JSON with 'action' and 'action_input' values " + E_INST
    text += "\nUser: {input}"
    return text

def json_filter(content)-> str:
    l = content.find('{')
    r = content.rfind('}')
    try:
        return json.loads(content[l:r+1])
    except json.decoder.JSONDecodeError:
        print("JSONDecodeError...")
        return None

def demo01(prompts):
    prompt_template = prompt(calculator.SYSTEM_MESSAGE)
    p = prompts.pop()
    while True:
        if len(prompts) == 0:
            break
        resp = post(prompt_template.format(input=p))
        res = json_filter(resp['content'])
        if res is None:
            time.sleep(1)
            continue
        else:
            print(res)
            p = prompts.pop()

        time.sleep(1)


if __name__ == '__main__':
    prompts = [
        "Write a poem about love",
        "what's 1+1=2 ?",
        "What about black hole?",
        "How about landing the Mars?",
        "how are you today?",
    ]
    demo01(prompts)
