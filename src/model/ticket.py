class Ticket(object):
    """A ZenDesk ticket object
    Tickets are the means through which your end users (customers) communicate with agents in Zendesk Support.

    Attributes:
        See here for full list of attributes and descriptions:
        https://developer.zendesk.com/rest_api/docs/core/tickets

    """
    def __init__(self, json_object):
        """Initializes a new Ticket object from a json object

        Args:
            json_object (dict): Dictionary representation of a Ticket (typically from an API response)

        """
        self.id = json_object['id']
        self.url = json_object['url']
        self.external_id=json_object['external_id']
        self.created_at = json_object['created_at']
        self.updated_at = json_object['updated_at']
        self.type = json_object['type']
        self.subject= json_object['subject']
        self.raw_subject = json_object['raw_subject']
        self.description = json_object['description']
        self.priority = json_object['priority']
        self.status = json_object['status']
        self.recipient = json_object['recipient']
        self.requester_id = json_object['requester_id']
        self.submitter_id = json_object['submitter_id']
        self.assignee_id = json_object['assignee_id']
        self.organization_id = json_object['organization_id']
        self.group_id = json_object['group_id']
        self.collaborator_ids = json_object['collaborator_ids']
        self.follower_ids = json_object['follower_ids']
        self.problem_id = json_object['problem_id']
        self.has_incidents = json_object['has_incidents']
        self.due_at = json_object['due_at']
        self.tags = json_object['tags']
        self.via = json_object['via']
        self.custom_fields = json_object['custom_fields']
        self.satisfaction_rating = json_object['satisfaction_rating']
        self.sharing_agreement_ids = json_object['sharing_agreement_ids']

    def get_ticket_as_list(self, key_list):
        return_list = []
        for key in key_list:
            return_list.append(getattr(self, key))
        return return_list