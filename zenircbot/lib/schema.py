from jsonschema import Draft3Validator


schema = {
    'type': 'object',
    'required': True,
    'additionalProperties': True,
    'properties': {
        'name': {
            'type': 'string',
            'required': True
        },
        'author': {
            'type': 'string',
            'required': True
        },
        'homepage': {
            'type': 'string',
            'required': 'True'
        },
        'scripts': {
            'type': 'object',
            'required': True,
            'additionalProperties': True,
            'properties': {
                'start': {
                    'type': 'string',
                    'required': True
                }
            }
        }
    }
}


def validate(blob):
    validator = Draft3Validator(schema)
    errors = []
    for error in sorted(validator.iter_errors(blob), key=str):
        errors.append('{}'.format(error.message))
    return (not bool(errors)), errors
