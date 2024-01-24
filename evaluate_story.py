import argparse
import json
from openai import OpenAI

client = OpenAI(
    api_key='your-api-key',
)

def evaluate_story(story, words, word_count, scale, level):
    prompt = (
        f"Systematically evaluate the following story for English language proficiency at each level from 1 to 5, "
        f"using these strict criteria:\n"
        f"- Level 1: Basic comprehension; simple sentences; basic vocabulary. Focus on simple grammar and clarity.\n"
        f"- Level 2: Improved sentence structure; some variety in vocabulary. Consider basic storytelling elements.\n"
        f"- Level 3: Clear structure; good grammar; varied vocabulary. Evaluate coherence and the use of descriptive language.\n"
        f"- Level 4: Strong structure and grammar; diverse vocabulary. Assess narrative flow and complex language usage.\n"
        f"- Level 5: Advanced grammar; sophisticated vocabulary; complex sentences. Expect nuanced expression and advanced storytelling.\n"
        f"Provide a score on a scale of {scale} for each level, reflecting the specific criteria. Maintain strict consistency in scoring.\n\n"
        f"Story (approximately {word_count} words, containing words: {words}):\n{story}\n\n"
        f"After scoring, verify each score to ensure it aligns with the criteria for its respective level and fix if any discrepancy."
        f"Confirm that the scoring is consistent and accurate for each level."
    )

    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt},
            {"role": "user", "content": "Give the scores formatted as a JSON object."},
        ],
        model="gpt-3.5-turbo",
        temperature=0,
    )
    return response.choices[0].message.content.strip()


def main():
    parser = argparse.ArgumentParser(description="Evaluate a story for English proficiency using ChatGPT.")
    parser.add_argument("input_file", help="Path to the JSON input file")
    args = parser.parse_args()

    with open(args.input_file, "r") as json_file:
        data = json.load(json_file)

    story = data.get("story")
    words = data.get("words")
    word_count = data.get("word_count")
    scale = data.get("scale")
    proficiency_level = data.get("proficiency_level")

    evaluation = evaluate_story(story, words, word_count, scale, proficiency_level)
    print(evaluation)

if __name__ == "__main__":
    main()


