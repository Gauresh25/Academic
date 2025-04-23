import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import uuid
import json

fake = Faker()

# Constants (adjust to reach 5GB)
NUM_RECORDS = 50_000 # ~50M rows (~5GB)
CHUNK_SIZE = 10_000  # Chunk size to avoid memory issues

# Predefined options for categorical fields
ACTIVITY_TYPES = ['adventure', 'cultural', 'relaxation', 'culinary', 'nature', 'history']
TRAVEL_STYLES = ['budget', 'luxury', 'backpacking', 'family', 'solo']
ACCOMMODATION_TYPES = ['hotel', 'hostel', 'vacation rental', 'resort']
MOODS = ['relaxed', 'energetic', 'neutral', 'stress']
WEATHER_CONDITIONS = ['sunny', 'rainy', 'snowy', 'windy']
FLIGHT_STATUSES = ['on-time', 'delayed', 'cancelled']
EVENT_SOURCES = ['local_calendar', 'social_media', 'travel_blogs', 'ticketing_platforms']


def generate_geolocation():
    return f"{fake.latitude()},{fake.longitude()}"


def generate_conversation():
    queries = [
        f"Find me a {random.choice(['weekend', '7-day'])} trip to {fake.country()} under ${random.randint(500, 5000)}",
        f"I want a {random.choice(ACTIVITY_TYPES)} activity in {fake.city()}",
        "Suggest romantic places in Paris"
    ]
    return random.choice(queries)


def generate_activity():
    return {
        'activity_id': str(uuid.uuid4()),
        'activity_name': fake.bs(),
        'activity_type': random.choice(ACTIVITY_TYPES),
        'activity_tags': random.choice(['family-friendly', 'romantic', 'budget-friendly']),
        'activity_source': random.choice(EVENT_SOURCES),
        'trending_score': round(random.uniform(0, 10), 2),
        'price': round(random.uniform(20, 500), 2)
    }


def generate_user_data(num_records):
    data = {
        # User Profile
        'user_id': [str(uuid.uuid4()) for _ in range(num_records)],
        'travel_style': np.random.choice(TRAVEL_STYLES, num_records, p=[0.3, 0.2, 0.2, 0.2, 0.1]),
        'preferred_activities': [', '.join(np.random.choice(ACTIVITY_TYPES, random.randint(1, 3), replace=False)) for _
                                 in range(num_records)],
        'dietary_restrictions': np.random.choice(['none', 'vegetarian', 'vegan', 'gluten-free'], num_records,
                                                 p=[0.7, 0.1, 0.1, 0.1]),
        'physical_conditions': np.random.choice(['none', 'mobility', 'allergies'], num_records, p=[0.8, 0.1, 0.1]),
        'specific_interests': [
            ', '.join(np.random.choice(['art', 'nature', 'history'], random.randint(1, 2), replace=False)) for _ in
            range(num_records)],
        'past_trips': ['; '.join([fake.country() for _ in range(random.randint(1, 5))]) for _ in range(num_records)],
        'past_reviews': ['; '.join([fake.sentence() for _ in range(3)]) for _ in range(num_records)],
        'frequent_destinations': [fake.country() for _ in range(num_records)],
        'liked_activities': [', '.join(np.random.choice(ACTIVITY_TYPES, random.randint(1, 2), replace=False)) for _ in
                             range(num_records)],
        'accommodation_type': np.random.choice(ACCOMMODATION_TYPES, num_records),
        'budget_range': [f"{random.randint(500, 5000)}-{random.randint(5000, 15000)}" for _ in range(num_records)],
        'preferred_companions': np.random.choice(['solo', 'family', 'friends', 'couple'], num_records),

        # Trip Details
        'trip_id': [str(uuid.uuid4()) for _ in range(num_records)],
        'trip_duration': np.random.randint(3, 21, num_records),
        'travel_dates_start': [fake.date_between(start_date='-1y', end_date='+1y').isoformat() for _ in
                               range(num_records)],
        'travel_dates_end': [(datetime.strptime(d, '%Y-%m-%d') + timedelta(days=random.randint(5, 21))).isoformat() for
                             d in [fake.date_between(start_date='-1y', end_date='+1y').isoformat() for _ in
                                   range(num_records)]],
        'origin': [fake.city() for _ in range(num_records)],
        'destination': [fake.city() for _ in range(num_records)],
        'geolocation_tracking': [generate_geolocation() for _ in range(num_records)],
        'time_constraints': np.random.choice(['strict', 'flexible'], num_records),
        'current_mood': np.random.choice(MOODS, num_records),

        # Real-Time Interaction
        'conversational_query': [generate_conversation() for _ in range(num_records)],
        'assistant_response': [fake.sentence() for _ in range(num_records)],
        'favorite_destinations_chat': [fake.country() for _ in range(num_records)],
        'feedback_previous_trips': [fake.sentence() for _ in range(num_records)],
        'flight_status': np.random.choice(FLIGHT_STATUSES, num_records, p=[0.8, 0.15, 0.05]),
        'hotel_availability': np.random.choice(['available', 'limited', 'none'], num_records),
        'weather_forecast': np.random.choice(WEATHER_CONDITIONS, num_records),
        'local_events': [json.dumps([generate_activity() for _ in range(random.randint(1, 3))]) for _ in
                         range(num_records)],

        # Activity Database (embedded as JSON)
        'recommended_activities': [json.dumps([generate_activity() for _ in range(random.randint(2, 5))]) for _ in
                                   range(num_records)]
    }

    return pd.DataFrame(data)


# Generate data in chunks
for chunk in range(0, NUM_RECORDS, CHUNK_SIZE):
    df = generate_user_data(min(CHUNK_SIZE, NUM_RECORDS - chunk))
    df.to_csv(
        'travel_dataset.csv',
        mode='a' if chunk > 0 else 'w',
        header=chunk == 0,
        index=False,
        encoding='utf-8'
    )
    print(f"Processed {chunk + CHUNK_SIZE}/{NUM_RECORDS} records")