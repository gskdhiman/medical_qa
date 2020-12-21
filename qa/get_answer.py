
# reference: https://huggingface.co/clagator/biobert_squad2_cased

from transformers import BertForQuestionAnswering
import torch
import time
import tokenizers
import os
BERT_PATH = "model"
# print(f"Bert path: {BERT_PATH}")
model = BertForQuestionAnswering.from_pretrained(f'{BERT_PATH}/')
tokenizer = tokenizers.BertWordPieceTokenizer(
      f"{BERT_PATH}/vocab.txt",
      lowercase=True
  )


def get_answer(question, context):
    tok_text = tokenizer.encode(question, context)
    tokens = tok_text.tokens
    start_positions = torch.tensor([0])
    end_positions = torch.tensor([1])

    input_ids = tok_text.ids
    token_type_ids = tok_text.type_ids

    mask = [1] * len(token_type_ids)
    max_len = 50
    padding_length = max_len - len(input_ids)
    if padding_length > 0:
        input_ids = input_ids + ([0] * padding_length)
        mask = mask + ([0] * padding_length)
        token_type_ids = token_type_ids + ([0] * padding_length)

    inputs = {
            'input_ids': torch.tensor([input_ids], dtype=torch.long),
            'token_type_ids': torch.tensor([token_type_ids], dtype=torch.long),
        }

    outputs = model(**inputs, start_positions=start_positions, end_positions=end_positions)
    loss = outputs[0]
    start_scores = outputs[1]
    end_scores = outputs[2]
    start_normalized = ((start_scores-torch.min(start_scores))/(torch.max(start_scores)-torch.min(start_scores)))
    end_normalized = ((end_scores - torch.min(end_scores)) / (torch.max(end_scores) - torch.min(end_scores)))

    start_numpy = list(start_normalized.detach().numpy().ravel().round(3))
    end_numpy = list(end_normalized.detach().numpy().ravel().round(3))

    e = torch.argmax(end_scores)
    s = torch.argmax(start_scores)

    print(f"end score: {e}")
    print(f"start score: {s}")
    answer = " ".join(tokens[s:e+1])
    answer = answer.replace(" ##", '')
    print(f"""answer: {answer}""")
    if answer == "[CLS]":
        answer = "No Answer Found"
    confidence = {'token': tokens, 'start': start_numpy[:len(tokens)], 'end': end_numpy[:len(tokens)]}
    return answer, confidence


if __name__ == "__main__":

    question, context = "what symptoms does patient have?", \
                        "The doctor advised the patient to have medicnes sinces he was having colding"
    import os
    get_answer(question, context)