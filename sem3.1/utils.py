from flask import request, redirect, render_template


def local_routing(url_key, default_page, **kwargs):
	url = request.args.get(url_key, '')
	if not url:
		return render_template(default_page, **kwargs)
	return redirect(url)
