def check_for_numbers(text):
  """
    Validates input
  """
  for char in text:
    if not char.isdigit():
      return False
  return True