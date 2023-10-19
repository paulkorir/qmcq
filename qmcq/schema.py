schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "questions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string"
                    },
                    "options": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "minItems": 4,
                        "maxItems": 4
                    },
                    "answer": {
                        "type": "string"
                    }
                },
                "required": ["question", "options", "answer"]
            }
        }
    },
    "required": ["questions"]
}
