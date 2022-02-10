def response(speech: str):
    speech = speech.strip()
    return ('Sure.', "Calm down, I know what I'm doing!")[speech.isupper()] \
        if speech.endswith('?') else 'Whoa, chill out!' \
        if speech.isupper() else 'Whatever.' \
        if speech else 'Fine. Be that way!'
