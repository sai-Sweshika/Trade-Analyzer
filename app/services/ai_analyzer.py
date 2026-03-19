def analyze_data(sector: str, data: str):
    try:
        from google import genai
        import os

        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        response = client.models.generate_content(
            model="gemini-1.5-flash-latest",
            contents=f"Analyze {sector} sector in India:\n{data}"
        )

        return response.text

    except Exception as e:
        print("Gemini failed:", e)

        return f"""
## Overview
The {sector} sector in India is growing steadily.

## Current Trends
- Increasing investments
- Government support
- Rising demand

## Trade Opportunities
- Export opportunities
- Expansion into new markets

## Risks
- Regulatory challenges
- Market competition

## Conclusion
The {sector} sector has strong growth potential.

---
⚠️ AI service unavailable, fallback used.
"""