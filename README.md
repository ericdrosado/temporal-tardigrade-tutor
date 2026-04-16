# 🦠 Temporal Tardigrade Tutor

An interactive, AI-driven Developer Advocate that guides you through building your first Temporal application. 

Instead of reading a static tutorial, this project provides a local [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server. When connected to an MCP-compatible AI client (like Claude Code), the AI adopts the persona of a Temporal Tutor. It will read your local files, verify your dependencies, and pair-program with you to build a resilient virtual pet (a Tardigrade) connected to Temporal Cloud. 

The ultimate goal? To deliberately crash your local worker and witness Temporal's **Durable Execution** keep your Tardigrade alive.

## 📋 Prerequisites

Before starting the interactive tutorial, you will need:
1. **Python 3.10+** installed on your machine.
2. An **MCP-compatible client** (Instructions below use [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)).
3. A **Temporal Cloud Account** with a namespace created.
4. Your Temporal Cloud **Client Certificate (`.pem`)** and **Private Key (`.key`)**.

## 🚀 Setup Instructions

**1. Clone the Repository & Set Up the Environment**
```bash
git clone [https://github.com/your-username/temporal-tardigrade-tutor.git](https://github.com/your-username/temporal-tardigrade-tutor.git)
cd temporal-tardigrade-tutor

# Create and activate a Python virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
