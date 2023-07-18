class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        call_string = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_string)
        self.call_history.append(call_string)

    def show_call_history(self):
        print("Call History:")
        for call in self.call_history:
            print(call)

    def send_message(self, to_phone, content):
        message = {
            "to": to_phone.phone_number,
            "from": self.phone_number,
            "content": content,
        }
        self.messages.append(message)

    def show_outgoing_messages(self):
        print("Outgoing Messages:")
        for message in self.messages:
            if message["from"] == self.phone_number:
                print(f"To: {message['to']}, Content: {message['content']}")

    def show_incoming_messages(self):
        print("Incoming Messages:")
        for message in self.messages:
            if message["to"] == self.phone_number:
                print(f"From: {message['from']}, Content: {message['content']}")

    def show_messages_from(self, from_phone):
        print(f"Messages from {from_phone.phone_number}:")
        for message in self.messages:
            if message["from"] == from_phone.phone_number:
                print(f"To: {message['to']}, Content: {message['content']}")


# Example usage
phone1 = Phone("123456789")
phone2 = Phone("987654321")

phone1.call(phone2)
phone2.call(phone1)

phone1.send_message(phone2, "Hello!")
phone2.send_message(phone1, "Hi there!")

phone1.show_call_history()

phone2.show_incoming_messages()

phone1.show_messages_from(phone2)
