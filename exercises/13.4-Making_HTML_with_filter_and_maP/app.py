all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def generate_li (values):
	return list(map(lambda value: f"<li>{value['label']}</li>", filter_colors(values) ))
def filter_colors (values):
	return list(filter(lambda sexy: sexy["sexy"], values))


print(generate_li(all_colors))