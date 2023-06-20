For maintaining a session for logged in users, the frontend should follow these steps:

After the user logs in, the server sends an access token and a refresh token.

For each subsequent request that requires authentication, the frontend should send the access token in the Authorization header.

When the server returns a 401 Unauthorized status (usually indicating the access token has expired), the frontend should send a request to the server with the refresh token to get a new access token.

If the server returns a new access token, the frontend replaces the old access token and continues to make requests. If not, the user is asked to login again.
