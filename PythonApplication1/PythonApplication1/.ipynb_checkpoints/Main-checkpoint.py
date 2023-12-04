from flask import Flask, render_template_string
import folium
import webbrowser
import Map

app = Flask(__name__)

@app.route("/")
def home():
    map_obj = Map.show_map_with_route()
    header = map_obj.get_root().header.render()
    body_html = map_obj.get_root().html.render()
    map_script = map_obj.get_root().script.render()
    
    return render_template_string(
        """
        <!DOCTYPE html>
        <html>
            <head>
                {{ header|safe }}
                <title>Bản đồ thành phố Hồ Chí Minh</title>
                <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
            </head>
            <body>
                {{ body_html|safe }}
                <script>
                    {{ map_script|safe }}
                </script>
            </body>
        </html>
        """,
        header=header,
        body_html=body_html,
        map_script=map_script
    )

def open_browser():
    webbrowser.open_new_tab("http://127.0.0.1:50100/")  # Thay đổi URL tùy theo cổng bạn sử dụng

# Chạy ứng dụng và sau đó tự động mở trình duyệt
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=50100, debug=True)
    open_browser()
