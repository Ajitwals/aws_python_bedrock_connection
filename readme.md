

````markdown
# AWS Bedrock Text Generator using Amazon Nova

This Python script connects to **Amazon Bedrock's Nova model** to generate high-quality AI responses based on user input. It demonstrates how to use the `converse` API to send text prompts and receive AI-generated text responses.

 🚀 Features

- Uses **Amazon Bedrock** via the `boto3` SDK.
- Connects to the **`amazon.nova-lite-v1:0`** model.
- Supports custom prompt input.
- Handles errors gracefully with appropriate messaging.



 📦 Requirements

- Python 3.7+
- AWS credentials with access to **Amazon Bedrock**
- AWS region enabled for Bedrock (e.g., `us-east-1`)
- The following Python packages:
  - `boto3`
  - `botocore`

Install them via:

```bash
pip install boto3
````



 🔐 AWS Configuration

Make sure your AWS credentials are configured using one of the following methods:

1. **Environment Variables**:

   ```bash
   export AWS_ACCESS_KEY_ID="your-access-key-id"
   export AWS_SECRET_ACCESS_KEY="your-secret-access-key"
   export AWS_DEFAULT_REGION="us-east-1"
   ```

2. **AWS CLI Config**:

   ```bash
   aws configure
   ```

3. **IAM Role (if using from an EC2 or Lambda)**.

> Ensure your user/role has access to Bedrock via IAM policy.



 🧠 Supported Model

The current script uses:

```
Model ID: amazon.nova-lite-v1:0
```

You can switch to other Bedrock models like:

* `amazon.titan-text-express-v1`
* `anthropic.claude-3-sonnet-20240229-v1:0`

Just update the `model_id` variable in the script.



 🛠️ How to Use

# 1. Clone the repo or save the script:

```bash
git clone https://github.com/yourusername/bedrock-text-generator.git
cd bedrock-text-generator
```

# 2. Run the script:

```bash
python generate_text.py
```

# 3. Enter a prompt:

You’ll be prompted to type your message. For example:

```
Enter your prompt: Write a haiku about the ocean.
```

# Output:

```
Amazon Nova Text Response:
Waves whisper secrets  
Moonlit tides embrace the shore  
Oceans breathe in peace
```



 🧩 File Structure

```
bedrock-text-generator/
│
├── generate_text.py       # Main script
└── README.md              # You're here!
```



 🛡️ Error Handling

If the script fails due to incorrect credentials or service errors, it prints:

```
ERROR: Can't invoke 'amazon.nova-lite-v1:0'. Reason: <error>
```



 📜 License

MIT License



 🤝 Author

Built by [Ajit Walvekar](https://github.com/yourusername)



 📬 Feedback

For questions, issues, or contributions, please open an issue or PR on the repository.

