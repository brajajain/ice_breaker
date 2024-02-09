from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOllama
from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatOllama(temperature=0, model="llama2")

    tools_for_agent = [
        (
            Tool(
                name="Crawl google for LinkedIn profile page.",
                func=get_profile_url,
                description="useful for retrieving the LinkedIn profile for a person when provided only a name.",
            )
        )
    ]
    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
    )

    summary_template = """
    Given the full name of a person {name_of_person}, I want you to get me a URL to the their LinkedIn profile page. 
        Your final answer should only contain a URL.
    """
    prompt_template = PromptTemplate(input_variables=["name_of_person"], template=summary_template)

    linkedin_profile_url = agent.invoke(prompt_template.format(name_of_person=name))
    return linkedin_profile_url
