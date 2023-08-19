class SMS_store():
    def __init__(self):
        self.message = []

    def __str__(self):
        return f"{self.message}"

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.message.append((False, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        return len(self.message)

    def get_unread_indexes(self):
        count_list = []
        for text in self.message:
            # if the message has not been viewed
            if not text[0]:
                index = self.message.index(text)
                count_list.append(index)
        return count_list

    def get_message(self, i):
        if i >= len(self.message):
            return None
        else:
            text = self.message[i]
            # Tuples are immutable, so we have to concatenate
            # Create a separate list that turns False into True
            # Concatenate the remainder of self.message[i]
            read_text = (True,) + text[1:]
            self.message[i] = read_text
            return text[1:]


# Test cases 
inbox = SMS_store()
inbox.add_new_arrival("12345", "10:25", "This is the first message")
inbox.add_new_arrival("678910", "10:28", "Second message here")
inbox.add_new_arrival("11121314", "10:38", "Now we have the third message")
inbox.add_new_arrival("20212223", "10:49", "Finally the fourth message")
print(inbox)
print(inbox.message_count())
print(inbox.get_unread_indexes())
print(inbox.get_message(0))
print(inbox.get_unread_indexes())
print(inbox)
print(inbox.get_message(2))
print(inbox.get_unread_indexes())
print(inbox)
