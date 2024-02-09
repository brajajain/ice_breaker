from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOllama
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profiles
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parser import person_intel_parser, PersonIntel

def ice_break(name: str) -> PersonIntel:
    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profiles(linkedin_profile_url)

    summary_template = """
    Given the LinkedIn information {information} about a person, I want you to create:
    1. A short summary of the person
    2. Two interesting facts about the person
        \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={"format_instructions":person_intel_parser.get_format_instructions()},
    )

    llm = ChatOllama(temperature=0, model="mistral")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    res = chain.run(information=linkedin_data)

    return person_intel_parser.parse(res)


if __name__ == ("__main__"):
    print("Hello Langchain")
    ice_break("Harrison Chase")
