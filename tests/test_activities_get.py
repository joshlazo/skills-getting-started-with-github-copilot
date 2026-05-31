def test_get_activities_returns_all_activities_with_no_store_header(client):
    # Arrange

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert response.headers.get("cache-control") == "no-store"
    assert isinstance(payload, dict)
    assert "Chess Club" in payload
    assert "participants" in payload["Chess Club"]
    assert isinstance(payload["Chess Club"]["participants"], list)
