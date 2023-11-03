class AppRoutes:

    API_VERSION: str = "/v1.0"

    class Books:
        TAG: str = "books"
        PREFIX: str = "/books"
        POST_URL: str = "/"
        POST_OPENBD_URL: str = "/openbd"
        GET_URL: str = "/"

    class Authors:
        TAG: str = "authors"
        PREFIX: str = "/authors"
        GET_URL: str = "/"

    class Token:
        TAG: str = "token"
        PREFIX: str = "/token"
        POST_URL: str = "/"

    class Users:
        TAG: str = "users"
        PREFIX: str = "/users"
        POST_URL: str = "/"
        GET_URL: str = "/"
