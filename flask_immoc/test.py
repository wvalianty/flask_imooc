import os
print(os.path.exists(os.path.realpath('./fisher')))
def import_from():
    if os.path.exists(os.path.realpath('./app')):
        return "app.config.secure"
    else:
        return "app.config.setting"

print(import_from())