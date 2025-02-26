#!/usr/bin/env python
# coding: utf-8

# In[11]:


import math
from collections import defaultdict

# Function to calculate probabilities with Laplace smoothing
def calculate_probabilities(training_data, sense_counts, V):
   word_counts = defaultdict(lambda: defaultdict(int))  # word_counts[sense][word] = count
   for sentence, sense in training_data:
       words = sentence.split()
       for word in words:
           word_counts[sense][word] += 1

   probabilities = defaultdict(dict)  # probabilities[sense][word] = P(word|sense)
   for sense in sense_counts:
       total_words_in_sense = sum(word_counts[sense].values())
       for word in word_counts[sense]:
           probabilities[sense][word] = (word_counts[sense][word] + 1) / (total_words_in_sense + V)
       # Handle unseen words
       probabilities[sense]["UNSEEN"] = 1 / (total_words_in_sense + V)

   return probabilities

# Function to calculate the score for a given sense
def calculate_score(sense, context, probabilities, prior):
   score = math.log(prior[sense])  # log(P(sense))
   for word in context:
       if word in probabilities[sense]:
           score += math.log(probabilities[sense][word])  # log(P(word|sense))
       else:
           score += math.log(probabilities[sense]["UNSEEN"])  # log(P(UNSEEN|sense))
   return score

# Main function
def main():
   # Input training data
   training_data = []
   sense_counts = defaultdict(int)
   print("Enter training data (sentence and sense, separated by a comma). Type 'done' to finish:")
   while True:
       user_input = input().strip()
       if user_input.lower() == "done":
           break
       sentence, sense = user_input.split(",")
       training_data.append((sentence.strip(), sense.strip()))
       sense_counts[sense.strip()] += 1

   # Input testing data
   print("\nEnter testing data (sentence). Type 'done' to finish:")
   testing_data = []
   while True:
       user_input = input().strip()
       if user_input.lower() == "done":
           break
       testing_data.append(user_input)

   # Vocabulary size (V)
   V = len(set(word for sentence, _ in training_data for word in sentence.split()))

   # Calculate priors
   total_sentences = len(training_data)
   priors = {sense: count / total_sentences for sense, count in sense_counts.items()}

   # Calculate probabilities
   probabilities = calculate_probabilities(training_data, sense_counts, V)

   # Predict senses for testing data
   print("\nPredictions:")
   for sentence in testing_data:
       context = sentence.split()
       scores = {}
       print(f"\nSentence: '{sentence}'")
       for sense in sense_counts:
           scores[sense] = calculate_score(sense, context, probabilities, priors)
           # Print probabilities for each word in the context
           print(f"\nProbabilities for sense '{sense}':")
           for word in context:
               if word in probabilities[sense]:
                   print(f"P({word}|{sense}) = {probabilities[sense][word]:.4f}")
               else:
                   print(f"P({word}|{sense}) = UNSEEN -> {probabilities[sense]['UNSEEN']:.4f}")
           print(f"Prior P({sense}) = {priors[sense]:.4f}")
           print(f"Score for sense '{sense}': {scores[sense]:.4f}")
       predicted_sense = max(scores, key=scores.get)
       print(f"\nPredicted Sense: '{predicted_sense}'")

# Run the program
if __name__ == "__main__":
   main()


# In[ ]:




