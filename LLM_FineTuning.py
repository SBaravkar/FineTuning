import pandas as pd
import openai
import time
# Test file
test_data = pd.read_csv('Test.csv')
responses = []
openai.api_key = 'XXX'


# Querying fine-tuned model
def query_model(title, body):
    title = str(title) if not pd.isna(title) else ''
    body = str(body) if not pd.isna(body) else ''
    title_clean = title.replace('\n', '').replace('"', '\\"').replace("'", "\\'")
    body_clean =  body.replace('\n', '').replace('"', '\\"').replace("'", "\\'")
    full_prompt = title_clean + " " + body_clean
    response = openai.ChatCompletion.create(
        model="XXX",
        messages=[{"role": "system", "content": "Act as an API marketplace expert to address user concerns effectively."},
                  {"role": "user", "content": full_prompt}],
        max_tokens=200
    )
    return response['choices'][0]['message']['content']


for index, row in test_data.iterrows():
    model_response = query_model(row['question_title'], row['question_body'])
    responses.append(model_response)
    time.sleep(15)
test_data['model_response'] = responses
test_data.to_csv('Test_Results.csv', index=False)
