import random


def simulate_usage_time(session_duration_minutes, max_interval_duration_minutes):
    """
    Usage Time Data:
    - Define a session duration (e.g., 8 hours for a typical workday).
    - Divide the session into intervals (e.g., 30 minutes each).
    - Ensure that the total usage time doesn't exceed the session duration.
    """

    usage_data = []

    remaining_time = session_duration_minutes

    while remaining_time > 0:
        activity_duration = min(random.randint(10, max_interval_duration_minutes), remaining_time)
        usage_data.append(activity_duration)
        remaining_time -= activity_duration + 1  # Add 1 to avoid consecutive inactivity periods

    return usage_data


def simulate_inactivity(usage_data):
    """
    Inactivity Data:
    - Randomly generate inactivity periods within the activity session duration.
    """
    inactivity_data = []
    for duration in usage_data:
        inactivity_duration = random.randint(0, duration // 2)
        inactivity_data.append(inactivity_duration)
    return inactivity_data


def simulate_activity_labels(inactivity_data, activity_data, threshold_ratio, activity_threshold):
    """
    Activity Labels:
    - Based on your criteria (e.g., if the ratio of inactivity time to activity time exceeds a threshold,
    label it as "break needed"), assign labels to each interval of simulated data.
    """
    activity_labels = []
    # i = 0
    for inactivity_duration, activity_duration in zip(inactivity_data, activity_data):
        # print(inactivity_duration / activity_duration)
        if activity_duration > activity_threshold and (inactivity_duration / activity_duration) <= threshold_ratio:
            activity_labels.append("break needed")
            # print(inactivity_duration / activity_duration)
            # i += 1
        else:
            activity_labels.append("no break needed")
    # print(i)
    return activity_labels


# simulate data
def simulate_data(inactivity_threshold_ratio=0.15, activity_threshold=30):
    # Simulate usage time for 2 months of  8-hour workday with 60-minute intervals
    usage_data = simulate_usage_time(60 * 8 * 60, 60)
    print(usage_data)

    # Simulate inactivity
    inactivity_data = simulate_inactivity(usage_data)
    print(inactivity_data)

    # Simulate activity labels based on the ratio of inactivity time to activity time
    activity_labels = simulate_activity_labels(inactivity_data, usage_data, inactivity_threshold_ratio,
                                               activity_threshold)
    print(activity_labels)
    return usage_data, inactivity_data, activity_labels
