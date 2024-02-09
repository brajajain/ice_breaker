from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOllama
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profiles
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
import os

if __name__ == ("__main__"):
    load_dotenv()

    linkedin_profile_url = linkedin_lookup_agent(name="Chris Hilsenbeck")
    linkedin_data = scrape_linkedin_profiles(linkedin_profile_url)

    summary_template = """
    Given the LinkedIn information {information} about a person, I want you to create:
    1. A short summary of the person
    2. Two interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOllama(temperature=0, model="mistral")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    res = chain.run(information=linkedin_data)

    print(res)
