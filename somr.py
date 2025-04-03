import openai
from back import calculate_tax

# Initialize OpenAI API (should be set in environment variables)
openai.api_key = os.getenv("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")

def get_tax_tip(text):
    """Analyze receipt text and provide tax advice."""
    try:
        prompt = f"""
        Analyze this receipt and provide tax advice:
        {text}
        
        Include:
        1. Deductible items
        2. Potential tax savings
        3. IRS code references
        Return the response in a clear, concise format.
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating tax tip: {str(e)}"