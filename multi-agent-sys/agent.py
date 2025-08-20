from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_ibm import WatsonxLLM
import os

os.environ["WATSONX_API_KEY"] = "your-api-key"
os.environ["SERPER_API_KEY"] = "your-api-key"

# parameters for the model
params = {"decoding_method": "greedy", "max_tokens": 500, "temperature": 0.5}

# create the llm
llm = WatsonxLLM(
    model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct",
    url = "https://us-south.ml.cloud.ibm.com",
    params = params,
    project_id = "your-project-id",
)

print(llm.invoke("What is the capital of France?"))

# create function calling llm
function_calling_llm = WatsonxLLM(
    model_id = "ibm-mistral/merlinite-7b",
    url = "https://us-south.ml.cloud.ibm.com",
    params = params,
    project_id = "your-project-id",
)

# create the search tool
search_tool = SerperDevTool()

# create the research agent
research_agent = Agent(
    llm=llm,
    function_calling_llm=function_calling_llm,
    role="Senior AI Researcher",
    goal="You are tasked with researching the latest trends in AI.",
    backstory="You are a senior AI researcher with a passion for finding the latest and most relevant information on synthetic biology.",
    allow_delegation=False,
    tools=[search_tool],
    verbose=True,
)

# create the writer agent
writer_agent = Agent(
    llm=llm,
    function_calling_llm=function_calling_llm,
    role="Senior AI Writer",
    goal="You are tasked with writing a blog post about the latest trends in AI.",
    backstory="You are a senior AI writer with a passion for writing about the latest trends in AI.",
    allow_delegation=False,
    verbose=True,
)

# create the task
task_1 = Task(
    description="Research the latest trends in AI.",
    agents=[research_agent],
    expected_output="A list of the latest trends in AI.",
    output_file="task_1_output.txt",
    agent=research_agent,
)

# create the task
task_2 = Task(
    description="Write a blog post about the latest trends in AI.",
    agents=[writer_agent],
    expected_output="A blog post about the latest trends in AI.",
    output_file="task_2_output.txt",
    agent=writer_agent,
)


# create the crew
crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[task_1, task_2],
    verbose=True,   
)

crew.run()
print(crew.get_task_output(task_1))
print(crew.get_task_output(task_2))