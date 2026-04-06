import json

def generate_model(input_data):
    context = input_data.get("context", {})
    
    if context.get("location") == "home" and context.get("time") == "night":
        return {"action": "turn_on_lights"}
    
    return {"action": "none"}

if __name__ == "__main__":
    with open("../examples/smart_home_case/input_model.json") as f:
        data = json.load(f)
    
    result = generate_model(data)
    print("Generated:", result)
