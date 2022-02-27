def transform(legacy_data):
    return {letter.lower(): k for k, v in legacy_data.items() for letter in v}