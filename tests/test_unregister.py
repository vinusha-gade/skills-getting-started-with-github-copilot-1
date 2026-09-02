def test_unregister_removes_student_from_activity(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity}"
    activities = client.get("/activities").json()
    assert email not in activities[activity]["participants"]


def test_unregister_rejects_unknown_activity(client):
    # Arrange
    activity = "Robotics Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_rejects_student_not_in_activity(client):
    # Arrange
    activity = "Chess Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_unregistered_student_can_sign_up_again(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    unregister_response = client.delete(
        f"/activities/{activity}/signup", params={"email": email}
    )
    signup_response = client.post(
        f"/activities/{activity}/signup", params={"email": email}
    )

    # Assert
    assert unregister_response.status_code == 200
    assert signup_response.status_code == 200
    assert email in client.get("/activities").json()[activity]["participants"]
