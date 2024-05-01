import sys

def load_settings():
    import settings
    return {attr: getattr(settings, attr) for attr in dir(settings) if not attr.startswith('__')}

def render_template(template_path, context):
    with open(template_path, 'r') as file:
        content = file.read()
    for key, value in context.items():
        content = content.replace(f"{{{key}}}", value)
    return content

def main():
    if len(sys.argv) != 2:
        print("Error: Incorrect number of arguments.")
        sys.exit(1)
    
    template_path = sys.argv[1]
    if not template_path.endswith('.template'):
        print("Error: File must have a .template extension.")
        sys.exit(1)
    
    try:
        context = load_settings()
        output_content = render_template(template_path, context)
        output_path = template_path.replace('.template', '.html')
        with open(output_path, 'w') as file:
            file.write(output_content)
        print(f"Output generated at {output_path}")
    except FileNotFoundError:
        print("Error: File does not exist.")
        sys.exit(1)

if __name__ == "__main__":
    main()

