from pyrogram import Client

api_id = 28247021 # Замените на свой api_id
api_hash = '40c65b3a952023b873b8fbe54f4a5a65' # Замените на свой api_hash
message = "Привет, это тестовое сообщение на русском языке😱."

def send_messages():
    print("Starting send_messages")
    with Client('my_new_account', api_id, api_hash) as app:
        try:
            with open('users.txt', 'r') as f:
                users = [line.strip() for line in f]
        except Exception as e:
            print(f"Failed to read users. Error: {e}")
            return
        for user in users:
            try:
                app.send_message(user, message)
                print(f"Message sent to user {user}")
            except Exception as e:
                print(f"Failed to send message to user {user}. Error: {e}")
    print("Finished send_messages")

send_messages()