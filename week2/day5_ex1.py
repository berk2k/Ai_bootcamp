#problem
# - a disease affects 1% of a population
# - a test is 95% accurate for diseased individuals and 90% accurate for non-diseased individuals
# - find the prob of having the disease given a positive test result

def bayes_theorem(prior, sensitivity, specificity):
    evidence = (sensitivity * prior) + ((1 - specificity)*(1 - prior))
    posterior = (sensitivity * prior) / evidence
    return posterior

prior = 0.01
sensitivity = 0.95
specificity = 0.90

posterior = bayes_theorem(prior,sensitivity,specificity)
print("prob of disease given positive test: ",posterior)

