import sys

def marketing():
	clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
		'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
		'elon@paypal.com', 'jessica@gmail.com']
	participants = ['walter@heisenberg.com', 'vasily@mail.ru',
		'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
		'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
	recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

	set_clients = set(clients)
	set_participants = set(participants)
	set_recipients = set(recipients)

	if (len(sys.argv) != 2):
		return

	if (sys.argv[1] == "call_center"):
		set_notSeenPromotion = set_clients - set_recipients
		print(set_notSeenPromotion)

	elif (sys.argv[1] == "potential_clients"):
		set_notClients = set_participants - set_clients
		print(set_notClients)

	elif (sys.argv[1] == "loyalty_program"):
		set_notParticipate = set_clients - set_participants
		print(set_notParticipate)

	else:
		return

if __name__ == '__main__':
	marketing()
