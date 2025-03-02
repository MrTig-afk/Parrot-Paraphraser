# -*- coding: utf-8 -*-
"""NLP_Certification

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Krcs8I-SKtsbFMjPQL3d_EMcSKEmQbt2
"""

!pip install git+https://github.com/PrithivirajDamodaran/Parrot_Paraphraser.git
from parrot import Parrot
import torch
import warnings
warnings.filterwarnings("ignore")
parrot=Parrot(model_tag="Prithivida/parrot_paraphraser_on_T5",use_gpu=False)

def print_paraphrase_sentences(phrases):
  for phrase in phrases:
      print("-"*100)
      print("Input_phrase: ", phrase)
      print("-"*100)
      para_phrases = parrot.augment(input_phrase=phrase, use_gpu=False)
      print(para_phrases)
      for para_phrase in para_phrases:
        print(para_phrase)

phrases= ["What are the famous places we should not miss in Russia?","Can you recommend some upscale restaurants in Newyork?"]
print_paraphrase_sentences(phrases)

def custom_paraphrase_sentences(phrase, phrase_diversity=False):
    print("-" * 100)
    print("Input_phrase: ", phrase)
    print("-" * 100)
    para_phrases = parrot.augment(input_phrase=phrase, use_gpu=False,
                                  diversity_ranker="levenshtein",
                                  max_return_phrases=15,
                                  do_diverse=False,
                                  max_length=40,
                                  adequacy_threshold=0.85,
                                  fluency_threshold=0.88)
    for para_phrase in para_phrases:
        print(para_phrase)

diversity_phrases=["Which is better for the lats? Pull-ups or Lat Pull down?"]

custom_paraphrase_sentences(diversity_phrases[0])

phrase_diversity= True
custom_paraphrase_sentence(diversity_phrases[0],phrase_diversity)

while True:
  user_q = input("Enter a phrase (To quit enter 'exit'): ")
  if user_q == "exit":
    break
  else:
    phrase_d = input("Do you want phrasal diversity? (y or n): ")
    if phrase_d and phrase_d.lower() == "y":
      custom_paraphrase_sentences(user_q, phrase_diversity=True)
    else:
        custom_paraphrase_sentences(user_q)