from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOllama
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profiles
import os

if __name__ == ("__main__"):
    load_dotenv()

    linkedin_profile_url = "https://gist.githubusercontent.com/brajajain/39d2c27a8d8920fe638861b14353f819/raw/5b1c156bd716cc172f0df8703d52c88304c52017/brjain-linkedin.json"

    linkedin_data = scrape_linkedin_profiles(linkedin_profile_url)

    summary_template = """
    Given the LinkedIn information {information} about a person, I want you to create:
    1. A short summary of the person
    2. two interesting facts about the person
    """

    summary_promp_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOllama(temperature=0, model="llama2")

    chain = LLMChain(llm=llm, prompt=summary_promp_template)

    res = chain.run(information=linkedin_data)

    print(res)
