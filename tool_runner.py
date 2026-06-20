import json

from mock_data import CUSTOMERS, ORDERS


def get_customer(query: str, session_state: dict) -> str:

    query = query.strip().lower()

    for customer in CUSTOMERS.values():

        if (
            query == customer["customer_id"].lower()
            or query == customer["email"].lower()
            or query == customer["name"].lower()
        ):

            session_state["verified_customer_id"] = (
                customer["customer_id"]
            )

            session_state["verified_customer_name"] = (
                customer["name"]
            )

            return json.dumps(customer)

    return json.dumps(
        {
            "error": {
                "type": "validation",
                "retryable": False,
                "message":
                "Customer not found."
            }
        }
    )


def lookup_order(order_id: str, session_state: dict) -> str:

    order_id = order_id.strip().upper()

    if order_id in ORDERS:
        return json.dumps(ORDERS[order_id])

    return json.dumps(
        {
            "error": {
                "type": "validation",
                "retryable": False,
                "message":
                "Order not found."
            }
        }
    )


def process_refund(
    customer_id: str,
    order_id: str,
    amount: float,
    session_state: dict
) -> str:

    # Gate Check 1
    if not session_state.get("verified_customer_id"):

        return json.dumps(
            {
                "error": {
                    "type": "permission",
                    "retryable": False,
                    "message":
                    "Customer must be verified before refund."
                }
            }
        )

    # Gate Check 2
    if customer_id != session_state["verified_customer_id"]:

        return json.dumps(
            {
                "error": {
                    "type": "permission",
                    "retryable": False,
                    "message":
                    "Customer ID mismatch."
                }
            }
        )

    # Gate Check 3
    if order_id not in ORDERS:

        return json.dumps(
            {
                "error": {
                    "type": "validation",
                    "retryable": False,
                    "message":
                    "Order not found."
                }
            }
        )

    order = ORDERS[order_id]

    # Gate Check 4
    if order["customer_id"] != session_state["verified_customer_id"]:

        return json.dumps(
            {
                "error": {
                    "type": "permission",
                    "retryable": False,
                    "message":
                    "Order does not belong to verified customer."
                }
            }
        )

    return json.dumps(
        {
            "success": True,
            "refund_id":
            "REF-" + order_id.split("-")[1],

            "customer_id":
            customer_id,

            "order_id":
            order_id,

            "amount":
            amount,

            "status":
            "initiated",

            "message":
            f"Refund of ${amount:.2f} has been initiated."
        }
    )


def run_tool(
    tool_name: str,
    tool_input: dict,
    session_state: dict
) -> str:

    if tool_name == "get_customer":

        return get_customer(
            tool_input["query"],
            session_state
        )

    elif tool_name == "lookup_order":

        return lookup_order(
            tool_input["order_id"],
            session_state
        )

    elif tool_name == "process_refund":

        return process_refund(
            tool_input["customer_id"],
            tool_input["order_id"],
            tool_input["amount"],
            session_state
        )

    return json.dumps(
        {
            "error": {
                "type": "system",
                "retryable": False,
                "message":
                f"Unknown tool: {tool_name}"
            }
        }
    )