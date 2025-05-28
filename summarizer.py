import argparse
import requests

def summarize_with_api(text, model_name="facebook/bart-large-cnn", max_length=150):
    API_URL = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {"Authorization": "Bearer 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"}
    
    payload = {"inputs": text, "parameters": {"max_length": max_length}}
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()[0]["summary_text"]
    else:
        raise Exception(f"API Error: {response.text}")

def main():
    parser = argparse.ArgumentParser(description="Text Summarization")
    parser.add_argument("--text", type=str)
    parser.add_argument("--file", type=str)
    parser.add_argument("--model", default="facebook/bart-large-cnn")
    parser.add_argument("--max_length", type=int, default=150)
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r") as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        print("Error: Provide --text or --file")
        return

    print(f"Using model: {args.model}")
    summary = summarize_with_api(text, args.model, args.max_length)
    print("\nSummary:")
    print(summary)

if __name__ == "__main__":
    main()
