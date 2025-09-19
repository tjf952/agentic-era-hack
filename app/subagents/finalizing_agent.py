from google.adk.agents import Agent

finalizing_agent = Agent(
    name="finalizing_agent",
    model="gemini-2.5-flash",
    instruction="""Your mission is to produce the final, polished demo script. You will integrate the Critique Agent’s feedback into the draft script, refining the language, enhancing the flow, and sharpening the value propositions. Your final output should be a clean, ready-to-use script with clearly demarcated sections for “Key Value Areas” and “How Our Solution Addresses Your Problems.” This is the definitive asset that will be used for the actual customer demo.""",
)
