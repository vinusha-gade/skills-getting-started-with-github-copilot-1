def test_get_activities_returns_activity_details(client):
    # Arrange
    expected_activity = "Chess Club"
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert expected_activity in activities
    assert set(activities[expected_activity]) == expected_fields
    assert activities[expected_activity]["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]


def test_get_activities_includes_empty_participant_lists(client):
    # Arrange
    expected_activity = "Soccer Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.json()[expected_activity]["participants"] == []
