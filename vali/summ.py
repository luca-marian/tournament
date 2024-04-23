import openai

# Set up OpenAI API

# Define input text
input_text = "Industries in the Crop Production subsector grow crops mainly for food and fiber.  The subsector comprises establishments, such as farms, orchards, groves, greenhouses, and nurseries, primarily engaged in growing crops, plants, vines, or trees and their seeds."

# Create prompt with context for keyword extraction
prompt = f"Extract keywords from the following text:\n\"{input_text}\"\nKeywords:"

# Call OpenAI API to generate keywords
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=50  # Adjust as needed
)

# Extract keywords from response
generated_text = response.choices[0].text.strip()
keywords = generated_text.split(',')

print("Extracted Keywords:", keywords)