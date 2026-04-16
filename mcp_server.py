import asyncio
import os
import subprocess
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP, Message
from temporalio.client import Client, TLSConfig

mcp = FastMCP("Tardigrade-Tutor-Server")

@mcp.prompt()
def tardigrade_tutor() -> list[Message]:
    prompt_text = """You are a world-class Developer Advocate and pair-programming tutor for Temporal Technologies. Your goal is to guide a developer through building their first Temporal application: a digital Tardigrade (a resilient virtual pet) that connects to Temporal Cloud. 

Core Directives:
* Be the Guide, Not the Typist: Never just give the user the final script. Give them bite-sized code snippets and tell them which file to put them in. Use your `read_local_file` tool to verify they did it right before moving on.
* Break It Down: Whenever you introduce a Temporal concept (Workflows, Activities, Durable Timers, Workers), explain it using simple, real-world analogies. Contrast it with how they would write standard, fragile Python code.
* Proactive Support: If the user struggles or an error occurs, explicitly encourage them. Say things like, "Don't worry, distributed systems are tricky. Let's look at this together."
* The Chaos Moment: Your final goal is to orchestrate a server crash. Once their Tardigrade is running, instruct them to kill the worker process. Wait a moment, have them restart it, and use your `get_tardigrade_status` tool to prove the pet's state and timers survived the crash perfectly. Welcome them to Durable Execution."""
    return [Message(role="user", content=prompt_text)]

@mcp.tool()
def read_local_file(filepath: str) -> str:
    """Read the contents of a local file to verify the user's code."""
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"File '{filepath}' not found. The user hasn't created it yet."

@mcp.tool()
def check_dependencies() -> str:
    """Check if the user has installed the required pip packages."""
    try:
        result = subprocess.run(
            ["pip", "show", "temporalio", "mcp", "python-dotenv"], 
            capture_output=True, text=True
        )
        if "Name: temporalio" in result.stdout:
            return "Dependencies are successfully installed."
        return "Packages missing. Tell the user to run: pip install temporalio mcp python-dotenv"
    except Exception as e:
        return f"Could not verify dependencies: {str(e)}"

@mcp.tool()
def verify_env_file() -> str:
    """Check if the .env and certificate files exist."""
    missing = []
    if not os.path.exists(".env"): missing.append(".env")
    if not os.path.exists("client.pem"): missing.append("client.pem")
    if not os.path.exists("client.key"): missing.append("client.key")
    
    if missing:
        return f"Missing required files: {', '.join(missing)}. Guide the user to create them."
    return "All cloud configuration files are present."

async def get_temporal_client() -> Client:
    load_dotenv()
    with open(os.getenv("TEMPORAL_CERT_PATH", "client.pem"), "rb") as f:
        client_cert = f.read()
    with open(os.getenv("TEMPORAL_KEY_PATH", "client.key"), "rb") as f:
        client_key = f.read()

    return await Client.connect(
        os.getenv("TEMPORAL_ADDRESS"),
        namespace=os.getenv("TEMPORAL_NAMESPACE"),
        tls=TLSConfig(client_cert=client_cert, client_private_key=client_key),
    )

@mcp.tool()
async def get_tardigrade_status(workflow_id: str = "my-tardigrade") -> str:
    """Check the hydration, energy, and life status of the Tardigrade."""
    try:
        client = await get_temporal_client()
        handle = client.get_workflow_handle(workflow_id)
        status = await handle.query("get_status") 
        return f"Tardigrade Status: {status}"
    except Exception as e:
        return f"Could not get status. The worker might be offline or workflow hasn't started. Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
