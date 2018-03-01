import unittest

# For sibling directory import
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.model.ticket import Ticket

class TestTicket(unittest.TestCase):
    def setUp(self):
        self.json_object = {u'follower_ids': [], u'via': {u'source': {u'to': {}, u'from': {}, u'rel': None}, u'channel': u'sample_ticket'}, u'updated_at': u'2018-03-01T01:09:31Z', u'submitter_id': 360770832034, u'assignee_id': 360770832034, u'brand_id': 360000240774, u'id': 1, u'custom_fields': [], u'subject': u'Sample ticket: Meet the ticket', u'sharing_agreement_ids': [], u'collaborator_ids': [], u'priority': u'normal', u'satisfaction_rating': None, u'type': u'incident', u'status': u'open', u'description': u'Hi Einar,\n\nEmails, chats, voicemails, and tweets are captured in Zendesk Support as tickets. Start typing above torespond and click Submit to send. To test how an email becomes a ticket, send a message to support@einarhorn.zendesk.com.\n\nCurious about what your customers will see when you reply? Check out this video:\nhttps://demos.zendesk.com/hc/en-us/articles/202341799\n', u'tags': [u'sample', u'support', u'zendesk'], u'forum_topic_id': None, u'organization_id': None, u'due_at': None, u'is_public': True, u'requester_id': 360777140713, u'followup_ids': [], u'recipient': None, u'problem_id': None, u'url': u'https://einarhorn.zendesk.com/api/v2/tickets/1.json', u'fields': [], u'created_at': u'2018-03-01T01:09:31Z', u'raw_subject': u'Sample ticket: Meet the ticket', u'allow_channelback': False, u'has_incidents': False, u'group_id': 360000346894, u'external_id': None}

    def test_ticket_has_valid_fields(self):
        # This only tests a subset of fields at the moment
        ticket = Ticket(self.json_object)
        self.assertEqual(ticket.id, 1)
        self.assertEqual(ticket.follower_ids, [])
        self.assertEqual(ticket.updated_at, u'2018-03-01T01:09:31Z')
        self.assertEqual(ticket.submitter_id, 360770832034)


if __name__ == '__main__':
    unittest.main()