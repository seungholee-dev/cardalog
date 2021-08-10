from users.forms import UserRegisterForm

# Adds UserRegisterForm for the Base template(index.html). -> Below Context Variables will be able to be used across the any app actually.
# Context Processor
def add_variable_to_context(request):
    return {
        'register_form': UserRegisterForm(),
    }