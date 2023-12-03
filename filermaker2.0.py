import os

def create_files(dir_names):
    router_content = "import React from 'react';\nimport { BrowserRouter as Router, Routes, Route } from 'react-router-dom';\n\n"

    for script_name in dir_names:
        # Create directory in the current working directory
        dir_path = os.path.join(os.getcwd(), script_name)
        os.makedirs(dir_path, exist_ok=True)

        # JavaScript file content
        js_content = f"""import React from 'react';
import './{script_name}.css';

function {script_name.capitalize()}Page() {{
    return (
        <div>
            <h1>{script_name.capitalize()}</h1>
        </div>
    );
}}

export default {script_name.capitalize()}Page;
"""

        # Write JavaScript file
        with open(os.path.join(dir_path, f'{script_name}.js'), 'w') as js_file:
            js_file.write(js_content)

        # Create empty CSS file
        with open(os.path.join(dir_path, f'{script_name}.css'), 'w') as css_file:
            pass

        # Update router content
        router_content += f"import {script_name.capitalize()}Page from './{script_name}/{script_name}.js';\n"

    # Add routes to router content
    router_content += "\nfunction AppRouter() {\n  return (\n    <Router>\n      <Routes>\n"
    for script_name in dir_names:
        router_content += f"        <Route path='/{script_name}' element={{<{script_name.capitalize()}Page />}} />\n"
    router_content += "        <Route path='*' element={<h1>404</h1>} />\n      </Routes>\n    </Router>\n  );\n}\n\nexport default AppRouter;"

    # Write router.js file
    with open(os.path.join(os.getcwd(), 'router.js'), 'w') as router_file:
        router_file.write(router_content)

# Example usage
page_names = ["home", "about", "contact"]
create_files(page_names)
