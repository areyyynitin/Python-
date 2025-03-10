# Event Management System 
# Scenario: You are organizing a large event and need to manage the list of attendees. Some attendees have VIP access, while others do not. 
# Tasks: 
# 1. Create a set of attendees with names 'John', 'Jane', 'Emily', and 'Michael'. 
# 2. Create a frozenset vip_attendees with names 'Jane' and 'Michael'. 
# 3. A new attendee 'Sarah' registers for the event. Add her to the attendees set. 
# 4. Check if 'Emily' is a VIP attendee.
# 5. Find out which attendees have either regular or VIP access but not both. 6. List all attendees with either regular or VIP access.

attendees={'John', 'Jane', 'Emily', 'Michael'}
vipAttendees=frozenset({'Jane', 'Michael'})

print("Attendees: ", attendees)
print("VIP Attendees: ", vipAttendees)

attendees.add('Sarah')
if 'Emily' in vipAttendees:
    print("Emily is a VIP attendee.")
    

print("Attendees with either regular or VIP access but not both: ", attendees.symmetric_difference(vipAttendees))
print("VIP Attendees: ", vipAttendees)
print("Attendees: ", attendees)
