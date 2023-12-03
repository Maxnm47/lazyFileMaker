import os

def create_files(dir_name, script_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    os.makedirs(dir_path, exist_ok=True)

    js_content = f"""function {script_name.capitalize()}Page() {{
    return (
        <div>
            <h1>{script_name.capitalize()}</h1>
        </div>
    )
}}

export default {script_name}Page;
"""

    with open(os.path.join(dir_path, f'{script_name}.js'), 'w') as js_file:
        js_file.write(js_content)

    with open(os.path.join(dir_path, f'{script_name}.css'), 'w') as css_file:
        pass

    return dir_path

directory_name = "blog"
script_name = "blog"
dir_path = create_files(directory_name, script_name)
