from fastapi import status


class TestInternalAPI:
    """Test cases for internal API."""

    async def test_health_check(self, client):
        """Test that health check returns a healthy response."""
        response = await client.get("/api/health")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["status"] == "ok"
