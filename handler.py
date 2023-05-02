import json
from src.infrastructure.spacy_script_processor import SpacyScriptProcessor
#

def process_script_handler(event, context):
    try:
        body = json.loads(event["body"])
        content = body["content"]

        script_processor = SpacyScriptProcessor()
        play_script = script_processor.process(content)

        return {
            "statusCode": 200,
            "body": json.dumps(
                {"characters": play_script.characters, "scenes": play_script.scenes}
            ),
        }
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"message": str(e)})}
