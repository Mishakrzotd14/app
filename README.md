# App API with FastAPI

This project provides a FastAPI-based API that allows you to interact with two main endpoints: "Hello" and "Rps" (rock paper scissors).

## Description

The App API is designed to help you do awesome stuff. It includes endpoints for saying hello and playing rock paper scissors.

## Installation

To install the App API, follow these steps:
1. Clone the repository.
2. Install the required dependencies using `poetry install`.
3. Run the FastAPI application using `uvicorn app.main:app --reload`.

## Usage

### Say Hello
- **Description**: Endpoint to say hello.
- **URL**: `/hello`
- **Method**: GET
- **Response**: Returns a message "Hello What is love".

### Play Rock Paper Scissors (Rps)
- **Description**: Endpoint to play rock paper scissors.
- **URL**: `/rps`
- **Method**: GET
- **Parameters**:
  - `choice` (string): The choice of rock, paper, or scissors.
- **Response**: Returns the result of the game.