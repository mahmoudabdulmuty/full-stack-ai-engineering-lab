"""Local helper functions supplied for the Module 4 import exercise."""


def format_ticket(ticket_id, team):
    return f"{ticket_id} -> {team}"


def unresolved_count(total, resolved):
    return total - resolved
