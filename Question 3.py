raw_input = int(input().strip())
is_active = bool(raw_input)

print(f"Initial: {is_active}")

is_active = not is_active

print(f"Toggled: {is_active}")
