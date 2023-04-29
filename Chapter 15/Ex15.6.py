class SMS_store:
    def __init__(self):
        # Basically an inbox. Before receiving any message the inbox is empty, hence an empty list.
        self.message = []

    def __str__(self):
        return "{0}".format(self.message)

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS = text_of_SMS
        return self.message.append((False, self.from_number, self.time_arrived, self.text_of_SMS))

    def message_count(self):
        return len(self.message)

    def get_unread_indexes(self):
        index_list = []
        for index, message in enumerate(self.message):
            # if the message has not been viewed
            if not message[0]:
                index_list.append(index)
        return index_list

    def get_message(self, i):
        if i >= len(self.message):
            return None
        else:
            # Tuples are immutable, so we have to concatenate
            # Create a separate list that turns False into True
            # Concatenate the remainder of self.message[i]
            read_message = (True, ) + self.message[i][1:]
            return read_message

    def delete(self, i):
        del self.message[i]
        return self.message

    def clear(self):
        self.message.clear()
        return self.message
