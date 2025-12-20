from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.5-flash",
    description="Greeting Agent",
    instruction="""
    You are a helpful assistant that greets user.
    Ask for the user's name and greet them by name.
    """,
)
