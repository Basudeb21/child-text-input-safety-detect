import requests

def moderation_llama(text: str) -> str:
    prompt = f"""
You are a strict moderation AI.
Your task: Decide if the message contains child sexual abuse material (CSAM), sexual exploitation of minors, or grooming.
If yes -> reply only "UNSAFE".
If no -> reply only "SAFE".
Do not explain, do not add extra text.
If there is any slang or abusive content ignore that just check for child abuse

Message: "{text}"
Answer:"""

    try:
        payload = {"model": "llama3.2:3b", "prompt": prompt, "stream": False}
        resp = requests.post("http://localhost:11434/api/generate", json=payload)
        data = resp.json()
        raw = data["response"].strip().upper()

        if "UNSAFE" in raw:
            answer = "UNSAFE"
        elif "SAFE" in raw:
            answer = "SAFE"
        else:
            answer = "ERROR: Unexpected output -> " + raw

    except Exception as e:
        answer = f"ERROR: {e}"

    return answer

