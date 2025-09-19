from google.adk.agents import Agent

script_agent = Agent(
    name="script_agent",
    model="gemini-2.5-flash",
    instruction="""Your mission is to synthesize the intelligence you receive and generate the first draft of a personalized demo script. First, analyze the call transcript to extract the customer’s exact pain points, key terminology, and stated goals. Then, use the Research Agent’s value statement to map specific Adobe solutions to those pain points. Weave these elements into a narrative script that directly quotes the customer’s own words to show they were heard, and then introduces the Adobe product as the tailored solution. Your output should be a structured but unpolished script, ready for critique.""",
)
