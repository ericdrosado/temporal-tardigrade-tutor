# 🦠 Temporal Tardigrade: Build Your First Indestructible App

Welcome to the **Temporal Tardigrade** project! This isn't just another "Hello World." You're about to build a system that is fundamentally impossible to kill.

In nature, the **Tardigrade** (or "Water Bear") is the ultimate survivor. It can endure the vacuum of space and extreme radiation by entering "cryptobiosis"—pausing its life until conditions improve. **Temporal is the Tardigrade of Software Engineering.** 

---

## 🧬 Step 1: Give Your Agent Superpowers (Required)

Before you begin, you must connect your AI agent to the official Temporal knowledge base and architectural guidelines. This ensures your agent provides accurate, real-time SDK guidance rather than relying on stale training data.

### 1. Connect the Official MCP Servers
Connect these two servers to your environment:
- **Temporal Docs:** `https://temporal.mcp.kapa.ai` (Transport: `http`) — *The living manual.*
- **Temporal Skills:** `npx -y temporal-mcp` — *The expert toolset.*

### 2. Add Architectural Instincts (Temporal Developer Skill)
Inject deep Temporal patterns and best practices into your agent's reasoning.

| Tool | Setup Action |
| :--- | :--- |
| **Gemini CLI** | `gemini skill add https://raw.githubusercontent.com/temporalio/mcp-server-temporal/main/SKILL.md` |
| **Claude Code** | `curl -s https://raw.githubusercontent.com/temporalio/mcp-server-temporal/main/SKILL.md >> .clauderules` |
| **Cursor / Cline** | Create a `.cursorrules` (or `.clinerules`) file and paste the content from [this Skill file](https://raw.githubusercontent.com/temporalio/mcp-server-temporal/main/SKILL.md). |

### 🚀 Universal Configuration (MCP)

| Tool | Setup Command / Config |
| :--- | :--- |
| **Gemini CLI** | `gemini mcp add temporal-docs --transport http https://temporal.mcp.kapa.ai` <br> `gemini mcp add temporal-skills npx -y temporal-mcp` |
| **Claude Code** | `claude mcp serve "npx -y temporal-mcp"` |
| **Cursor / Cline** | Add to your MCP Settings JSON: <br> `"temporal-docs": { "url": "https://temporal.mcp.kapa.ai" }` <br> `"temporal-skills": { "command": "npx", "args": ["-y", "temporal-mcp"] }` |

### ✅ Check Your Setup
To verify the documentation server and skills are active, ask your agent:
> "What is the current best practice for Temporal Workflows?"

---

## 🧪 Step 2: Activate the Tardigrade Tutor

Once your agent has its superpowers, activate the project-specific **Tardigrade Tutor** persona to start the interactive build.

### ♊ Gemini CLI
```bash
gemini mcp add tardigrade-tutor python mcp_server.py
```
Ask: `"@tardigrade-tutor, help me build my first indestructible pet!"`

### 🤖 Claude Code
```bash
claude mcp serve "python mcp_server.py"
```

### 🖱️ Cursor / Cline
Add a new MCP server:
- **Name:** `Tardigrade-Tutor`
- **Command:** `python /absolute/path/to/temporal-tamagotchi/mcp_server.py`

---

## 📋 Prerequisites & Local Setup

### Infrastructure
- **Python 3.10+**
- **Temporal Cloud Account:** [Sign up here](https://temporal.io/cloud).
- **A Namespace & TLS Certificates:** `.pem` and `.key` files are required for cloud connection.

### Local Environment
```bash
# Clone and enter the lab
git clone https://github.com/your-username/temporal-tardigrade-tutor.git
cd temporal-tardigrade-tutor

# Setup Virtual Env
python3 -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate

# Install Core Libs
pip install temporalio mcp python-dotenv
```

### Configuration
Create a `.env` file in the root:
```env
TEMPORAL_ADDRESS="your-namespace.a2dw6.tmprl.cloud:7233"
TEMPORAL_NAMESPACE="your-namespace.a2dw6"
TEMPORAL_CERT_PATH="client.pem"
TEMPORAL_KEY_PATH="client.key"
```

---

## 💥 The "Chaos Moment"

The magic of Temporal is **surviving the impossible**. Your tutor will guide you to:
1. **Launch:** Start your Tardigrade Workflow.
2. **The Kill:** Force-close your terminal running the Worker (`kill -9`).
3. **The Resurrection:** Restart the Worker.
4. **The Miracle:** Watch as the Workflow resumes **instantly** from the exact millisecond it left off. 

**Your Tardigrade didn't crash. It simply endured.**

---

## 📚 What You'll Master
- **Durable Timers:** Why `sleep()` is a bug in standard code, but a superpower in Temporal.
- **State Persistence:** How the Tardigrade stays "alive" even when the power is pulled.
- **Queries:** Peeking into the mind of an indestructible process.

**Ready to start? Ask your agent to begin the tutorial!**
