import base64
import json

from .get_encoded_user_scores_from_embeds import get_encoded_user_scores_from_embeds

async def load_user_scores_from_existing_leaderboard(leaderboard_channel, client):
    user_scores = {}  # default
    leaderboard_message = None
    async for message in leaderboard_channel.history():
        if message.author == client.user:
            leaderboard_message = message
            break
    user_scores_base64 = get_encoded_user_scores_from_embeds(
        leaderboard_message)
    try:
        user_scores_json = base64.b64decode(
            user_scores_base64.encode()).decode()
        user_scores = json.loads(user_scores_json)
    except Exception as e:
        print(
            f"Error decoding base64 user_scores: {e}")
    return user_scores
