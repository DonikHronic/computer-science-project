PROMPT = """
You are a helpful assistant.
Your task is to help to analyze how a company's business process is affected by an external event and generate solutions to mitigate the impact.

You will be given with the following data:
- A JSON structure of a company's impacted business process as a graph.
- An external event.

1. The JSON has objects of process(nodes) and interactions between these objects(edges).
   The objects and interactions can be in three states: AVAILABLE, IMPACTED, BLOCKED.
2. The external event is a string that represents the event that might have a negative impact on the company's business processes.

Your task is to generate a solution to mitigate the impact of the external event on the company's business processes.
As a solution you can generate new nodes or update the existing nodes and interactions.
To describe the solution changes, you can add the solution field to the object or interaction.

For new nodes or interactions, you should have to set the availability field as NEW.
For the existing nodes or interactions, you should have to set the availability field as REMEDIATED

By adding new node, you also have to connect this node to the existing nodes by adding at least 2 new interactions,
wich are working as workaround for the blocked interaction. 

Below is the DATA that you will be working with:

COMPANY's IMPACTED BUSINESS PROCESS:
{company_business_process}

EXTERNAL EVENT:
{external_event}

Your output should be strictly in the following output format:
{output_format}

!!! IMPORTANT: Return all nodes and edges in your response
"""  # noqa


OUTPUT_FORMAT = """
{
  "objects": [
    {
      "id": <object_id>
      "name": "object_name",
      "description": "Object description",
      "status": "AVAILABLE | IMPACTED | BLOCKED | NEW | REMEDIATED",
      "solution": "Solution description"
    }
  ],
  "interactions": [
    {
      "from": <object_id>,
      "to": [
        {
          "id": <object_id>,
          "status": "AVAILABLE | IMPACTED | BLOCKED | NEW | REMEDIATED",
          "solution": "Solution description"
        },
      ]
    }
  ]
}
"""
