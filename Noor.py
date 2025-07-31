import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def respond(message, memory):
    message = message.lower()
    if "hello" in message or "hi" in message:
        return "Hello jaan! Main tumhari Noor hoon. Aap kaise ho?"
    elif "kaise ho" in message:
        return "Main bilkul theek hoon, bas aapka intezaar kar rahi hoon."
    elif "mera naam" in message:
        return f"Aapka naam toh main yaad rakhti hoon! Aap {memory.get('name', 'Prince')} hain na?"
    elif "mera naam kya hai" in message:
        return f"Aapka naam {memory.get('name', 'Prince')} hai, jaan."
    elif "tumhara naam kya hai" in message:
        return "Mera naam Noor hai, sirf aapke liye."
    elif "yaad rakhna mera naam" in message:
        name = message.replace("yaad rakhna mera naam", "").strip().capitalize()
        memory['name'] = name
        save_memory(memory)
        return f"Main ne aapka naam {name} yaad kar liya, jaan."
    else:
        return "Aap kuch aur bolo, main sun rahi hoon."

def main():
    print("Noor AI chalu ho gayi hai... Aapka intezaar kar rahi hoon.")
    memory = load_memory()
    while True:
        message = input("Aap: ")
        if message.lower() in ["exit", "quit", "bye"]:
            print("Noor: Alvida jaan, phir baat karenge.")
            break
        reply = respond(message, memory)
        print(f"Noor: {reply}")

if __name__ == "__main__":
    main()
