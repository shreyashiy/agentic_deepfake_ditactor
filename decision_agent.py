def make_decision(results):
    total = 0
    for r in results:
        total += r["risk"]

    final_score = total / len(results)

    if final_score > 0.5:
        label = "DEEPFAKE"
    else:
        label = "AUTHENTIC"

    return {"label": label, "score": round(final_score, 2)}