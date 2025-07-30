import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID. For text-only, you can still use Nova or
# other text-generation models like Titan Text Express v1 or Claude 3.
# Let's stick with a Nova model for consistency if you prefer it.
# You could also use "amazon.titan-text-express-v1" or
# "anthropic.claude-3-sonnet-20240229-v1:0" etc.
model_id = "amazon.nova-lite-v1:0"

def generate_text_with_nova(prompt: str) -> str:
    # Start a conversation with a user message containing only text
    conversation = [
        {
            "role": "user",
            "content": [
                {"text": prompt}, # Only include the text content block
            ],
        }
    ]

    try:
        # Send the message to the model, using a basic inference configuration.
        response = client.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens": 500, "temperature": 0.3},
        )

        # Extract and print the response text.
        # The structure remains the same for text-only responses from converse API.
        response_text = response["output"]["message"]["content"][0]["text"]
        return response_text

    except (ClientError, Exception) as e:
        error_message = f"ERROR: Can't invoke '{model_id}'. Reason: {e}"
        print(error_message)
        return error_message # Return error message instead of exiting for a function

# Run it
if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    output = generate_text_with_nova(user_input)
    print("\nAmazon Nova Text Response:\n", output)