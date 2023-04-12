import messagebird

client = messagebird.Client('your api key')

try:

    msg = client.voice_message_create('+4917', 'Hello, this is a test call from your Python script using MessageBird.', {'voice' : 'male'}
                                
)
    print(msg.__dict__)


except messagebird.client.ErrorException as e:

    for error in e.errors:
        print(error)
