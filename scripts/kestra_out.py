from kestra import Kestra

name = "Harish"
message = "Hi!"

Kestra.outputs(
  {
    'name': name,
    'message': message
  }
)