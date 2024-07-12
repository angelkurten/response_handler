from response_handler_lib.errors import ErrorResponseConfig, PredefinedErrorCodes
from response_handler_lib.response import Response
import json


class Example:
    def __init__(self):
        # Initialize a new Response object
        self.response = Response()

        # Define and add custom error messages to the configuration
        custom_errors = {
            "CUS_ERR1": "Custom error message 1.",
            "CUS_ERR2": "Custom error message 2."
        }
        ErrorResponseConfig.add_custom_errors(custom_errors)

    def generate_success_response(self):
        # Set data for a successful response
        self.response.data = "This is a successful response."
        return self.response.to_json(include_where=True)

    def generate_error_response(self):
        # Add predefined error to the response
        self.response.add_error(PredefinedErrorCodes.VAL_ERR.value)

        # Add custom error to the response
        self.response.add_error("CUS_ERR1")

        # Return the response as JSON including the location where the errors were generated
        return self.response.to_json(include_where=True)

    def generate_mixed_response(self):
        # Set data for a response with both data and errors
        self.response.data = "This response has both data and errors."

        # Add predefined error to the response
        self.response.add_error(PredefinedErrorCodes.AUTH_ERR.value)

        # Add custom error to the response
        self.response.add_error("CUS_ERR2")

        # Return the response as JSON including the location where the errors were generated
        return self.response.to_json(include_where=True)

    def print_responses(self):
        # Generate and print a successful response
        success_response = self.generate_success_response()
        print("---- Success Response ----")
        print(json.dumps(json.loads(success_response), indent=4))
        print("\n")

        # Generate and print an error response
        error_response = self.generate_error_response()
        print("---- Error Response ----")
        print(json.dumps(json.loads(error_response), indent=4))
        print("\n")

        # Generate and print a mixed response with both data and errors
        mixed_response = self.generate_mixed_response()
        print("---- Mixed Response ----")
        print(json.dumps(json.loads(mixed_response), indent=4))
        print("\n")


# Run the example
example = Example()
example.print_responses()