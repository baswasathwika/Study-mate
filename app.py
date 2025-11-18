from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model globally for all pages
tokenizer = AutoTokenizer.from_pretrained("ibm-granite/granite-3.3-2b-instruct")
model = AutoModelForCausalLM.from_pretrained("ibm-granite/granite-3.3-2b-instruct")

def chat_llm(user_prompt):
    messages = [
        {"role": "user", "content": user_prompt},
    ]
    inputs = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, tokenize=True,
        return_dict=True, return_tensors="pt",
    ).to(model.device)

    outputs = model.generate(**inputs, max_new_tokens=200)
    response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:])
    return response
