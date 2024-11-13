import os
from groq import Groq

def get_car_ai_bio(model, brand, year):
    prompt = '''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas especificas deste modelo de carro. Em portugues. não quero valores de aluguel ou de compra, quero apenas especificações técnicas
    '''

    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    prompt = prompt.format(brand,model,year)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em carros. Sua função é criar uma descrição técnica sobre o carro informado.",
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    ) 
    return (chat_completion.choices[0].message.content)  