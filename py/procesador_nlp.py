# procesador_nlp.py

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from decoradores import tiempo_de_ejecucion


class MiProcesadorNLP:
    def __init__(self, temperatura=0.5, max_tokens=100, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0):
        self.template = """{question}"""
        self.prompt = PromptTemplate(input_variables=["question"], template=self.template)
        self.llm = OpenAI(temperature=temperatura, max_tokens=max_tokens, top_p=top_p,
                          frequency_penalty=frequency_penalty, presence_penalty=presence_penalty)
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    @tiempo_de_ejecucion
    def ejecutar(self, question):
        return self.chain.run(question=question)
