# App API

App API helps you do awesome stuff. 🚀

## Hello

Say **Hello What is love**.

## Rps

You will be able to play in rock paper scissors

## API Documentation

### Introduction

The App API provides endpoints for saying hello and playing rock paper scissors.

### Base URL

The base URL for all endpoints is `http://localhost:8080`.

### Authentication

The App API does not require authentication for accessing the provided endpoints.

### Endpoints

#### Say Hello
- **Description**: Endpoint to say hello.
- **URL**: `/hello`
- **Method**: GET
- **Tags**: hello
- **Response**: Returns a message "Hello What is love".

#### Play Rock Paper Scissors
- **Description**: Endpoint to play rock paper scissors.
- **URL**: `/rps`
- **Method**: GET
- **Tags**: rps
- **Parameters**:
  - `choice` (string): The choice of rock, paper, or scissors.
- **Response**: Returns the result of the game.

### Models

The App API does not currently have any predefined models.

### Contact Information

For any inquiries or support, please contact MKurziankou at MKurzenkov.otd14@gmail.com.

### Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
