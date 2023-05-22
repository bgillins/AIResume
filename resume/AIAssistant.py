import langchain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import openai

from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()


class Assistant():
    def __init__(self):
        self.name = "Resume AI Assistant"
        self.openai_key = os.getenv('OPENAI_API_KEY')

        #connect to pinecone database
        # self.pinecone_key = os.getenv("PINECONE_API_KEY")
        # self.pinecone_index = os.getenv("PINECONE_INDEX_NAME")

    def ai_role(self):

        role = 'You are a professional resume writer. You will only use factional information about the candidate to write the resume.'

        return role

    def setting_up_openai(self):

        llm = OpenAI(temperature= 0.9)

    def ai_job_focused(self, job_title):
        # set up langchain page where we chain together two prompts
        # first prompt is preferred job title for recipient

        role = self.ai_role()
        job_title = job_title

        preferred_job_title_template = PromptTemplate(
            input_variables=['preferred_job_title', 'role'],
            template='{role} Please write a short description less than 250 words about {preferred_job_title}. Please make a commonly accepted skills for this position. Please put all skills in a bulletpoints. Follow up is this the type of role you would like to proceed creating a resume?'
        )

        llm = OpenAI(openai_api_key=self.openai_key,temperature=0.9)
        preferred_job_prompt = LLMChain(llm=llm, prompt=preferred_job_title_template, verbose=True)

        return preferred_job_prompt

    def ai_experience(self, job_title):
        # set up langchain page where we chain together two prompts
        # first prompt is preferred job title for recipient

        role = self.ai_role()
        job_title = job_title

        job_experience_template = PromptTemplate(
            input_variables=['previous_experience_1', 'role'],
            template="{role} I will provide previous work experience. I need you to come up with questions to help improve my resume. Please number each question in the following format (1). I will provide my experience {previous_experience_1}"
        )
        llm = OpenAI(openai_api_key=self.openai_key,temperature=0.9)
        job_experience_prompt = LLMChain(llm=llm, prompt=job_experience_template, verbose=True)

        return job_experience_prompt
