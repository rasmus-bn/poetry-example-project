from myapp.module1.greeting import echo_greeting


def test_version():
    # Arrange
    sender_name = 'Bob'

    # Act
    response = echo_greeting(sender_name=sender_name)

    # Assert
    assert response == 'Hello from Bob!'
