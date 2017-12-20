class Ticket(object):
    #
    title = str()
    description = str()
    ...
    
    def serialize(self):
        return {
            'Title': self.Title, 
            'Description': self.Description,
        }
