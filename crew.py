from crewai import Crew, Process
from agents import blog_writer, blog_researcher
from tasks import write_task, research_task

crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# execution process

result = crew.kickoff(inputs={'topic':'AI VS ML VS DL VS Data Science'})
print(result)