# Customer Support Agent - Stage 2

A Python-based AI Customer Support Agent built using the Anthropic Claude API. This project demonstrates tool calling, structured error handling, detailed tool descriptions, and customer/order lookup workflows.

## Overview

This agent can:

* Look up customer records using name, email, or customer ID.
* Look up order information using order ID.
* Use Claude's tool-calling capabilities to retrieve data.
* Return structured validation errors when records are not found.
* Provide helpful and user-friendly support responses.

This project was built as part of the Claude Certified Architect preparation track.

---

## Features

### Customer Lookup Tool

Search customers using:

* Customer ID (Example: `CUST-4492`)
* Email Address (Example: `sarah.chen@email.com`)
* Full Name (Example: `Sarah Chen`)

Returns:

* Customer ID
* Name
* Email
* Account Status
* Membership Date
* Total Orders
* Associated Order IDs

---

### Order Lookup Tool

Search orders using:

* Order ID (Example: `ORD-8821`)

Returns:

* Order Status
* Items Purchased
* Order Date
* Shipping Information
* Tracking Details
* Internal Notes

---

### Structured Error Handling

Instead of returning generic messages like:

```json
{
  "error": "Something went wrong"
}
```

The agent returns structured errors:

```json
{
  "error": {
    "type": "validation",
    "retryable": false,
    "message": "No order found with ID 'ORD-9999'."
  }
}
```

Benefits:

* Easier for Claude to reason about failures.
* Better user experience.
* Reduced context window usage.
* More reliable production behavior.

---

## Project Structure

```text
customer-agent-stage2/
│
├── agent.py
├── tools.py
├── tool_runner.py
├── mock_data.py
├── .env
├── .gitignore
└── README.md
```

---

## Technologies Used

* Python 3
* Anthropic Claude API
* python-dotenv
* JSON
* Tool Calling

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Deepakkumar2206/customer-agent-stage2.git
cd customer-agent-stage2
```

### Install Dependencies

```bash
pip install anthropic python-dotenv
```

### Create Environment File

Create a `.env` file:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

---

## Run the Agent

```bash
python agent.py
```

---

## Example Conversation

### Customer Lookup

```text
Customer: Sarah Chen
```

Agent retrieves:

```text
Customer ID: CUST-4492
Email: sarah.chen@email.com
Status: Active
```

---

### Order Lookup

```text
Customer: Check order ORD-8821
```

Agent retrieves:

```text
Status: Processing
Days Since Order: 6
Note: Warehouse inventory hold.
```

---

### Validation Error Example

```text
Customer: Check order ORD-9999
```

Agent response:

```text
No order found with ID 'ORD-9999'.
Please verify the order number and try again.
```

---

## Learning Outcomes

This project demonstrates:

* Claude Tool Calling
* Multi-tool Agent Workflows
* Structured Error Design
* Tool Description Engineering
* JSON Tool Responses
* Customer Support Agent Design
* AI Agent Reliability Best Practices

---

## Author

Deepakkumar

* Blockchain & Web3 Developer
* Smart Contract Engineer
* AI Agent Builder

GitHub:
https://github.com/Deepakkumar2206

```
```
