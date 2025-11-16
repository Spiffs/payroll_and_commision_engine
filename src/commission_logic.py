def calculate_bonus_total(entries):
    """
    Calculates the sum of bonuses from a list of amount/percentage dictionaries.

    Args:
        entries (list): A list of dictionaries, each with 'amount' and 'percentage' keys.

    Returns:
        float: The total calculated bonus amount.
    """
    total = 0.0
    for entry in entries:
        # Access the values directly from the entry dictionary
        amount = entry.get('amount', 0.0)
        percentage = entry.get('percentage', 0.0)
        bonus_amount = amount * (percentage / 100.0)
        total += bonus_amount

    return total
