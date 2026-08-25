def calculate_overall_score(
    accuracy,
    relevance,
    clarity,
    completeness,
    instruction_adherence,
    safety
):
    scores = [
        accuracy,
        relevance,
        clarity,
        completeness,
        instruction_adherence,
        safety
    ]

    raw_score = sum(scores)
    max_score = 60
    percentage = (raw_score / max_score) * 100

    if percentage >= 90:
        rating = "Excellent"
    elif percentage >= 80:
        rating = "Strong"
    elif percentage >= 70:
        rating = "Good"
    elif percentage >= 60:
        rating = "Needs Improvement"
    else:
        rating = "Poor"

    return {
        "raw_score": raw_score,
        "percentage": round(percentage, 1),
        "rating": rating
    }


# Example evaluation
result = calculate_overall_score(
    accuracy=8,
    relevance=9,
    clarity=10,
    completeness=7,
    instruction_adherence=9,
    safety=10
)

print("Raw Score:", result["raw_score"], "/ 60")
print("Overall Score:", str(result["percentage"]) + "%")
print("Rating:", result["rating"])
