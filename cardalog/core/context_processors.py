from users.forms import UserRegisterForm

# Adds UserRegisterForm for the Base template(index.html).
# Context Processor
def add_variable_to_context(request):
    return {
        'register_form': UserRegisterForm(),
    }