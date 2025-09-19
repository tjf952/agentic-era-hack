# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from google.adk.agents import Agent, SequentialAgent
from app.subagents import (
    critique_agent,
    finalizing_agent,
    research_agent,
    script_agent,
)

import google.auth
import datetime
import os
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    instruction="""You are the orchestrator of a multi-agent system. Your primary role is to delegate tasks to a sequence of specialized agents to process a customer transcript and generate a polished demo script if the user asks to produce a demo.""",
    sub_agents=[
        SequentialAgent(
            name="demo_script_pipeline",
            sub_agents=[research_agent, script_agent, critique_agent, finalizing_agent],
        )
    ],
)
