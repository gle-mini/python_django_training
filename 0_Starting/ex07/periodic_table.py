def parse_line(line: str):
    name, attributes = line.split("=")
    attributes_dict = {key.strip(): value.strip() for key, value in (item.split(":") for item in attributes.split(", "))}
    attributes_dict["name"] = name.strip()
    return attributes_dict

def generate_html_table(periodic_table):
    TEMPLATE = """
      <td style="border: 1px solid black; padding:10px">
        <h4>{name}</h4>
        <ul>
          <li>No {number}</li>
          <li>{small}</li>
          <li>{molar}</li>
          <li>{electron} electron</li>
        </ul>
      </td>
    """
    body = "<tr>"
    current_position = 0
    for element in periodic_table:
        element_position = int(element["position"])
        if current_position > element_position:
            body += "</tr>\n    <tr>"
            current_position = 0
        body += "      <td></td>\n" * (element_position - current_position - 1)
        current_position = element_position
        body += TEMPLATE.format(**element)
    body += "</tr>\n"
    return body

def main():
    HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Periodic Table</title>
  <style>
    table{{ border-collapse: collapse; }}
    h4 {{ text-align: center; }}
    ul {{ list-style: none; padding-left: 0px; }}
  </style>
</head>
<body>
  <table>{body}</table>
</body>
</html>
    """

    with open("periodic_table.txt", "r") as f:
        periodic_table = [parse_line(line.strip()) for line in f if line.strip()]

    table_body = generate_html_table(periodic_table)

    with open("periodic_table.html", "w") as f:
        f.write(HTML_TEMPLATE.format(body=table_body))

if __name__ == '__main__':
    main()

