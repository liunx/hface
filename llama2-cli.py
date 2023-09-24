import sys
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
    

if __name__ == '__main__':
    sys_msg = "<s>" + B_SYS + calculator.SYSTEM_MESSAGE + E_SYS
    instruction = B_INST + " Respond to the following in JSON with 'action' and 'action_input' values " + E_INST
    human_msg = instruction + "\nUser: {input}"
    resp = post(sys_msg + human_msg.format(input=f'{sys.argv[1]}'))
    print(resp['content'])
