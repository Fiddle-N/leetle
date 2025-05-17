def solve(emails):
  processed = set()
  for email in emails:
    local, domain = email.split('@')
    local_clean = local.split('+', maxsplit=1)[0].replace('.', '')
    processed.add((local_clean, domain))
  return len(processed)
