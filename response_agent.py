def generate_response(decision):
    return f"""
Final Result: {decision['label']}
Risk Score: {decision['score']}
"""