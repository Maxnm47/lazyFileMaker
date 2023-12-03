import os

def create_page_dir_and_files(new_page_name):
    dir_path = os.path.join(os.getcwd(), new_page_name)
    os.makedirs(dir_path, exist_ok=True)

    js_content = f"""import React from 'react';
import './{new_page_name}.css';

function {new_page_name.capitalize()}Page() {{
    return (
        <div>
            <h1>{new_page_name.capitalize()}</h1>
        </div>
    );
}}

export default {new_page_name.capitalize()}Page;
"""

    with open(os.path.join(dir_path, f'{new_page_name}.js'), 'w') as js_file:
        js_file.write(js_content)

    with open(os.path.join(dir_path, f'{new_page_name}.css'), 'w') as css_file:
        pass

def append_to_router(new_page_name):
    router_file_path = os.path.join(os.getcwd(), 'router.js')

    with open(router_file_path, 'r') as file:
        lines = file.readlines()

    import_str = f"import {new_page_name.capitalize()}Page from './{new_page_name}/{new_page_name}.js';\n"
    route_str = f"        <Route path='/{new_page_name}' element={{<{new_page_name.capitalize()}Page />}} />\n"


    import_index = next(i for i, line in enumerate(lines) if line.startswith("import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';")) + 1
    lines.insert(import_index, import_str)


    catch_all_route_index = next(i for i, line in enumerate(lines) if line.strip().startswith("<Route path='*'"))
    lines.insert(catch_all_route_index, route_str)

    with open(router_file_path, 'w') as file:
        file.writelines(lines)
#how to use
new_page_name = "blog"
create_page_dir_and_files(new_page_name)
append_to_router(new_page_name)
