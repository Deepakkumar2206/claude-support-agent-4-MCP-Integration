# Customer Support Agent - MCP Integration

This project is an upgraded version of my Customer Support Agent built using the Anthropic Claude API. In the previous stages, the tools were directly connected to the agent. In this stage, I moved those tools into an MCP (Model Context Protocol) server so they can be reused and managed separately.

The agent can:

* Look up customer details
* Look up order information
* Process refunds
* Verify customers before refunds
* Access tools through an MCP Server

---

## What I Learned

Before this project, all tools were defined inside the application itself. This works for small projects, but becomes difficult to maintain when multiple agents need the same tools.

With MCP, tools can be exposed through a separate server and shared across different applications without duplicating code.

I also learned:

* What MCP (Model Context Protocol) is
* How MCP Servers work
* How to expose Python functions as MCP tools
* How to configure MCP using `mcp.json`
* How to test tools using MCP Inspector
* Why environment variables should be used instead of hardcoded secrets

---

## Project Structure

```text
customer-support-agent/

├── agent.py
├── tools.py
├── tool_runner.py
├── mock_data.py
├── mcp_server.py
├── .claude/
│   └── mcp.json
├── .env
├── .gitignore
└── README.md
```

---

## Creating the MCP Server

I created an MCP server using FastMCP.

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("support-agent-tools")
```

This creates an MCP server named `support-agent-tools`.

---

## Exposing Existing Tools

The existing customer support functions were converted into MCP tools.

```python
@mcp.tool()
def get_customer_tool(query: str):
    return get_customer(query, session_state)
```

Now the tool can be discovered and called through MCP.

---

## MCP Configuration

```json
{
  "mcpServers": {
    "support-agent-tools": {
      "command": "python",
      "args": ["mcp_server.py"]
    }
  }
}
```

This configuration tells Claude how to start and connect to the MCP server.

---

## Testing with MCP Inspector

I used MCP Inspector to verify that the server was running correctly and exposing the tools.

```bash
mcp dev mcp_server.py
```

Using MCP Inspector, I was able to:

* Connect to the server
* View available tools
* Test tool execution
* Verify responses

---

## Available MCP Tools

### get_customer_tool

Find customer details using:

* Customer ID
* Email Address
* Full Name

### lookup_order_tool

Retrieve order information using an Order ID.

### process_refund_tool

Process refunds after customer verification checks pass.

---

## Technologies Used

* Python
* Anthropic Claude API
* MCP Python SDK
* FastMCP
* MCP Inspector
* python-dotenv

---

## Author

Deepakkumar
