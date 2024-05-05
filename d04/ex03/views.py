from django.shortcuts import render

def color_table(request):
    num_shades = 50  # Number of color shades
    step = 255 / (num_shades - 1)  # Step calculation, ensure it covers the full range from 0 to 255
    color_shades = [
        "{:02X}".format(int(i * step)) for i in range(num_shades)
    ]
    context = {
        "color_shades": color_shades
    }
    return render(request, 'ex03/color_table.html', context)
