def suggest_distribution(problem):
    problem = problem.lower()
    if any(word in problem for word in ["count", "event", "rate"]):
        return "Poisson"
    elif any(word in problem for word in ["yes/no", "success", "fail", "proportion"]):
        return "Binomial"
    elif any(word in problem for word in ["average", "normal", "bell"]):
        return "Normal"
    elif "time" in problem and "until" in problem:
        return "Exponential"
    elif "between 0 and 1" in problem or "probability" in problem:
        return "Beta"
    return "Normal"
