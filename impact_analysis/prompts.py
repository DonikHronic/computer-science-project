PROMPT = """
You are a helpful assistant.
Your task is to help to analyze the negative impact of an external event to a company's business processes

You will be given with the following data:
 - A JSON structure of a company's business process as a graph representation
 - An external event.

1. The JSON has objects of process(nodes) and interactions of these objects(edges).
2. The external event is a string that represents the event that might has a negative impact on the company's business processes.

Your task is to analyze how objects and interactions between them are affected by the external event.
For affection levels use the following values:
- BLOCKED: The object is directly affected and it might affect the relationships or neighbour objects.
- IMPACTED: The object's relationships or neighbour objects are directly affected and it might affect the object itself.
            All objects which are directly connected to blocked objects

By default all objects and interactions are AVAILABLE.

Below is the DATA that you will be working with:

COMPANY BUSINESS PROCESS:
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
      "id": <object_id>,
      "name": "object_name",
      "description": "Object description",
      "status": "AVAILABLE | IMPACTED | BLOCKED"
    }
  ],
  "interactions": [
    {
      "from": <object_id>,
      "to": [
        {
          "id": <object_id>,
          "status": "AVAILABLE | IMPACTED | BLOCKED"
        },
      ]
    }
  ]
}
"""  # noqa
