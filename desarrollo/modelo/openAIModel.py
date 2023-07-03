import os
import openai
from pydantic import BaseModel

#org-FlF7DjfN8kf6smfJafiv4p82
#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
openai.organization='org-FlF7DjfN8kf6smfJafiv4p82'
openai.api_key = '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'

class Document(BaseModel):
  prompt: str=''

def inference(prompt: str) -> list:
  openai.organization = 'org-FlF7DjfN8kf6smfJafiv4p82'
  openai.api_key = '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'

  print('[PROCESANDO]'.center(40, '-'))

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature= 0.8,
    messages=[
      {"role": "system", "content": """Realiza el calculo factorial del numero que se te sea enviado.
      E.G: 5
      respuesta: 120"""},
      {"role": "user", "content": prompt}
    ]
  )
  content= completion.choices[0].message.content
  total_tokens= completion.usage.total_tokens


  print('[SE TERMINO DE PROCESAR]'.center(40, '-'))
  return [content, total_tokens]
