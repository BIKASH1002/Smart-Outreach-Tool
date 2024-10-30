import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature = 0, groq_api_key = os.getenv("GROQ_API_KEY"), model = "llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Natasha Romanoff, a business development executive at ZenX. ZenX is an AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools. 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of ZenX
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase ZenX's portfolio: {link_list}
            Remember you are Natasha Romanoff, BDE at ZenX. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content
    
    def write_ab_test_mails(self, job, links):
        prompt_email_v1 = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Natasha Romanoff, a business development executive at ZenX. ZenX is an AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools. 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a formal cold email to the client regarding the job mentioned above describing the capability of ZenX
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase ZenX's portfolio: {link_list}
            Remember you are Natasha Romanoff, BDE at ZenX. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE and VERSION A):
            """
        )
        prompt_email_v2 = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Natasha Romanoff, a business development executive at ZenX. ZenX is an AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools. 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a friendly cold email to the client regarding the job mentioned above describing the capability of ZenX
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase ZenX's portfolio: {link_list}
            Remember you are Natasha Romanoff, BDE at ZenX. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE and VERSION B):
            """
        )
        chain_email_v1 = prompt_email_v1 | self.llm
        chain_email_v2 = prompt_email_v2 | self.llm

        email_a = chain_email_v1.invoke({"job_description": str(job), "link_list": links}).content
        email_b = chain_email_v2.invoke({"job_description": str(job), "link_list": links}).content

        return email_a, email_b


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))